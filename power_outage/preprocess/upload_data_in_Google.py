# Libraries
import os
from pathlib import Path
path = os.path.join(Path.home(),'Documents','github','etl','power_outage')
os.chdir(path)
import pandas as pd


# Connect with Google Sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# From dataframe to Google sheets
from df2gspread import df2gspread as d2g

# Dataframe
agg_date = pd.read_csv('datatoGoogle/agg_date.csv')


# Configuration setup
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Read Json with credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('preprocess/clave.json',scope)

# Authorize
gc = gspread.authorize(credentials)

# Id of spreadsheet
spreadsheet_key = '1zNuQFkPacDfFVYIHN9DxnP9uYfOR4_yK9ZRhrCy8U6g'

# Upload
worksheet_name = 'Sheet1'
cell_of_start = 'A1'
d2g.upload(agg_date,
           spreadsheet_key,
           worksheet_name,
           credentials = credentials,
           col_names = True,
           row_names = False,
           start_cell = cell_of_start,
           clean = False)
           
print ('GoogleSheet Updated') 

