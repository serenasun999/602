# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os
import tensorflow as tf
import logging
import sklearn.metrics as metrics
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.preprocessing.image import ImageDataGenerator

from keras.layers import Dense, GlobalAveragePooling2D, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.inception_v3 import InceptionV3
from keras.models import Model, Sequential
from keras.callbacks import EarlyStopping
from keras.optimizers import SGD
from keras import backend as K
from keras import optimizers

# Silence messages
logging.disable(logging.WARNING) 
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Set global seed 
tf.random.set_seed(42)

# ===========================================================================================
# Image preprocessing
# Referenced code by Sohom Majumder (2021)
# https://www.kaggle.com/code/sohommajumder21/coronahack-chest-x-ray-keras-and-resnet50-both
# ===========================================================================================

def SortImages(metadata):
    '''
    Sorts CoronaHack train and test images into target folders within new directories (training and testing) for use with Keras ImageDataGenerator
    flow from directory. Takes pandas dataframe with CoronaHack metadata as input (Chest_xray_Corona_Metadata.csv).
    Assumes train images are in ./train and test images are in ./test.
    https://www.kaggle.com/datasets/praveengovi/coronahack-chest-xraydataset
    '''    
    # Assign multi-class classification labels to each image (normal, viral pneumonia, or bacterial pneumonia)
    metadata.loc[(metadata['Label'] == 'Normal'), 'label'] = 'Normal'
    metadata.loc[(metadata['Label'] == 'Pnemonia') & (metadata['Label_1_Virus_category'] == 'Virus') & (metadata['Label_2_Virus_category'].isnull()), 'label'] = 'Virus'
    metadata.loc[(metadata['Label'] == 'Pnemonia') & (metadata['Label_1_Virus_category'] == 'bacteria') & (metadata['Label_2_Virus_category'].isnull()), 'label'] = 'Bacteria'
    metadata = metadata[['X_ray_image_name', 'Dataset_type', 'label']]
    
    # Export labeled files to csv for later use
    metadata.to_csv('labeled_image_files.csv')

    # Split test and train metadata
    train_metadata = metadata[metadata['Dataset_type'] == 'TRAIN']
    test_metadata = metadata[metadata['Dataset_type'] == 'TEST']
    
    # Make new directories to sort images
    try:
        os.makedirs('./training/Normal')
        os.makedirs('./training/Virus')
        os.makedirs('./training/Bacteria')
        os.makedirs('./testing/Normal')
        os.makedirs('./testing/Virus')
        os.makedirs('./testing/Bacteria')
    except:
        pass

    # Sort images if not sorted already
    if len(os.listdir('./training/Bacteria')) == 0:
        
        # Define paths
        train_source = './train'
        train_normal = './training/Normal'
        train_bacteria = './training/Bacteria'
        train_virus = './training/Virus'
        test_source = './test'
        test_normal = './testing/Normal'
        test_bacteria = './testing/Bacteria'
        test_virus = './testing/Virus'
        
        # Get file names for training image categories
        training_normal = train_metadata.loc[(train_metadata['label'] == 'Normal'), 'X_ray_image_name']
        training_virus = train_metadata.loc[(train_metadata['label'] == 'Virus'), 'X_ray_image_name']
        training_bacteria = train_metadata.loc[(train_metadata['label'] == 'Bacteria'), 'X_ray_image_name']
        
        # Normal images
        for i in training_normal.values:
            path = os.path.join(train_source, i)
            shutil.copy(path, train_normal)
    
        # Viral pneumonia
        for i in training_virus.values:
            path = os.path.join(train_source, i)
            shutil.copy(path, train_virus)
    
        # Bacterial pneumonia
        for i in training_bacteria.values:
            path = os.path.join(train_source, i)
            shutil.copy(path, train_bacteria)
        
        # Get file names for training image categories
        testing_normal = test_metadata.loc[(test_metadata['label'] == 'Normal'), 'X_ray_image_name']
        testing_virus = test_metadata.loc[(test_metadata['label'] == 'Virus'), 'X_ray_image_name']
        testing_bacteria = test_metadata.loc[(test_metadata['label'] == 'Bacteria'), 'X_ray_image_name']

        # Normal images
        for i in testing_normal.values:
            path = os.path.join(test_source, i)
            shutil.copy(path, test_normal)
    
        # Viral pneumonia
        for i in testing_virus.values:
            path = os.path.join(test_source, i)
            shutil.copy(path, test_virus)
    
        # Bacterial pneumonia
        for i in testing_bacteria.values:
            path = os.path.join(test_source, i)
            shutil.copy(path, test_bacteria)

# Load metadata
metadata = pd.read_csv('Chest_xray_Corona_Metadata.csv')

# Sort images into target folders within test and train directories
SortImages(metadata)

# Set up image generators for test and validation data
datagen = ImageDataGenerator(rescale=1./255)

# Training flow
train_gen = datagen.flow_from_directory(directory='./training', batch_size=128, class_mode='categorical',
                                              subset='training', target_size=(299, 299), shuffle=False, # Target size set to 299 for InceptionV3
                                              seed=42)

# Validation flow
val_gen = datagen.flow_from_directory(directory='./testing', batch_size=128, class_mode='categorical',
                                          target_size=(299, 299), shuffle=False,
                                              seed=42)

# ====================================================================
# InceptionV3 model training
# Referenced code by ceceshao1 
# https://gist.github.com/ceceshao1/cb834ed819628244093a2b61408c86e0
# ====================================================================
# Image dimensions for InceptionV3
input_shape = (299, 299, 3)

# Params
batch_size = 128
min_delta = 0.0001
patience = 4
train_samples = train_gen.samples
val_samples = val_gen.samples

# Load pretrained model
inception_base = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)

# Add some top layers
x = inception_base.output
# Global spatial average pooling layer
x = GlobalAveragePooling2D()(x)
# Dropout
x = Dropout(0.2, seed=42)(x)
# Fully-connected layer
x = Dense(1024, activation='relu')(x)
# Output layer with three nodes for classification
out = Dense(3, activation='softmax')(x)

model = Model(inputs=inception_base.input, outputs=out)

# Train only top layers first
for layer in inception_base.layers:
    layer.trainable = False

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(
    train_gen,
    steps_per_epoch = train_samples // batch_size,
    epochs = 25,
    validation_data = val_gen,
    validation_steps = val_samples // batch_size,
    callbacks=[EarlyStopping(monitor='val_loss', min_delta = min_delta, patience=patience)],
    verbose=0)

# Recompile and use SGD with low learning rate
model.compile(optimizer=SGD(learning_rate=0.0001, momentum=0.8), loss='categorical_crossentropy',metrics=['accuracy'])

# Train again
model.fit(
    train_gen,
    steps_per_epoch= train_samples // batch_size,
    epochs=15,
    validation_data= val_gen,
    validation_steps= val_samples // batch_size,
    callbacks=[EarlyStopping(monitor='val_loss', min_delta=min_delta, patience=patience)],
              verbose=0,
)

model.save("saved_model.h5")
print('Training complete.')