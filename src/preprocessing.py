import pandas as pd
from data_loading import ScrapeClimateAverages
from data_loading import LoadCsv


def clean_daily_data(df):
    """Clean the raw dataframe of Malin Head
        - convert to correct data format
        - engineer new features (month,year, meantp)
    """
    #convert date column to proper datetime
    df['date'] = pd.to_datetime(df['date'])

    #drop all "ind" columns  
    ind_cols = [col for col in df.columns if col.startswith('ind')]
    df = df.drop(columns = ind_cols)

    #create month and yer columns
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    malin_head_column = ['maxtp', 'mintp','gmin', 'rain', 'cbl',
                         'wdsp', 'sun', 'soil', 'pe', 'evap']

    for col in malin_head_column:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = 'coerce')

    #create a mean temp column- average of max and min

    df['meantp'] = (df['maxtp'] + df['mintp']) / 2
    
    print(f" Data ranges between: {df['date'].min()} to {df['date'].max()} \n")
    print(f"Total rows: {len(df)} \n")
    
    return df




def clean_scraped_data():
    """Cleans scraped 30 year climate normals
        - return most relevant rows
        - reshape dataframe (each month is a colmn rather than row)
    """

    raw_normals_df = ScrapeClimateAverages()


    #relevant row labels from scraped table
    desired_rows ={
        'mean daily max': 'normals_maxtp',
        'mean daily min': 'normals_mintp',
        'mean temperature': 'normals_meantp',
        'mean monthly total': 'normals_rain',
        'mean monthly speed': 'normals_wdsp',
        'mean daily duration': 'normals_sun',
    }

    month_cols = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']




    clean_dictionary = {} #dictionary which will store cleaned data

    for index, row in raw_normals_df.iterrows():
        label = row.iloc[0].strip() # strip first column of each row is the variable name
        for key in desired_rows: #loop through dictionary
            if key in label.lower():
                values = pd.to_numeric(row[month_cols], errors='coerce').tolist()
                clean_dictionary[desired_rows[key]] = values
    
    # turn dictionary into dataframe where each row is a month
    result = pd.DataFrame(clean_dictionary)
    

    print("*" * 50)
    print("\nDataframe post-cleaning :\n")
    print("*" * 50)

    print(result)
    return result

cleaned_normals = clean_scraped_data()

df = LoadCsv()
cleaned_csv = clean_daily_data(df)

#print(cleaned_csv)

def export_clean_data(daily_df,normals_df):
    """exports both cleaned dataframes to processed folder as CSV"""

    daily_df.to_csv('data/processed/daily_clean.csv', index= False)
    print("exported: daily_clean.csv to /processed")
    print("*"*50)

    normals_df.to_csv('data/processed/normals_clean.csv', index= False)
    print("exported: normals_clean.csv to /processed")
    print("*"*50)

export_clean_data(cleaned_csv,cleaned_normals)