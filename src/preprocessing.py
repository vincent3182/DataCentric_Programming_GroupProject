import pandas as pd
import numpy as np

def clean_dataframe(df):
    """Clean the raw dataframe of Malin Head
        - convert to correct data format
        - engineer new features
    """



def clean_scraped_data:
data=[]
        rows = soup.find_all("tr")
        for row in rows:
           
           cols = [c.get_text(strip=True) for c in row.find_all("td")]

           if len(cols) == 14:
                data.append(cols)

        clean_data = data[1:]
    
        header = data[1]

        df = pd.DataFrame(clean_data,  columns= header)
        




df['date'] = pd.to_datetime(df['date'])
