import pandas as pd
from bs4 import beautifulsoup
import requests




df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)

print(df.head())
print(df.shape)



print(df.isnull().sum())