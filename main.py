import sys 
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from scripts.data_download import download_and_extract_zip
from scripts.data_processing import clean_verra_data, clean_gold_data, merge_data
from scripts.data_analysis import analyze_data
from scripts.data_visualization import visualize_data
from logger import logger

def main():
    # url of api that returns a zip of all the resources
    url = "https://gspp.berkeley.edu/assets/uploads/page/VROD-v11-RegistryFiles.zip"
    zip_filename = "public/VROD-v11-RegistryFiles.zip"
    # using data from these two files
    target_files = [
        "VROD_v11_Registry Documents/Gold Buffer.xlsx",
        "VROD_v11_Registry Documents/Verra Projects.xlsx"
    ]
    
    #download and extract the data
    download_and_extract_zip(url, zip_filename, target_files)
    
    #clean the data
    verra_df = clean_verra_data('public/Verra Projects.xlsx')
    gold_df = clean_gold_data('public/Gold Buffer.xlsx')
    
    #merge the data
    unified_df = merge_data(verra_df, gold_df)
    logger.info("Merged datasets successfully.")
    
    #analyze the data
    credits_by_country, credits_by_project_type, credits_by_year, highest_credit_project, lowest_credit_project = analyze_data(unified_df)
    
    #visualize the data
    visualize_data(credits_by_country, credits_by_project_type, credits_by_year, highest_credit_project, lowest_credit_project,unified_df)

if __name__ == "__main__":
    main()
