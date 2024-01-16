# Data Science and Analytics Projects
##### REPORTS AND FILES ARE UNDER BRANCH - RESULT :)

# 601 Project - Working with Data and Visualization - "Analysis of Calgary’s Historical Air Quality Data"
The project is a detailed study examining air quality changes over 39 years in Calgary due to anthropogenic factors, particularly greenhouse gas emissions. It leverages data from Alberta Environment and Parks and the World Health Organization to compare local and global trends.

1. **Objective and Data Sources**: The project aims to understand the variability in greenhouse gas emissions over nearly four decades in Calgary. It uses two primary datasets: 'Historical Air Quality' from the Calgary Region Airshed Zone and 'Global Data Trends' from the WHO.

    #### Guiding Questions
    1. How did the environmental parameters such as greenhouse gasses (Carbon Dioxide, Methane, Nitrogen Dioxide and Nitric Oxide), air quality index, wind speed and temperature change over the course of 39 years?
    2. Is there any correlation between temperature and greenhouse gasses and between wind speed and greenhouse gasses over the 39 years? 
    3. What is the distribution of pollutants throughout Calgary?
       
2. **Methodology and Analysis**: The study employed data wrangling techniques to clean and format large datasets. Statistical analysis was carried out to draw correlations between air pollutants and non-pollutant factors like temperature and wind speed across different locations in Calgary and compared with global trends.

3. **Key Findings**: 
   - A decline in Nitrogen Dioxide and Nitric Oxide levels was observed, attributed to technological advancements and increased environmental awareness.
   - Methane and Carbon Dioxide levels showed an upward trend, likely linked to population growth and energy consumption.
   - The Air Quality Index fluctuated over the years, with notable dips potentially indicating data inconsistencies or specific environmental events.

4. **Conclusions and Recommendations**: The report concludes that while some pollutant levels have decreased, others like Methane and Carbon Dioxide continue to rise, posing environmental concerns. It highlights the importance of individual and collective actions towards eco-friendly practices.

5. **Next Steps**: Future work could focus on examining other greenhouse gas emissions within Alberta to assess the impact of the oil and gas industry more closely and explore the relationship between air quality and proximity to industrial sites.

The project underscores Calgary's progress in air quality management compared to global trends but also emphasizes the need for ongoing efforts to address the rise in certain greenhouse gases.


# 602 Project - Statistical Data Analysis - "Historical Air Quality Analysis"
### Focus of statistical investigation
The focus of our statistical investigation is to understand if there is any statistical difference between the particulate matter recorded in Calgary vs particulate matter recorded globally in order to gain evidence to support or reject our hypothesis that PM2.5 globally is equal to PM2.5 in Calgary. We also want to determine how greenhouse gas emissions changed over the years in Calgary by plotting the distribution of greenhouse gas emissions over the years and estimating the population average via bootstrapping. This data is leveraged by the Government of Alberta to visualize, analyze and continually monitor air pollution. This enables Calgary residents to protect themselves and take the necessary precautions especially those who are health compromised. 

1. **Objective**: To understand how Calgary's air quality has changed over the years and how it compares to global data, with a specific look at particulate matter (PM2.5) and greenhouse gases in relation to Calgary's population growth.

2. **Data Sources and Methodology**: Utilizing the "Historical Air Quality" dataset and WHO Air Quality Database, the team applied statistical methods such as hypothesis testing, permutation tests, and linear regression analysis.

3. **Key Findings**:
   - There is a statistically significant difference between PM2.5 levels in Calgary and the global average, with Calgary's levels being different from the world's.
   - No significant difference was found in the Air Quality Index between central and non-central areas of Calgary, challenging the assumption that central areas would have higher pollution levels.
   - A strong negative correlation was identified between population growth and levels of Nitrogen Dioxide (NO2) and Nitric Oxide (NO), contrary to expectations of increased emissions with population growth.

4. **Conclusions**: The study concluded that Calgary's PM2.5 levels are distinct from global levels and that central Calgary does not necessarily have poorer air quality compared to other areas. Additionally, despite population growth, some greenhouse gas emissions have decreased due to improved technology and environmental awareness.

5. **Next Steps**: It is suggested to analyze other parameters from the primary dataset and to use the established models for predictive analysis regarding the impact of population growth on air quality.
   

# 603 Project - Statistical Modelling with Data - "Multiple Regression Analysis: Prediction of Average Overall Achievement Score of schools in North Carolina"
1. **Objective**: In our research for this project, we discovered that many different factors contribute to an individual’s success in terms of their education. The goal of this project is to explore these factors and analyze how each factor negatively, or positively impacts an individual’s success in the education system to be able to make informed decisions on the overall quality of education these students are receiving, as well as predicting school achievement success.

