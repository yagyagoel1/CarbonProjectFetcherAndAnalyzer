import os
import sys


import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from logger import logger

def clean_gold_data(file_path):
    #reading the excel file 
    df = pd.read_excel(file_path)
    #renaming the columns so to have the same name
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')# Converting the quantity data to num,eric and the coerce is used to convert the values which  cannot be converted to numeric into nan values
    if not all(df[col].isna().sum() < 10 for col in df.columns):
        logger.warning("the number of missing values in the columns are more than 10")
    columns_to_select_gold = ['Project Name','Project Type', 'Country', 'Quantity', 'Vintage']# Selecting the required columns from the dataset
    df = df[columns_to_select_gold].rename(columns={'Quantity': 'Credits Issued','Project Name':'Name'}) # Renaming the column
    return df

def clean_verra_data(file_path):
    df = pd.read_excel(file_path)
    df['Estimated Annual Emission Reductions'] = pd.to_numeric(df['Estimated Annual Emission Reductions'], errors='coerce')
    df.isna().sum()
    columns_to_select_veera = ['Name', 'Project Type', 'Country/Area', 'Estimated Annual Emission Reductions']
    df = df[columns_to_select_veera].rename(columns={'Country/Area': 'Country', 'Estimated Annual Emission Reductions': 'Credits Issued'})
    if not all(df[col].isna().sum() < 10 for col in df.columns):
       logger.warning("the number of missing values in the columns are more than 10")
    return df

def merge_data(verra_df, gold_df):
    
    #combining the dataframes
    df_unified = pd.concat([gold_df, verra_df], ignore_index=True) 


    
    return df_unified
