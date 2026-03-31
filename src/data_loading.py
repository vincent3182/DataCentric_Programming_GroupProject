import pandas as pd

df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)

print(df.head())
print(df.shape)


#convert date to date format
df['date'] = pd.to_datetime(df['date'])