2. **Data Sources and Methodology**: Utilizing the open source dataset “School Report Cards (SRC)” which was taken from: the North Carolina Department of Public Instruction. All datasets have a key column “agency_code” which includes various information regarding school and staff performance together with aggregated scores for each school in every subject (Math, English and etc.) for each year. 15 independent variables were narrowed down via stepwise regression for feature selection. Multiple regression analysis was applied to the dataset. The methodology involved checking for multicollinearity, individual t-tests, and stepwise regression to finalize the model.

3. **Key Findings and Conclusions**:
    - The results indicated that factors like school development, staff performance, and financial assets were significant. The final model incorporated interaction terms and was validated against regression assumptions. The main challenge was homoscedasticity, which was addressed using transformations like Box-Cox. The model's adjusted R-squared value was 61.64%, reflecting the unpredictability of human-related data.
  
4. **Next Steps**:The study suggests future research could focus on individual student-level data to refine predictions.

# 604 Project - Working with Data at Scale - "Health Outcomes Related to Air Quality and Economic Factors in New York City"
1. **Objective**: The project examines the relationships between air quality and neighbourhood poverty, and see what effect this has on cancer rates and incidents of asthma in New York City. It discovered that lung cancer is strongly correlated to air pollution, and chose to investigate that along with 3 other types of cancer that we think will also be affected and that we found interesting. The cancers that be investigated are Lung cancer, Larynx cancer, Esophageal cancer, and Non-Hodgkins Lymphoma.

    **4 guiding questions**:
    - By looking at different areas of New York City, can we conclude in general a poor neighbourhood has a higher cancer rate and worse air quality?
    - Which pollutants have the highest correlations with which cancers?
    - Does poor air quality increase the prevalence of asthma in adults? Does the borough in NYC affect this? Which pollutants have the greatest effect on asthma incidents?
    - Do the poorest neighbourhoods have the highest incidents of asthma among adults?
  
2. **Data Source and Methodology**:
    - The dataset for Asthma incidence rate for the past 12 months for adults from 2003 to 2020. This is an open-source dataset that was taken from the New York City Department of Health Environment and Health Data Portal from the New York City government website.
    - The dataset for Cancer Incidence for adults is from 2007 - 2011. This is an open-source dataset that was taken from the New York City Department of Health Environment and Health Data Portal from the New York City government website. The four types of cancers that we are focusing on are Lung and Bronchus cancer, Larynx cancer, Esophageal cancer, and Non-Hodgkins Lymphoma.
    - The dataset for air quality measurement for NYC is from 2011. This is an open-source dataset that was taken from the New York City Department of Health Environment and Health Data Portal from the New York City government website. When combining the tables for this dataset, the pollutants that had matching columns were Nitrogen Dioxide, Nitric Oxide, and PM2.5. Therefore, our study will be focusing on these 3 pollutants.
    - The dataset for neighbourhood poverty is from 2007 - 2011. This is an open-source dataset that was taken from the New York City Department of Health Environment and Health Data Portal from the New York City government website.

4. **Tools Used**: All datasets were cleaned and loaded to the SQL server. Data were operated via SQL queries. A regression analyst was applied for specific questions.

5. **Results**:
    - The results of our Pearson's correlation show that there is *no correlation* between poverty level and the presence of Nitrogen Dioxide, Nitric Oxide, or PM2.5 in New York City.
    - According to Pearson's correlation, we discover that Non-Hodgkins lymphoma is *significantly positively correlated* with Nitrogen Dioxide, Nitric Oxide, and PM2.5.
    - According to Pearson's correlation, we discover that Larynx cancer is *not correlated* with Nitrogen Dioxide, Nitric Oxide, or PM2.5.
    - According to Pearson's correlation, we discover that Esophageal cancer is *significantly positively correlated* with PM2.5.
    - According to Pearson's correlation, we discover that Lung and Bronchus cancer is *not* correlated with Nitrogen Dioxide, Nitric Oxide, or PM2.5.
    - Notably, the bar graphs shown above indicate that Staten Island has the highest rates of Lung and bronchus cancer cases, but has among the lowest rates of Nitrogen Dioxide, Nitric Oxide, and PM2.5.
    - Our Pearson's correlation shows that there is no significant correlation between Asthma and Nitrogen Dioxide, Nitric Oxide, or PM2.5.
    - From the bar graphs, we can see that Manhattan has the highest rates of air pollution across all boroughs of Manhattan, but has the lowest mean rate of asthma incidents, whereas The Bronx has average levels of air pollutants, but the highest rate of asthma incidents.
    -  From the scatter plot, there is no obvious relationship between the prevalence of Asthma and Nitrogen Dioxide, Nitric Oxide or PM25.
    -  We use the Pearson correlation coefficient and p-value for testing correlation. As a result, all values we get contain zero thus we could not conclude there is a relationship between the prevalence of asthma and nitrogen dioxide, the prevalence of asthma and nitric oxide or the prevalence of asthma and particulate matter.

