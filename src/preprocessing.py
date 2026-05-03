import pandas as pd
from data_loading import LoadCsv


def clean_daily_data(df):
    """Clean the raw dataframe of Air Quality
        - convert to correct data format
        - engineer new features (month,year, seasons)
        - convert values to numbers
        -handle missing values and outliers
    """
    
    #rename Columns to simplify



    df = df.rename(columns = renamed_columns)





    #convert date column to proper datetime
    df['date'] = pd.to_datetime(df['date'], format = '%y-%m-%d')

    #create month and yer columns
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year


    #Convert Measurements to Numbers
    malin_head_column = ['aqi', 'pm25','pm10', 'no2', 'so2',
                         'co', 'o3', 'temperature', 'humidity', 'wind_speed']

    #coerce bad values to NAN
    for col in malin_head_column:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = 'coerce')

    #create a mean temp column- average of max and min

    
    print(f" Data ranges between: {df['date'].min()} to {df['date'].max()} \n")
    print(f"Total rows: {len(df)} \n")
    

    return df



