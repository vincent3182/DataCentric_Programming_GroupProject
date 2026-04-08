import pandas as pd
from bs4 import BeautifulSoup
import requests

def LoadCsv():
    """Loads csv file of Malin Head from Met Eireann"""
    df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)


def ScrapeClimateAverages():
    """ Scrapes 30 year climate normals table from Met EIreanns Malin Head page"""
    url = "https://www.met.ie/cms/assets/uploads/2023/09/www_met_ie_malin_9120.htm"

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    table = soup.find("table")

    rows = table.find_all("tr")

    print(response.text)
#data = []
#for row in rows:
#    cols = row.find_all(["td","th"])
#    cols = [col.text.strip() for col in cols]
#    data.append(cols)

#df = pd.DataFrame(data)

    print(f"Status code: {response.status_code}\n")





#print(df.isnull().sum())
LoadCsv()
ScrapeClimateAverages()