- **Next Steps**: For the future, we would like to see if there are machine learning algorithms that can predict the number of cancer cases and asthma incidents based on the levels of air pollution. We would also like to have data that contains different kinds of air pollutants other than the ones we studied so we can have a more accurate depiction of any correlations we might discover. This would be useful in aiding the NYC government to regulate the levels of air pollution in New York City to minimize the impact this has on cancer cases and asthma.

# 621 Project - Advanced Statistical Modelling - "Investigating the Association between Thalassemia and Heart Disease using Logistic Regression Modeling"
1. **Objectives**: The primary objective of this study was to determine whether the presence of thalassemia is associated with a diagnosis of heart disease and, if so, whether it is associated with increased severity of heart disease. The secondary objective of this study was to determine if a thalassemia diagnosis is associated with decreased serum LDL cholesterol levels.
   
3. **Data Source and Methodology**: The dataset used in this study containing information collected at the Cleveland Clinic in 1988 is publicly available from the UCI Machine Learning Repository, Center for Machine Learning and Intelligent Systems (Dua & Graff, 2019). Utilizing logistic regression and linear regression models. All hypothesis testing was conducted using a predetermined significance level (ɑ) of 0.05; all results with p-values lower than this limit were considered statistically significant. In addition, 95% confidence intervals are reported for all estimated regression coefficients and odds ratios to provide a range of values in which the true population parameter is likely to fall. These confidence intervals were assessed to determine if they included 0 (for regression coefficients) or 1 (for odds ratios), which would indicate no significant effect.
4. **Conclusion**: Heart disease is a common and multifactorial condition that represents a major health concern. This cross-sectional study had two objectives. The first was to investigate the relationship between thalassemia and heart disease, examining not only the presence of thalassemia as a risk factor for heart disease but also its association with the severity of heart disease. The second was to explore the link between thalassemia and cholesterol levels to better understand the potential impact on heart disease. The descriptive statistics showed that patients with thalassemia were more often male and had a higher mean age and resting blood pressure than patients without thalassemia. Patients with thalassemia also experienced more exercise-induced angina and less chest pain. The binary logistic regression analysis found that thalassemia, age group, sex, chest pain type, exercise-induced angina, and resting ECG were significant predictors of heart disease. Patients with thalassemia were 5.2845 times more likely to develop heart disease compared to patients without thalassemia. Although the ordinal logistic regression model provided a similar conclusion, its results are considered to be invalid due to the violation of the proportional odds assumption. We also found that there was no significant difference in the serum LDL cholesterol levels between the exposed (thalassemia) and unexposed (no thalassemia) groups.
5. **More Details in Report**

# 622 Project - Machine Learning for Health Data Science - "Chest X-Ray Classification"
The "Chest X-Ray Classification" project involves classifying chest X-ray images using various pre-trained machine learning models. The project aimed to identify the most efficient model for this purpose. Six different models, including VGG16, ResNet50, InceptionV3, MobileNetV3, DenseNet121, and EfficientNetB7, were tested. InceptionV3 emerged as the top performer, combining high accuracy with efficient runtimes. The team employed a transfer learning approach, fine-tuning InceptionV3 by altering its layers and experimenting with various hyperparameters. The report also outlines specific contributions in areas like image preprocessing and model training.

# 623 Project - Big Data in Health
1. **Utilizing International Stroke Trail (IST) Dataset**
    - Objectives: 
        - What are the characteristics of the patient groups (aspirin and high heparin)?
        - The primary purpose of the study is to investigate when patients who have not received any aspirin within 3 days before randomization or heparin within 24 hours before randomization and who have not had any symptoms noted on waking (wake-up stroke), the hazard ratio for death difference in the aspirin group and high-dose heparin group in a stroke trial.
        - The secondary purpose of the study is to investigate differences in efficacy (survival rate) among treatments for various stroke subtypes (ischaemic stroke, hemorrhagic stroke and indeterminate stroke) after six months.

2. **Utilizing Canada COVID-19 Dataset**
    - Objectives:
        - This study provides a comprehensive picture of mental illness prevalence in Canada by gender and geography in 2020 and 2021 to inform public health and policy efforts to address mental
