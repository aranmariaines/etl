"""
This script contains all the functions needed to run the electric_companies_data_scraper.py

"""

# Libraries
import urllib
import pandas as pd
import js2py
import sqlalchemy
from importlib import reload


def download_data_from_url(company,output_javascript_file):
    """
    Retrieve data from javascript file
    
    Parameters
    ----------
    company: str
        the name of electric company. Currently it supports the ones listed here: 
        https://www.argentina.gob.ar/enre/estado-de-la-red-electrica-en-el-area-metropolitana-de-buenos-aires
        
    Returns
    ------
    file: javaascript file
        javascript file downloaded from url
    
    """
    
    # Define URL path for each electric company
    if company == 'edenor':
        url = 'http://www.enre.gov.ar/paginacorte/js/data_EDN.js?'
    elif company == 'edesur':
        url = 'http://www.enre.gov.ar/paginacorte/js/data_EDS.js?'
    else:
        'error'
        
    #Retrieve URL and save into a js file
    urllib.request.urlretrieve(url,output_javascript_file)
    
    return output_javascript_file
    
def transform_js_to_py(input_javascript_file, output_python_file):
    """
    Recieve a javascript file as input and transform it into python code
    
    Parameters
    ---------
    input_file : string
        name of javascript file with code to convert
    python_file: string
        name of python output file
        
    Returns
    ------
    file 
        A python file converted from javascript file
    """
    
    js2py.translate_file(input_javascript_file, output_python_file)
    
    return output_python_file


def generate_tables(company):
    """
    Structure data from python file into data frames
    
    Parameters
    ---------
    company: string
        the name of electric company. 
    
    Returns
    ------
    Dataframes
        Data frames for each subject of interest
    """
    
    # Import transformed file
    import company
    reload(company)
    from company import company

    
    data = company.data
    
    # Build Dataframes from tables
    cortescomunicados = pd.DataFrame.from_dict(data['cortesComunicados'])
    cortespreventivos = pd.DataFrame.from_dict(data['cortesPreventivos'])
    cortesprogramados = pd.DataFrame.from_dict(data['cortesProgramados'])
    cortesserviciobaja = pd.DataFrame.from_dict(data['cortesServicioBaja'])
    cortesserviciomedia = pd.DataFrame.from_dict(data['cortesServicioMedia'])
    
    # Name Dataframes
    cortescomunicados.name = 'cortescomunicados'
    cortespreventivos.name = 'cortespreventivos'
    cortesprogramados.name = 'cortesprogramados'
    cortesserviciobaja.name = 'cortesserviciobaja'
    cortesserviciomedia.name = 'cortesserviciomedia'    
    
    # Get Misc    
    general = pd.DataFrame({'empresa': data['empresa'],
                         'fuente': data['fuente'],
                         'totalUsuariosAyer': data['totalUsuariosAyer'],
                         'totalUsuariosConSuministro' : data['totalUsuariosConSuministro'],
                         'totalUsuariosSinSuministro' : data['totalUsuariosSinSuministro'],
                         'ultimaActualizacion' : data['ultimaActualizacion']},
                         index = [0])
    general.name = 'general'
    
    return (cortescomunicados,cortespreventivos,cortesprogramados,cortesserviciobaja,cortesserviciomedia, general);
    

def generate_ids(table, datetimenow):
    """
    Adds a column to a dataframe
    
    Parameters
    ---------
    table : dataframe
        dataframe to add the column
    datetimenow: string
        datetimenow contains date and time
        
    """
    
    table['created_on'] = datetimenow
    

def add_companpy_column(table,company):
    """
    Adds a column to a dataframe
    
    Parameters
    ---------
    table : dataframe
        dataframe to add the column
    company: string
        name of electric company
    """
    
    table['company'] = company
    

def connect_to_database(user,password,host,database_name):
    """
    Connect to PostgreSQL using credentials from a hidden file
    
    Parameters
    ---------
    user: string
        Database user
    password: string
        Password to access the Postgres database
    host: int
        host number
    database_name: string
        name of database/schema to uplaod data
        
    Returns
    ------
    Connection
        An engine for connection
    
    """
    
    # Connect to database
    db_string = f"postgres://{user}:{password}@{host}/{database_name}" 
    engine = sqlalchemy.create_engine(db_string)
    
    return engine


def insert_into_database(table, engine):
    """
    Get dataframe and insert or append it to a table in database
    
    Parameters
    ---------
    table: data frame
        dataframe to upload
    engine: connection enginne
        engine that contains the connection to database
    """
    
    table.to_sql(name = table.name, con=engine, if_exists = 'append', index = False)
    
    return
    

    


    
    
        
    