import pandas as pd

def load_data():
    """Load the raw Malin Head weather data."""
    df = pd.read_csv( "data/raw/dly1575.csv", skiprows=24, delim_whitespace=True, header=None)
    return df

def time_columns(df):
    """Add year and month columns."""
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df

def main():
    df = load_data()
    print(df.head())

if __name__ == "__main__":
    main()
