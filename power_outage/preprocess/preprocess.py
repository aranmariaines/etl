# Libraries
import pandas as pd
import os
from pathlib import Path
path = os.path.join(Path.home(),'Documents','github','etl','power_outage')
os.chdir(path)


# Import data
general = pd.read_csv('data/general.csv')
#cortespreventivos = pd.read_csv('data/cortespreventivos.csv')
cortesprogramados = pd.read_csv('data/cortesprogramados.csv')
corteserviciobaja = pd.read_csv('data/cortesserviciobaja.csv')
corteserviciomedia = pd.read_csv('data/cortesserviciomedia.csv')

# Add headers
general.columns = ['Company','Webservice','Users without power','Users with power','Yesterday users without power','Update hour','Time','Company2'] 
cortesprogramados.columns = ['City','Estimated time of fix','County','Substation','Users','Time','Company']
corteserviciomedia.columns = ['City','Estimated time of fix','County','Substation','Users without power','Time','Company']
corteserviciobaja.columns = ['City','County','Users without power','Time','Company'] 

# Data type transformation
general['Time'] = pd.to_datetime(general.Time)
corteserviciobaja['Time'] = pd.to_datetime(corteserviciobaja.Time)

# County names normalization
cortesprogramados.County.replace(['CAPITAL'], ['CAPITAL FEDERAL'], inplace=True)
corteserviciomedia.County.replace(['CAPITAL'], ['CAPITAL FEDERAL'], inplace=True)
corteserviciobaja.County.replace(['CAPITAL'], ['CAPITAL FEDERAL'], inplace=True)

# Add Date
general['Date'] = general['Time'].dt.date
corteserviciobaja['Date'] = corteserviciobaja['Time'].dt.date

# Aggregate by date
agg_date = corteserviciobaja[['Date','City','County','Users without power']].groupby(['Date','City'], as_index = False).max()

# Save aggregated dataset
agg_date.to_csv('datatoGoogle/agg_date.csv', index = False)

