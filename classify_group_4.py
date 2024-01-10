# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import random
import cv2
import sklearn.metrics as metrics
import tensorflow as tf
import logging


from IPython.display import Image, display
from PIL import Image
from tensorflow import keras
from keras import backend as K
from keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

# Silence messages
logging.disable(logging.WARNING) 
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
 
# Set global seed 
tf.random.set_seed(42)
np.random.seed(42)

# Load saved model
model = keras.models.load_model('saved_model.h5')

# Define batch size
batch_size = 128

# Create test data generator
test_datagen = ImageDataGenerator(rescale=1./255)

test_gen = test_datagen.flow_from_directory(directory='./testing', batch_size=128, class_mode='categorical',
                                          target_size=(299, 299), shuffle=False,
                                              seed=42)

# Calculate and display metrics
# Reset test generator
test_gen.reset()

# Get predicted values
y_pred = model.predict(test_gen, test_gen.samples / batch_size)
pred = np.argmax(y_pred, axis=1)

# Get true values
true =test_gen.classes

# Change values to categorical for micro AUC calculation
n_classes = 3
y_true_cat = to_categorical(true, num_classes=n_classes)
y_pred_cat = to_categorical(pred, num_classes=n_classes)

print('Accuracy:\n', metrics.accuracy_score(true, pred))
print('Micro AUC:\n', metrics.roc_auc_score(y_true_cat, y_pred_cat, average='micro', multi_class='ovo'))
print('Micro F1 Score:\n', metrics.f1_score(true, pred, average='micro'))
print('Micro Precision:\n', metrics.precision_score(true, pred, average='micro'))
print('Micro Recall:\n', metrics.recall_score(true, pred, average='micro'))

# Create dataframe with image filenames and model predictions
labels = (test_gen.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in pred]

filenames=test_gen.filenames


new_filenames = []

for file in filenames:
    new_file = file.split('/')[1]
    new_filenames.append(new_file)

results=pd.DataFrame({'Filename':new_filenames,
                      'Predictions':predictions})

# ===========================================
# Model explainability
# Source Code:
# https://keras.io/examples/vision/grad_cam/
# ===========================================

def get_img_array(img_path, size):
    # `img` is a PIL image of size 299x299
    img = keras.preprocessing.image.load_img(img_path, target_size=size)
    # `array` is a float32 Numpy array of shape (299, 299, 3)
    array = keras.preprocessing.image.img_to_array(img)
    # We add a dimension to transform our array into a "batch"
    # of size (1, 299, 299, 3)
    array = np.expand_dims(array, axis=0)
    return array


def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    # First, we create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    # This is the gradient of the output neuron (top predicted or chosen)
    # with regard to the output feature map of the last conv layer
    grads = tape.gradient(class_channel, last_conv_layer_output)

    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    # then sum all the channels to obtain the heatmap class activation
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

    # Get name of last convolutional layer
last_conv_layer = None
for layer in reversed(model.layers):
    if 'conv2d' in layer.name:
        last_conv_layer = layer
        break

# check what the name of the last layer is (if needed)
if last_conv_layer is not None:
    last_conv_layer_name = last_conv_layer.name

# Randomly Selecting 5 Images
# Set the number of random images to display
num_images = 5

# Load and preprocess the images
img_dir = './test/'
img_size = (299, 299)
img_paths = results['Filename']
random.shuffle(img_paths)
img_paths = img_paths[:num_images]

for img_path in img_paths:
    img_path = os.path.join(img_dir, img_path)
    img_array = preprocess_input(get_img_array(img_path, size=img_size))

    # Generate Grad-CAM heatmap
    heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)

    # Display the original image
    img = cv2.imread(img_path)
    print("image:", img_path)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # Get predicted labels
    pred = model.predict(img_array)
    pred_class_index = np.argmax(pred, axis=1)
    pred_class = labels[pred_class_index[0]]

    # Display the heatmap overlaid on the original image
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
    overlayed_img = cv2.addWeighted(img, 0.5, heatmap, 0.5, 0)
    plt.imshow(cv2.cvtColor(overlayed_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title(pred_class)
    plt.show()