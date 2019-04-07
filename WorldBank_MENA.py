#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:16:02 2018

@author: Gsond001
"""

import pandas as pd # data science essentials (read_excel, DataFrame)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns
import numpy as np


file = 'world_data.xlsx'
world = pd.read_excel(file)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

##need to extract from world data

mena= world.iloc[73:94,:]

mena.to_excel('world_4.xlsx')
mena = pd.read_excel('world_4.xlsx')

mena.describe()

# Checking for missing values

print(
      mena.isnull()
      .any()
      )

# Yes, there are missing values. Let's get a closer look

# In absolute numbers
print(
      mena[:]
      .isnull()
      .sum()
      )

# As a percentage of total observations (take note of the parenthesis)
print(
      ((world[:].isnull().sum())
      /
      world[:]
      .count())
      .round(2)
)

#Flagging missing Data
      
for col in mena:
    if mena[col].isnull().astype(int).sum() > 0:
       mena['m_'+col] = mena[col].isnull().astype(int)
       print(col)



#Creating new columns for income category 
mena['income_cat'] = pd.DataFrame.copy(mena['income_group'])
mena['income_cat'] = mena['income_cat'].replace(['High income' , 'Upper middle income' , 'Lower middle income', 'Low income'], [3,2,1,1])
print(mena.shape)

#####################        

#REMOVE SYRIA#
mena= mena.drop(89, 0)
print(mena.shape)


####################

#subsets by income category

mena3= mena[mena.income_cat == 3]
mena2 = mena[mena.income_cat == 2]
mena1 = mena[mena.income_cat == 1]

print(mena3)
print(mena2)
print(mena1)

print(mena3.shape)
print(mena2.shape)
print(mena1.shape)

######################
#Median Imputation


median1 = pd.DataFrame.copy(mena1)
median2=pd.DataFrame.copy(mena2)
median3=pd.DataFrame.copy(mena3)

for col in mena1:
    if median1[col].isnull().astype(int).sum() > 0:
        col_median = median1[col].median()
        median1[col] = median1[col].fillna(col_median).round(3)

for col in mena2:
    if median2[col].isnull().astype(int).sum() > 0:
        col_median = median2[col].median()
        median2[col] = median2[col].fillna(col_median).round(3)
        
        
for col in mena3:
    if median3[col].isnull().astype(int).sum() > 0:
        col_median = median3[col].median()
        median3[col] = median3[col].fillna(col_median).round(3)
        
        



fmena=pd.concat([median1,median2,median3])

#Checking for missing values
print(median1.isnull().any().any())
print(median2.isnull().any().any())
print(median3.isnull().any().any())

#HISTOGRAM

for col in fmena:
    plt.hist(fmena[col],bins='fd')
    plt.title(col)
    plt.show()




###############################################################################
# Saving things for future use
###############################################################################

# saving dataset
fmena.to_excel('mena_imputed.xlsx', index = False)





file ='mena_imputed.xlsx'
imena = pd.read_excel(file)



###############################################################################
# Outlier detection using quantile techniques
###############################################################################

# Using describe() for distribution analysis 
imena.describe()




###############################################################################
# Outlier detection using boxplots
###############################################################################

# Using boxplots for distribution analysis


for col in imena:
        imena.boxplot(column=['gdp_usd'], by =[col],vert= True, patch_artist =True, meanline = True,showmeans= True)
        plt.suptitle('')
        plt.tight_layout()
        plt.show()




####################################################
#Boxplots Per Country
####################################################

imena.boxplot(column = ['gdp_usd'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['access_to_electricity_pop'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['access_to_electricity_rural'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['access_to_electricity_urban'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['CO2_emissions_per_capita)'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['compulsory_edu_yrs'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_female_employment'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_male_employment'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_agriculture_employment'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_industry_employment'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_services_employment'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['exports_pct_gdp'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['fdi_pct_gdp'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['gdp_usd'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['gdp_growth_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['incidence_hiv'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['internet_usage_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()



imena.boxplot(column = ['homicides_per_100k'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['adult_literacy_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['child_mortality_per_1k'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['avg_air_pollution'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['women_in_parliament'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['tax_revenue_pct_gdp'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['unemployment_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['urban_population_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()



imena.boxplot(column = ['urban_population_growth_pct'], by= ['country_name'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()




######################################
#Boxplots per Income Group
#####################################
imena.boxplot(column = ['gdp_usd'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['gdp_usd'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['access_to_electricity_pop'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['access_to_electricity_rural'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['access_to_electricity_urban'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['CO2_emissions_per_capita)'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['compulsory_edu_yrs'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_female_employment'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_male_employment'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_agriculture_employment'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_industry_employment'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['pct_services_employment'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['exports_pct_gdp'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['fdi_pct_gdp'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['gdp_usd'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['gdp_growth_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['incidence_hiv'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['internet_usage_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()



imena.boxplot(column = ['homicides_per_100k'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['adult_literacy_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['child_mortality_per_1k'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['avg_air_pollution'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['women_in_parliament'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()

imena.boxplot(column = ['tax_revenue_pct_gdp'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['unemployment_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()


imena.boxplot(column = ['urban_population_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()



imena.boxplot(column = ['urban_population_growth_pct'], by= ['income_cat'],
                                    vert=False, 
                                    patch_artist = True,
                                    meanline = True, 
                                    showmeans = True)
plt.suptitle('')
plt.tight_layout()
plt.show()





###############################################################################
# Outlier Thresholds
###############################################################################


access_to_electricity_pop_limit_low= 80

access_to_electricity_rural_limit_low= 80

access_to_electricity_urban_limit_low= 80

CO2_emissions_per_capita_limit_hi= 20

pct_female_employment_limit_hi= 35
pct_female_employment_limit_low = 10

pct_male_employment_limit_hi= 10
pct_male_employment_limit_low= 2

pct_agriculture_employment_limit_hi= 30
pct_agriculture_employment_limit_low= 5

pct_industry_employment_limit_hi= 45
pct_industry_employment_limit_low= 20


pct_services_employment_limit_hi= 80
pct_services_employment_limit_low=40



exports_pct_gdp_limit_hi=100
exports_pct_gdp_limit_low = 20

fdi_pct_gdp_limit_hi= 6
fdi_pct_gdp_limit_low = 0 

gdp_usd_limit_hi= 5
gdp_usd_limit_low= 1


gdp_growth_pct_limit_hi=5
gdp_growth_pct_limit_low=0 


incidence_hiv_limit_hi= .05
incidence_hiv_limit_low = 0

internet_usage_pct_limit_hi= 90
internet_usage_pct_limit_low= 20


homicides_per_100k_limit_hi= 3
homicides_per_100k_limit_low = 1


adult_literacy_pct_limit_hi = 90
adult_literacy_pct_limit_low=85



child_mortality_per_1k_limit_hi=50
child_mortality_per_1k_limit_low= 10


avg_air_pollution_limit_hi=100
avg_air_pollution_limit_low = 20


women_in_parliament_limit_hi= 30
women_in_parliament_limit_low = 5

tax_revenue_pct_gdp_limit_hi= 20
tax_revenue_pct_gdp_limit_low = 5 

unemployment_pct_limit_hi= 5

urban_population_pct_limit_hi = 90
urban_population_pct_limit_low= 50


urban_population_growth_pct_limit_hi= 5
urban_population_growth_pct_limit_low = 2


###############################################################################
# Flagging outliers
###############################################################################
imena['electricity_pop_low'] = 0

for val in enumerate(imena.loc[ : , : 'access_to_electricity_pop']): 
    if val[1] < 'access_to_electricity_pop_limit_low':
        imena.loc[val[0], 'electricity_pop_low'] = 1


imena['electricity_rural_low'] = 0

for val in enumerate(imena.loc[ : , : 'access_to_electricity_rural']):
    if val[1] < 'access_to_electricity_rural_limit_low':
       imena.loc[val[0], 'electricity_rural_low'] = 1


imena['electricity_urban_low'] = 0
for val in enumerate(imena.loc[ : , : 'access_to_electricity_urban']):
    if val[1] < 'access_to_electricity_urban_limit_low':
        mena.loc[val[0], 'electricity_urban_low'] = 1

imena['CO2_emissions'] = 0
for val in enumerate(imena.loc[ : , : 'CO2_emissions_per_capita)']):
    if val[1] > 'CO2_emissions_per_capita_limit_hi':
       imena.loc[val[0], 'CO2_emissions'] = 1

imena['female_employment'] = 0
for val in enumerate(imena.loc[ : , 'pct_female_employment']):
    if val[1] > pct_female_employment_limit_hi:
       imena.loc[val[0], 'female_employment'] = 1
for val in enumerate(imena.loc[ : , 'pct_female_employment']):
    if val[1] < pct_female_employment_limit_low:
        imena.loc[val[0], 'female_employment'] = 1


imena['male_employment'] = 0
for val in enumerate(imena.loc[ : , 'pct_male_employment']):
    if val[1] < pct_male_employment_limit_low:
        imena.loc[val[0], 'male_employment'] = 1
for val in enumerate(imena.loc[ : , 'pct_male_employment']):
    if val[1] > pct_male_employment_limit_hi:
        imena.loc[val[0], 'male_employment'] = 1

imena['agriculture_employment'] = 0
for val in enumerate(imena.loc[ : , 'pct_agriculture_employment']):
    if val[1] < pct_agriculture_employment_limit_low:
        imena.loc[val[0], 'agriculture_employment'] = 1
for val in enumerate(imena.loc[ : , 'pct_agriculture_employment']):
    if val[1] > pct_agriculture_employment_limit_hi:
        imena.loc[val[0], 'agriculture_employment'] = 1

imena['industry_employment'] = 0
for val in enumerate(imena.loc[ : , 'pct_industry_employment']):
    if val[1] < pct_industry_employment_limit_low:
        imena.loc[val[0], 'agriculture_employment'] = 1
for val in enumerate(imena.loc[ : , 'pct_industry_employment']):
    if val[1] > pct_industry_employment_limit_hi:
        imena.loc[val[0], 'industry_employment'] = 1

imena['services_employment'] = 0
for val in enumerate(imena.loc[ : , 'pct_services_employment']):
    if val[1] < pct_services_employment_limit_low:
        imena.loc[val[0], 'agriculture_employment'] = 1
for val in enumerate(imena.loc[ : , 'pct_services_employment']):
    if val[1] > pct_services_employment_limit_hi:
        imena.loc[val[0], 'services_employment'] = 1

imena['exports'] = 0
for val in enumerate(imena.loc[ : , 'exports_pct_gdp']):
    if val[1] < exports_pct_gdp_limit_low:
        imena.loc[val[0], 'exports'] = 1
for val in enumerate(imena.loc[ : , 'exports_pct_gdp' ]):
    if val[1] > exports_pct_gdp_limit_hi:
        imena.loc[val[0], 'exports'] = 1

imena['fdi'] = 0
for val in enumerate(imena.loc[ : , 'fdi_pct_gdp']):
    if val[1] < fdi_pct_gdp_limit_low:
        imena.loc[val[0], 'fdi'] = 1
for val in enumerate(imena.loc[ : , 'fdi_pct_gdp']):
    if val[1] > fdi_pct_gdp_limit_hi:
        imena.loc[val[0], 'fdi'] = 1

imena['gdp_usd'] = 0
for val in enumerate(imena.loc[ : , 'gdp_usd']):
    if val[1] < gdp_usd_limit_low:
        imena.loc[val[0], 'gdp'] = 1
for val in enumerate(imena.loc[ : , 'gdp_usd']):
    if val[1] > gdp_usd_limit_hi:
        imena.loc[val[0], 'gdp'] = 1
        
imena['gdp_growth'] = 0
for val in enumerate(imena.loc[ : , 'gdp_growth_pct']):
    if val[1] < gdp_growth_pct_limit_low:
        imena.loc[val[0], 'gdp_growth'] = 1
for val in enumerate(imena.loc[ : , 'gdp_growth_pct']):
    if val[1] > gdp_growth_pct_limit_hi:
        imena.loc[val[0], 'gdp_growth'] = 1


imena['hiv'] = 0
for val in enumerate(imena.loc[ : , 'incidence_hiv']):
    if val[1] < incidence_hiv_limit_low:
        imena.loc[val[0], 'hiv'] = 1
for val in enumerate(imena.loc[ : , 'incidence_hiv']):
    if val[1] > incidence_hiv_limit_hi:
        imena.loc[val[0], 'hiv'] = 1

imena['internet_usage'] = 0
for val in enumerate(imena.loc[ : , 'internet_usage_pct']):
    if val[1] < internet_usage_pct_limit_low:
        imena.loc[val[0], 'internet_usage'] = 1
for val in enumerate(imena.loc[ : , 'internet_usage_pct']):
    if val[1] > internet_usage_pct_limit_hi:
        imena.loc[val[0], 'internet_usage'] = 1


imena['homicides'] = 0
for val in enumerate(imena.loc[ : , 'homicides_per_100k']):
    if val[1] < homicides_per_100k_limit_low:
        imena.loc[val[0], 'homicides'] = 1
for val in enumerate(imena.loc[ : , 'homicides_per_100k']):
    if val[1] > homicides_per_100k_limit_hi:
        imena.loc[val[0], 'homicides'] = 1

imena['adult'] = 0
for val in enumerate(imena.loc[ : , 'adult_literacy_pct']):
    if val[1] < adult_literacy_pct_limit_low:
        imena.loc[val[0], 'adult'] = 1
for val in enumerate(imena.loc[ : , 'adult_literacy_pct']):
    if val[1] > adult_literacy_pct_limit_hi:
        imena.loc[val[0], 'adult'] = 1


imena['child'] = 0
for val in enumerate(imena.loc[ : , 'child_mortality_per_1k']):
    if val[1] < child_mortality_per_1k_limit_low:
        imena.loc[val[0], 'child'] = 1
for val in enumerate(imena.loc[ : , 'child_mortality_per_1k']):
    if val[1] > child_mortality_per_1k_limit_hi:
        imena.loc[val[0], 'child'] = 1


imena['air'] = 0
for val in enumerate(imena.loc[ : , 'avg_air_pollution']):
    if val[1] < avg_air_pollution_limit_low:
        imena.loc[val[0], 'air'] = 1
for val in enumerate(imena.loc[ : , 'avg_air_pollution']):
    if val[1] > avg_air_pollution_limit_hi:
        imena.loc[val[0], 'air'] = 1


imena['women'] = 0
for val in enumerate(imena.loc[ : , 'women_in_parliament']):
    if val[1] < women_in_parliament_limit_low:
        imena.loc[val[0], 'women'] = 1
for val in enumerate(imena.loc[ : , 'women_in_parliament']):
    if val[1] > women_in_parliament_limit_hi:
        imena.loc[val[0], 'women'] = 1

imena['tax'] = 0
for val in enumerate(imena.loc[ : , 'tax_revenue_pct_gdp']):  
    if val[1] < tax_revenue_pct_gdp_limit_low:
        imena.loc[val[0], 'tax'] = 1
for val in enumerate(imena.loc[ : , 'tax_revenue_pct_gdp']):
    if val[1] > tax_revenue_pct_gdp_limit_hi:
        imena.loc[val[0], 'tax'] = 1

imena['unemployment'] = 0
for val in enumerate(imena.loc[ : , 'unemployment_pct']):
    if val[1] > unemployment_pct_limit_hi:
        imena.loc[val[0], 'unemployment'] = 1

imena['urban_population'] = 0
for val in enumerate(imena.loc[ : , 'urban_population_pct']):
    if val[1] < urban_population_pct_limit_low:
        imena.loc[val[0], 'urban_population'] = 1
for val in enumerate(imena.loc[ : , 'urban_population_pct']):
    if val[1] > urban_population_pct_limit_hi:
        imena.loc[val[0], 'urban_population'] = 1

imena['urban_population_growth'] = 0
for val in enumerate(imena.loc[ : , 'urban_population_growth_pct']):
    if val[1] < urban_population_growth_pct_limit_low:
        imena.loc[val[0], 'urban_population_growth'] = 1
for val in enumerate(imena.loc[ : , 'urban_population_growth_pct']):
    if val[1] > urban_population_growth_pct_limit_hi:
        imena.loc[val[0], 'urban_population_growth'] = 1


########################
# Analyzing outlier flags
########################

imena['out_sum'] = (imena['electricity_pop_low']+
     imena['electricity_rural_low']+
     imena['CO2_emissions']+
     imena['female_employment']+
     imena['male_employment']+
     imena['agriculture_employment']+
     imena['industry_employment']+
     imena['services_employment']+
     imena['exports']+
     imena['fdi']+
     imena['gdp_usd']+
     imena['gdp_growth']+
     imena['hiv']+
     imena['internet_usage']+
     imena['homicides']+
     imena['adult']+
     imena['child']+
     imena['air']+
     imena['women']+
     imena['tax']+
     imena['unemployment']+
     imena['urban_population']+
     imena['urban_population_growth'])



check = (imena.loc[ : , ['country_name',
                         'out_sum',
                            'electricity_pop_low',
                            'electricity_rural_low',
                            'CO2_emissions',
                            'female_employment',
                            'male_employment',
                            'agriculture_employment',
                            'industry_employment',
                            'services_employment',
                            'exports',
                            'fdi',
                            'gdp_usd',
                            'gdp_growth',
                            'hiv',
                            'internet_usage',
                            'homicides',
                            'adult',
                            'child',
                            'air',
                            'women',
                            'tax',
                            'unemployment',
                            'urban_population',
                            'urban_population_growth']].sort_values(['out_sum'],
                                          ascending = False))






###############################################################################
# Saving things for future use
###############################################################################

imena.to_excel('mena_flagged.xlsx', index = False)




file = 'mena_flagged.xlsx'
cmena = pd.read_excel(file)

df_corr = cmena.corr().round(3)
print(df_corr)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


## Correlation matrix

df_corr.to_excel("mena_corr_matrix.xlsx")

cmena_corr_all = cmena.corr().round(2)
print(cmena_corr_all)
cmena_corr_all.to_excel("cmena_corr_all_matrix.xlsx")


cmena_3 = cmena[cmena.income_cat == 3]
cmena_2 = cmena[cmena.income_cat == 2]
cmena_1 = cmena[cmena.income_cat == 1]

cmena_3 = cmena_3.corr().round(2)
cmena_2 = cmena_2.corr().round(2)
cmena_1 = cmena_1.corr().round(2)


print(cmena_3)
print(cmena_2)
print(cmena_1)

cmena_3.to_excel("cmena_3_corr_matrix.xlsx")
cmena_2.to_excel("cmena_2_corr_matrix.xlsx")
cmena_1.to_excel("cmena_1_corr_matrix.xlsx")



## Extract top correleations

file = 'cmena_3_corr_matrix.xlsx'
cmena_3_corr = pd.read_excel(file)



cmena_3_corr = cmena_3.corr().abs()

sol = (cmena_3_corr.where(np.triu(np.ones(cmena_3_corr.shape), k=1).astype(np.bool))
                 .stack()
                 .sort_values(ascending=False))
print(sol.round(2).head(30))


file = 'cmena_2_corr_matrix.xlsx'
cmena_2_corr = pd.read_excel(file)



cmena_2_corr = cmena_2.corr().abs()

sol = (cmena_2_corr.where(np.triu(np.ones(cmena_2_corr.shape), k=1).astype(np.bool))
                 .stack()
                 .sort_values(ascending=False))
print(sol.round(2).head(30))


file = 'cmena_1_corr_matrix.xlsx'
cmena_3_corr = pd.read_excel(file)



cmena_1_corr = cmena_1.corr().abs()

sol = (cmena_1_corr.where(np.triu(np.ones(cmena_1_corr.shape), k=1).astype(np.bool))
                 .stack()
                 .sort_values(ascending=False))
print(sol.round(2).head(30))


##########


## Correlation Heatmap

sns.heatmap(df_corr,
            cmap = 'Blues',
            square = True,
            annot = False,
            linecolor = 'black',
            linewidths = 0.5)

##Subsetting by income groups

cmena[cmena.income_group == 'High income']      


 
##Scatterplots for all variables    
    
plt.scatter(x = 'pct_female_employment',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('Female Employment')
plt.ylabel('Country')
plt.grid(True)
plt.show()    

plt.scatter(x = 'access_to_electricity_pop',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('Access to Electricity Pop')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'CO2_emissions_per_capita)',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('CO2_emissions_per_capita')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'compulsory_edu_yrs',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('compulsory_edu_yrs')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'pct_male_employment',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('pct_male_employment')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'pct_agriculture_employment',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('pct_agriculture_employment')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'pct_industry_employment',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('pct_industry_employment')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'pct_services_employment',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('pct_services_employment')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'exports_pct_gdp',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('exports_pct_gdp')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'fdi_pct_gdp',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('fdi_pct_gdp')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'gdp_growth_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('gdp_growth_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'incidence_hiv',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('incidence_hiv')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'internet_usage_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('internet_usage_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'adult_literacy_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('adult_literacy_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'child_mortality_per_1k',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('child_mortality_per_1k')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'avg_air_pollution',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('avg_air_pollution')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'women_in_parliament',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('women_in_parliament')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'tax_revenue_pct_gdp',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('tax_revenue_pct_gdp')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'unemployment_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('unemployment_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'urban_population_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('urban_population_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()

plt.scatter(x = 'urban_population_growth_pct',
            y = 'country_name',
            alpha = 0.7,
            cmap = 'bwr',
            data = cmena)


plt.xlabel('urban_population_growth_pct')
plt.ylabel('Country')
plt.grid(True)
plt.show()


##############
#lmplot



sns.lmplot(x = 'unemployment_pct',
           y = 'gdp_usd',
           data = mena3,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Exports")
plt.grid()
plt.tight_layout()
plt.show()


sns.lmplot(x = 'unemployment_pct',
           y = 'gdp_usd',
           data = mena2,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')
plt.title("Exports")
plt.grid()
plt.tight_layout()
plt.show()

sns.lmplot(x = 'unemployment_pct',
           y = 'gdp_usd',
           data = mena1,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')
plt.title("Exports")
plt.grid()
plt.tight_layout()
plt.show()

######Correlations between High Income#######
sns.lmplot(x = 'exports_pct_gdp',
           y = 'gdp_growth_pct',
           data = mena3,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')
plt.title("Exports")
plt.grid()
plt.tight_layout()
plt.savefig('Exports per GDP Growth.png')
plt.show()




sns.lmplot(x = 'pct_industry_employment',
           y = 'CO2_emissions_per_capita)',
           data = mena3,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("CO2 Emissions")
plt.grid()
plt.tight_layout()
plt.savefig('Industry per CO2.png')
plt.show()




######Correlations between Middle Income#######
sns.lmplot(x = 'unemployment_pct',
           y = 'gdp_growth_pct',
           data = mena2,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Unemployment")
plt.grid()
plt.tight_layout()
plt.savefig('Unemployment per GDP Growth.png')
plt.show()




sns.lmplot(x = 'gdp_usd',
           y = 'urban_population_pct',
           data = mena2,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Urban Population")
plt.grid()
plt.tight_layout()
plt.savefig('Unemployment per GDP Growth.png')
plt.show()




######Correlations between Lower Income#######

sns.lmplot(x = 'gdp_growth_pct',
           y = 'fdi_pct_gdp',
           data = mena1,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("FDI")
plt.grid()
plt.tight_layout()
plt.savefig('FDI per GDP Growth.png')
plt.show()



sns.lmplot(x = 'gdp_usd',
           y = 'CO2_emissions_per_capita)',
           data = mena1,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("CO2 Emissions per GDP")
plt.grid()
plt.tight_layout()
plt.savefig('CO2 per GDP.png')
plt.show()




sns.lmplot(x = 'unemployment_pct',
           y = 'pct_agriculture_employment',
           data = mena1,
           fit_reg = False,
           hue= 'country_name',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma')

plt.title("Unemployment per agriculture")
plt.grid()
plt.tight_layout()
plt.savefig('Unemployment per agriculture.png')
plt.show()



