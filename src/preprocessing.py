import pandas as pd
from data_loading import LoadCsv

def clean_data(raw_df):
    """Clean the raw dataframe of Air Quality
        - convert to correct data format
        - engineer new features (month,year)
        - convert values to numbers
        -handle missing values and outliers
    """
    
    #rename Columns to simplify

    renamed_columns = {
        
    'Date': 'date',
    'City': 'city',
    'Country': 'country',
    'AQI': 'aqi',
    'PM2.5 (µg/m³)': 'pm25',
    'PM10 (µg/m³)': 'pm10',
    'NO2 (ppb)': 'no2',
    'SO2 (ppb)': 'so2',
    'CO (ppm)': 'co',
    'O3 (ppb)': 'o3',
    'Temperature (°C)': 'temperature',
    'Humidity (%)': 'humidity',
    'Wind Speed (m/s)': 'wind_speed'
    }


    df = raw_df.rename(columns = renamed_columns)

    #convert date column to proper datetime
    df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

    #create month and yer columns
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year


    #Convert Measurements to Numbers
    Air_Quality_column = ['aqi', 'pm25','pm10', 'no2', 'so2',
                         'co', 'o3', 'temperature', 'humidity', 'wind_speed']

    #coerce bad values to NAN
    for col in Air_Quality_column:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = 'coerce')

    #create a mean temp column- average of max and min

    #*Outlier Handling*

    outlier_columns = ['aqi','pm25','pm10','no2','so2','co','o3']

    for col in outlier_columns:
        #calculate quartiles
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        #calculate IQR
        iqr = q3 - q1

        #calculate bounds
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        #find outliers
        too_low = df[col] < lower
        too_high = df[col] > upper

        # count outlier sum
        outliers_found = (too_low | too_high).sum()

        #cap values
        df[col] = df[col].clip(lower, upper)

        print(col, ":", outliers_found, "outliers capped")
    
    print(f" Data ranges between: {df['date'].min()} to {df['date'].max()} \n")
    print(f"Total rows: {len(df)} \n")
    
# Missing Values Handling 
# Add median to missing values

    print("missing values before cleaning:")
    print(df.isnull().sum().sum())

    for col in Air_Quality_column:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    print("missing values after cleaning:")
    print(df.isnull().sum().sum())
    return df

def export_clean_data(df):
    """Exports cleaned data as csv and JSON"""
    #export to csv
    df.to_csv('data/processed/Air_Quality_clean.csv', index= False)
   
    print("exported: daily_clean.csv to /processed")
    print("*"*50)
    #export to json
    df.to_json('data/processed/Air_Quality_clean.json', orient= 'records', date_format = 'iso', indent=2)
   
    print("exported: Air_Quality_clean.json to /processed")
    print("*"*50)


raw_df = LoadCsv()
clean_df = clean_data(raw_df)
        
export_clean_data(clean_df)

