import os 
import sys


import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from logger import logger


def analyze_data(df):
    
    #  grouping the sum of credits by country 
    credits_by_country = df.groupby('Country')['Credits Issued'].sum().reset_index()
    # grouping the sum of credits by project type 
    credits_by_project_type = df.groupby('Project Type')['Credits Issued'].sum().reset_index()  

    # grouping the sum of credits by year
    credits_by_year = df.groupby('Vintage')['Credits Issued'].sum().reset_index()

    
    #removing the extreme highest value from the data
    max_threshold = df['Credits Issued'].quantile(0.9999)
    filtered_df = df[df['Credits Issued'] <= max_threshold]

    #removing all the zero values
    filtered_df = filtered_df[filtered_df['Credits Issued'] > 0]
    
    #taking the maximum and minimum credits issued of new data
    highest_credit_project = filtered_df.loc[filtered_df['Credits Issued'].idxmax()]
    lowest_credit_project = filtered_df.loc[filtered_df['Credits Issued'].idxmin()]

    return credits_by_country, credits_by_project_type, credits_by_year, highest_credit_project, lowest_credit_project

