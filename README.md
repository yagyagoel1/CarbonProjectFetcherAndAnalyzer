# Carbon Project Fetcher And Analyzer

## About

In this project I have integrated the backend api of [berkeley](https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database) and scraping the zip file which include mulitple data 
files we are only considering two that is By Veera and Gold buffer we are saving those two locally and only pulling again from api only when the file gets one day old  after that we sanitize the data by removing the irrelavent columns and checking 
if there are null values then we merge the datasets after doing so we analyze the data creating multiple feilds that are further used for visualization. We also use logger to log any error or disrupcencies.

## Setup

To setup the project locally follow the given steps below :

  * ```git clone https://github.com/yagyagoel1/CarbonProjectFetcherAndAnalyzer/```
  
After Cloning it locally in root dir of the project execute these commands:


  * ```python3 -m venv myenv```
  
  * ```source myenv/bin/activate```
  
  * ```pip install -r requirements.txt```
  
  * ```python main.py```

  *  **You can checkout the visualizations in public/images**



## Problem faced and the process

So I started with downloading the file by myself and trying to go through but this is a tidious process when we have to download the data again as there might me miltiple new rows added so 
to downloading this locally automatically I then tried integrating the backend api querying for their dataset which worked fine but didnt worked for acr2 and the reserve2 
as i guess those api are enabled for their own frontend domain using cors.So I tried the backend api for berkeley it was working fine and a zip file was getting downloaded which had data about all other website like that of 
verra and gold buffer so analyzed the file provided by the zip verra and buffer were the most compatible one so I took the data from
the same but the download time of the zip file was very big so I only download once a day and save the required field locally and for the whole data gets fetched from the local file and then I used the column which was similar in both to creatiing the merged data and then I did some analysis on the data where i faced a problem that some data does not have credit value which was set to 0 so toh handle the situation
I took those data which is not zero for lowest value and did the same with the highest value which felt manipulated.
Then I vizualized the data with various type of charts like stacked bar chart and bar chart for top 10 project and country line chart for trend of credit over the year.


### Thank you
