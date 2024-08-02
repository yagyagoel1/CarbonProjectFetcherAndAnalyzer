import os 
import sys


import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from logger import logger

def analyze_data(df):
    
    # Calculate total credits issued by project type and country
    credits_by_country = df.groupby('Country')['Credits Issued'].sum().reset_index()
    credits_by_project_type = df.groupby('Project Type')['Credits Issued'].sum().reset_index()  # Summing credits issued by project type

    # Identifying trends in credit issuance over time
    credits_by_year = df.groupby('Vintage')['Credits Issued'].sum().reset_index()

    
    # Removing the extreme highest value
    max_threshold = df['Credits Issued'].quantile(0.9999)
    filtered_df = df[df['Credits Issued'] <= max_threshold]

    # Ensuring the lowest value is greater than zero
    filtered_df = filtered_df[filtered_df['Credits Issued'] > 0]
    
    # Finding projects with the highest and lowest credit issuance in the filtered dataset
    highest_credit_project = filtered_df.loc[filtered_df['Credits Issued'].idxmax()]
    lowest_credit_project = filtered_df.loc[filtered_df['Credits Issued'].idxmin()]

    return credits_by_country, credits_by_project_type, credits_by_year, highest_credit_project, lowest_credit_project

