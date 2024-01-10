# 601 Project - Working with Data and Visualization - "Analysis of Calgary’s Historical Air Quality Data"
The project is a detailed study examining air quality changes over 39 years in Calgary due to anthropogenic factors, particularly greenhouse gas emissions. It leverages data from Alberta Environment and Parks and the World Health Organization to compare local and global trends. Here are the key points for a summary:

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


# 602 Project - Statistical Data Analysis
### Focus of statistical investigation
The focus of our statistical investigation is to understand if there is any statistical difference between the particulate matter recorded in Calgary vs particulate matter recorded globally in order to gain evidence to support or reject our hypothesis that PM2.5 globally is equal to PM2.5 in Calgary. We also want to determine how greenhouse gas emissions changed over the years in Calgary by plotting the distribution of greenhouse gas emissions over the years and estimating the population average via bootstrapping. This data is leveraged by the Government of Alberta to visualize, analyze and continually monitor air pollution. This enables Calgary residents to protect themselves and take the necessary precautions especially those who are health compromised. 

# 603 Project - Statistical Modelling with Data
In our research for this project, we discovered that many different factors contribute to an individual’s success in terms of their education. The goal of this project is to explore these factors, and analyze how each factor negatively, or positively impacts an individual’s success in the education system in order to be able to make informed decisions on the overall quality of education these students are receiving, as well as predict school achievement success.

# 604 Project - Working with Data at Scale
For our project, we will be examining the relationships between air quality and neighbourhood poverty, and seeing what effect this has on cancer rates and incidents of asthma in New York City. In our research for this project, we discovered that lung cancer is strongly correlated to air pollution, and chose to investigate that along with 3 other types of cancer that we think will also be affected and that we found interesting. The cancers that we will be investigating are: Lung cancer, Larynx cancer, Esophageal cancer, and Non-Hodgkins Lymphoma.

For our project, we will be asking 4 guiding questions:
- By looking at different areas of New York City, can we conclude in general a poor neighbourhood has higher cancer rate and worse air quality?
- Which pollutants have the highest correlations with which cancers?
- Does poor air quality increase the prevalence of asthma in adults? Does the borough in NYC affect this? Which pollutants has the greatest effect on asthma incidents?
- Do the poorest neighbourhoods have the highest incidents of asthma among adults?

## Dataset
- The dataset we have chosen for 601 and 602 project is “Historical Air Quality”  which was collected by the Calgary Region Airshed Zone and submitted to Alberta Environment and Parks (AEP). This information is publicly available and can be used from the City of Calgary’s Open Data Portal. City of Calgary’s Open Data Portal Historical Air Quality [online]. Available at: https://data.calgary.ca/Environment/Historical-Air-Quality/uqjm-jxgp/data
- WHO Air Quality Database. WHO Air Quality Database (Update 2022), Available at: https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database
- The datasets we have chosen for 604 through different databases that were collected and published by the American Community Survey, which are publicly available on the New York City Department of Health Environment and Health Data Portal from the New York City government website.
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
- The datasets we have chosen for 603 is from The North Carolina Department of Public Instruction. School Report Card Resources for Researchers. Accessed at " https://www.dpi.nc.gov/data-reports/school-report-cards/school-report-card-resources-researchers" on 11/15/2022.
