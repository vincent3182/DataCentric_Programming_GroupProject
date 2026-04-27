import pandas as pd
import numpy as np
from data_loading import LoadCsv
from preprocessing import clean_daily_data


def main():
    raw_df = LoadCsv()
    df = clean_daily_data(raw_df)

    print("\n" + "*" * 50)
    print("DATA OVERVIEW")
    print("*" * 50)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDate range:")
    print(df["date"].min(), "to", df["date"].max())

    print("\nMissing values:")
    print(df.isna().sum())

    stats_columns = ["maxtp", "mintp", "meantp", "rain", "wdsp", "sun"]
    stats_columns = [c for c in stats_columns if c in df.columns]

    print("\nSummary statistics:")
    print(df[stats_columns].describe())

    print("\nVariance and percentiles:")
    for col in stats_columns:
        values = df[col].dropna()
        print(f"\n{col.upper()}:")
        print("Variance:", round(np.var(values, ddof=1), 2))
        print("25th percentile:", round(np.percentile(values, 25), 2))
        print("50th percentile:", round(np.percentile(values, 50), 2))
        print("75th percentile:", round(np.percentile(values, 75), 2))

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    df["month_name"] = pd.Categorical(
        df["date"].dt.strftime("%b"),
        categories=month_order,
        ordered=True
    )

    monthly = df.groupby("month_name", observed=True)[["maxtp", "mintp", "meantp", "rain", "sun"]].mean()
    yearly = df.groupby("year", observed=True)[["maxtp", "mintp", "meantp", "rain"]].mean()

    print("\n" + "*" * 50)
    print("MONTHLY AVERAGES")
    print("*" * 50)
    print(monthly)

    print("\n" + "*" * 50)
    print("YEARLY AVERAGES")
    print("*" * 50)
    print(yearly)


if __name__ == "__main__":
    main()
