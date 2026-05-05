import os
import pandas as pd
import numpy as np
from preprocessing import clean_data
from data_loading import load_csv


def descriptive_stats(df, columns):
    """Return descriptive statistics for selected numeric columns."""
    stats = {}

    for col in columns:
        if col in df.columns:
            values = df[col].dropna()

            stats[col] = {
                "mean": np.mean(values),
                "median": np.median(values),
                "std_dev": np.std(values, ddof=1),
                "variance": np.var(values, ddof=1),
                "min": np.min(values),
                "25th_percentile": np.percentile(values, 25),
                "50th_percentile": np.percentile(values, 50),
                "75th_percentile": np.percentile(values, 75),
                "max": np.max(values)
            }

    return pd.DataFrame(stats).T


def city_summary(df):
    """Return average AQI and pollutant values by city."""
    summary = df.groupby("city")[["aqi", "pm25", "pm10", "no2", "so2", "co", "o3"]].mean()
    return summary.round(2)


def country_summary(df):
    """Return average AQI and pollutant values by country."""
    summary = df.groupby("country")[["aqi", "pm25", "pm10", "no2", "so2", "co", "o3"]].mean()
    return summary.round(2)


def monthly_summary(df):
    """Return monthly average AQI and pollutant values."""
    summary = df.groupby("month")[["aqi", "pm25", "pm10", "no2", "so2", "co", "o3"]].mean()
    return summary.round(2)


def main():
    raw_df = load_csv()
    df = clean_data(raw_df)

    numeric_columns = [
        "aqi", "pm25", "pm10", "no2", "so2",
        "co", "o3", "temperature", "humidity", "wind_speed"
    ]

    print("*" * 50)
    print("DATASET OVERVIEW")
    print(df.head())
    print("\nShape:", df.shape)

    print("*" * 50)
    print("MISSING VALUES")
    print(df[numeric_columns].isnull().sum())

    print("*" * 50)
    print("DESCRIPTIVE STATISTICS")
    stats_df = descriptive_stats(df, numeric_columns)
    print(stats_df.round(2))

    print("*" * 50)
    print("AVERAGE VALUES BY CITY")
    city_df = city_summary(df)
    print(city_df)

    print("*" * 50)
    print("AVERAGE VALUES BY COUNTRY")
    country_df = country_summary(df)
    print(country_df)

    print("*" * 50)
    print("MONTHLY AVERAGES")
    monthly_df = monthly_summary(df)
    print(monthly_df)

    os.makedirs("data/processed", exist_ok=True)
    stats_df.round(2).to_csv("data/processed/descriptive_statistics.csv")
    city_df.to_csv("data/processed/city_summary.csv")
    country_df.to_csv("data/processed/country_summary.csv")
    monthly_df.to_csv("data/processed/monthly_summary.csv")

    print("*" * 50)
    print("Analysis results exported to data/processed")


if __name__ == "__main__":
    main()
