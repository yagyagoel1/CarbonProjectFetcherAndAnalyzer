import os
import sys


import requests
import zipfile
import time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from logger import logger


def is_file_older(file_path):
    #check if the file exists 
    if os.path.exists(file_path):
        #calculate the file age if it is more than 1 send true
        file_age_in_seconds = time.time() - os.path.getmtime(file_path)
        file_age_in_days = file_age_in_seconds / (24 * 60*60)
        return file_age_in_days > 1
    return True

def download_and_extract_zip(url, zip_filename, target_files):
    output_filename= "public/"
    need_to_download= False

    #iterating over both the files 
    for target_file in target_files:
        output_filedir = os.path.join(output_filename, os.path.basename(target_file))
        if is_file_older(output_filedir):
            need_to_download = True #if the file is more than 1 day setting download to true
            break

    #hitting the url to get the zip file that has the file 
    if need_to_download:
        response = requests.get(url) 
        if response.status_code == 200:#if the req is successful then save the zip file 
            with open(zip_filename, "wb") as file:
                file.write(response.content)
            logger.info("Zip file downloaded successfully.")
        
            with zipfile.ZipFile(zip_filename, 'r') as z:
                all_files = z.namelist()#saving the path for all the files
                logger.info("All files in the zip: %s", all_files)

                #checking if the target file exist in all the paths
                for target_file in target_files:
                    if target_file in all_files:
                        output_filename+= target_file.split('/')[-1]
                        #saving the files locally in data file 
                        with open(output_filename, 'wb') as f:
                            f.write(z.read(target_file))
                        logger.info("Extracted and saved: %s", output_filename)
                        output_filename="public/"
                    else:
                        logger.warning("File not found in the zip archive: %s", target_file)
                
                #removing the zip file when every think is successful
                os.remove(zip_filename)
            logger.info("Zip file deleted successfully.")
        else:
            logger.error("Failed to download file. Status code: %d", response.status_code)
    else:
        logger.info("Files are up-to-date, no need to download the zip file again.")