health issues in the population. To make better mental health interventions, an overview of mental illness distribution across Canada is necessary.
    - Methodology:
        - From Mental Illness during the Pandemic: Survey on COVID-19 and Mental Health (Cycles 1 and 2). Cycle 1 is from September-December 2020, and cycle 2 is from Feb - May 2021
            - Proportion (%) screening positive for GAD, MDD, and GAD and/or MDD, by age group, by gender, Canada (Cycles 1 and 2)
            - Proportion (%) reporting daily heavy alcohol drinking and cannabis use, by GAD and/or MDD, Canada (Cycles 1 and 2)
            - Proportion (%) screening positive for PTSD, by age group, by gender, Canada (Cycles 1 and 2)
            - Proportion (%) reporting impacts of COVID-19, by PTSD, Canada (Cycles 1 and 2)
        - From Map of Canadian mental health during the COVID-19 pandemic
            - Percentage (%) of the population aged 18 years and older who showed moderate to severe symptoms of generalized anxiety disorder, by province/territorial capital, all adults/females/males, 2020 and 2021 SCMH - Survey on COVID-19 and Mental Health
            - Percentage (%) of the population aged 18 years and older who showed moderate to severe symptoms of major depressive disorder, by province/territorial capital, all adults/females/males, 2020 and 2021 SCMH - Survey on COVID-19 and Mental Health
            - Percentage (%) of the population aged 18 years and older who showed moderate to severe symptoms of post-traumatic stress disorder (PTSD), by province/territorial capital, all adults/females/males, 2020 and 2021 SCMH - Survey on COVID-19 and Mental Health
3. **More Details in Report**

# 624 Project - Advanced Exploration and Visualization in Health - Visualization and Tableau
1. **Tools** Python and Tableau
2. **Libraries** Plotly, Matplotlib, Seaborn, Geopandas
3. **Tableau Project** - An Analysis of Renal Failure Using MIMIC-IV
    - The project utilizes the MIMIC-IV dataset, the data files from the hosp folder within the MIMIC-IV, courtesy of PhysioNet (https://physionet.org/content/mimiciv/2.2/). 
4. **More Details in Report**


# Dataset
- The dataset we have chosen for the 601 and 602 projects is “Historical Air Quality”  which was collected by the Calgary Region Airshed Zone and submitted to Alberta Environment and Parks (AEP). This information is publicly available and can be used from the City of Calgary’s Open Data Portal. City of Calgary’s Open Data Portal Historical Air Quality [online]. Available at: https://data.calgary.ca/Environment/Historical-Air-Quality/uqjm-jxgp/data
- WHO Air Quality Database. WHO Air Quality Database (Update 2022), Available at: https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database
- The datasets we have chosen for 603 are from The North Carolina Department of Public Instruction. School Report Card Resources for Researchers. Accessed at " https://www.dpi.nc.gov/data-reports/school-report-cards/school-report-card-resources-researchers" on 11/15/2022.
- The datasets we have chosen for 604 through different databases were collected and published by the American Community Survey, which is publicly available on the New York City Department of Health Environment and Health Data Portal from the New York City government website.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Black carbon. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2024#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Fine particles (PM 2.5). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2023#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Nitric oxide (NOx). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2028#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Nitrogen dioxide (NO2). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2025#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Ozone (O3). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2027#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal."Neighborhood Air Quality" data. Sulfur dioxide (SO2). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/air-quality/?id=2026#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Adults asthma prevalence" data. Adults with asthma (past 12 months). Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/asthma/?id=18#display=summary" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Economic conditions" data. Neighborhood poverty. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/economic-conditions/" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Carbon monoxide" data. Carbon monoxide incidents. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/carbon-monoxide-incidents/" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Cancer" data. Lung and bronchus cancer. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/cancer/" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Cancer" data. Non-Hodgkin's lymphomas. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/cancer/" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Cancer" data. Esophageal cancer. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/cancer/" on 10/31/2022.
  - New York City Department of Health, Environment & Health Data Portal. "Cancer" data.Larynx cancer. Accessed at "https://a816-dohbesp.nyc.gov/IndicatorPublic/beta/data-explorer/cancer/" on 10/31/2022.

- Datasets for 621:
    - The dataset used in this study containing information collected at the Cleveland Clinic in 1988 is publicly available from the UCI Machine Learning Repository, Center for Machine Learning and Intelligent Systems (Dua & Graff, 2019).
- Dataset for 622:
    - CoronaHack -Chest X-Ray-Dataset on Kaggle. https://www.kaggle.com/datasets/praveengovi/coronahack-chest-xraydataset
- Datasets for 623:
    - Mental Illness during the Pandemic | Public Health Infobase - Public Health Agency of Canada. https://health-infobase.canada.ca/covid-19/mental-health-survey/data-tables.html. Accessed 19 Feb. 2023.
    - Canada, Public Health Agency of. “Map of Canadian Mental Health during the COVID-19 Pandemic.” Aem, 20 June 2022, https://health-infobase.canada.ca/covid-19/mental-health/.
    - IST dataset: https://datashare.ed.ac.uk/handle/10283/3406
