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
    df.isna().sum()# Checking if any nil values are present
    columns_to_select_gold = ['Project Name','Project Type', 'Country', 'Quantity', 'Vintage']# Selecting the required columns from the dataset
    df = df[columns_to_select_gold].rename(columns={'Quantity': 'Credits Issued','Project Name':'Name'}) # Renaming the column

    return df

def clean_verra_data(file_path):
    df = pd.read_excel(file_path)

    df['Estimated Annual Emission Reductions'] = pd.to_numeric(df['Estimated Annual Emission Reductions'], errors='coerce')
    df.isna().sum()
    columns_to_select_veera = ['Name', 'Project Type', 'Country/Area', 'Estimated Annual Emission Reductions']
    df = df[columns_to_select_veera].rename(columns={'Country/Area': 'Country', 'Estimated Annual Emission Reductions': 'Credits Issued'})


    return df

def merge_data(verra_df, gold_df):
    # Drop empty columns or columns with only NA values
    # verra_df = verra_df.dropna(axis=1, how='all')
    # gold_df = gold_df.dropna(axis=1, how='all')
    
    # # Define common columns
    # common_columns = [
    #     "ID", "Name", "Project Type", "Country", 
    #     "Estimated Annual Emission Reductions", 
    #     "Methodology","Project Registration Date"
    # ]
    
    # # Add columns only if they exist
    # if 'Proponent' in verra_df.columns and 'Proponent' in gold_df.columns:
    #     common_columns.append("Proponent")
    # if 'AFOLU Activities' in verra_df.columns and 'AFOLU Activities' in gold_df.columns:
    #     common_columns.append("AFOLU Activities")
    # if 'Status' in verra_df.columns and 'Status' in gold_df.columns:
    #     common_columns.append("Status")
    # if 'Region' in verra_df.columns and 'Region' in gold_df.columns:
    #     common_columns.append("Region")
    
    # # Merge datasets and keep only common columns
    # unified_df = pd.concat([verra_df, gold_df], ignore_index=True)
    # unified_df = unified_df[common_columns]
    # unified_df.to_csv('unified_dataset.csv',index=False)

    #combining the dataframes
    df_unified = pd.concat([gold_df, verra_df], ignore_index=True) 


    
    return df_unified
