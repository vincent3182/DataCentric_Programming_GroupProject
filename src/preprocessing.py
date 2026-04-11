import pandas as pd
import numpy as np
from data_loading import ScrapeClimateAverages
from data_loading import LoadCsv


def clean_daily_data(df):
    """Clean the raw dataframe of Malin Head
        - convert to correct data format
        - engineer new features
    """
    df['date'] = pd.to_datetime(df['date'])

    #drop all "ind" columns  
    ind_cols = [col for col in df.columns if col.startswith('ind')]
    df = df.drop(columns = ind_cols)

    






def clean_scraped_data():
    """Cleans scraped 30 year climate normals
        - return most relevant rows
        - reshape dataframe (each month is a colmn rather than row)
    """



