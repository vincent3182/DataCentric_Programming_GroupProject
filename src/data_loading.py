import pandas as pd
from bs4 import BeautifulSoup
import requests

def LoadCsv():
    """Loads csv file of Malin Head from Met Eireann"""
    df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)
    
    return df

def ScrapeClimateAverages():
    """ Scrapes 30 year climate normals table from Met EIreanns Malin Head page"""
    url = "https://www.met.ie/cms/assets/uploads/2023/09/www_met_ie_malin_9120.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    table = soup.find("table")

    rows = table.find_all("tr")

    print(f"Status code: {response.status_code}\n")
    
    if response.ok:
        print(f"Succesfully fetched: {url}\n")

        data=[]
        rows = soup.find_all("tr")
        for row in rows:
           
           cols = [c.get_text(strip=True) for c in row.find_all("td")]

           if len(cols) == 14:
                data.append(cols)

        scraped_data = data[2:]
        
        column_names = data[1]

        Normals30Yr_df = pd.DataFrame(scraped_data, columns = column_names)        
        return Normals30Yr_df
        #return scraped_data

daily_df = LoadCsv()

print(daily_df.head())
print(daily_df.columns.tolist())

print("*" * 50)
print("\nSuccesfully laoded csv file\n")

print("*" *50)
print("\nScraped raw data - Malin Head\n")
print("*" *50)

normals_df = ScrapeClimateAverages()
print(normals_df)