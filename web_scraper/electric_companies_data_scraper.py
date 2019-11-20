"""
This script retrieves data from URLs that contain electric network failures in AMBA region in Argentina.
Then it uploads the data into a PostgreSQL.

URL with data of electrical status:
https://www.argentina.gob.ar/enre/estado-de-la-red-electrica-en-el-area-metropolitana-de-buenos-aires
"""
# Libraries
from functions import download_data_from_url,transform_js_to_py,generate_tables, generate_ids,connect_to_database,insert_into_database,add_companpy_column
import datetime
from credentials_docker import user,password,database_name,host,port
import time

# List the companies to get that
companies = ['edesur','edenor']

# Get the data from URL and import it into PostgresSQL
while True:
    for company in companies:

        # Download data from url
        download_data_from_url(company = company, output_javascript_file = 'company.js' )

        # Transform javascript file to python
        transform_js_to_py(input_javascript_file = 'company.js',output_python_file = 'company.py')

        # Build tables    
        cortescomunicados,cortespreventivos,cortesprogramados,cortesserviciobaja,cortesserviciomedia,general = generate_tables(company) 

        tables = [cortescomunicados,cortespreventivos,cortesprogramados,cortesserviciobaja,cortesserviciomedia,general]

        # Add timestamp to all tables
        print(f'Adding timestamps to tables of {company}...')
        datetimenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for table in tables:
            generate_ids(table, datetimenow)
            
        # Add company to all tables
        for table in tables:
            add_companpy_column(table, company)
            
        # Connect to database
        print('Connecting to database...')
        engine = connect_to_database(user,password,host,database_name,port)
            
        # Add data to database
        print('Adding data into database...')
        for table in tables:
            insert_into_database(table,engine)

        # Disconect from database
        print('Closing conection...')
        engine.dispose()    

    # Sleep
    print('Going to sleep...')
    time.sleep(300)
  
    