import pandas as pd
from data_loading import LoadCsv
from pre_processing import clean_daily_data, clean_scraped_data


def main():
    raw_df = LoadCsv()
    df = clean_daily_data(raw_df)
    normals_df = clean_scraped_data()

    print("\n" + "*" * 50)
    print("DATA OVERVIEW")
    print("*" * 50)
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDate range:")
    print(df["date"].min(), "to", df["date"].max())

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nSummary statistics:")
    print(df[["maxtp", "mintp", "meantp", "rain", "wdsp", "sun"]].describe())

    print("\nKey findings:")
    print("Average max temperature:", round(df["maxtp"].mean(), 2))
    print("Average min temperature:", round(df["mintp"].mean(), 2))
    print("Average mean temperature:", round(df["meantp"].mean(), 2))
    print("Total rainfall:", round(df["rain"].sum(), 2))
    print("Average wind speed:", round(df["wdsp"].mean(), 2))
    print("Average sunshine:", round(df["sun"].mean(), 2))

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    df["month_name"] = pd.Categorical(
        df["date"].dt.strftime("%b"),
        categories=month_order,
        ordered=True
        )

    monthly = df.groupby("month_name")[["maxtp", "mintp", "meantp", "rain", "sun"]].mean()
    print("\n" + "*" * 50)
    print("MONTHLY AVERAGES")
    print("*" * 50)
    print(monthly)

    yearly = df.groupby("year")[["maxtp", "mintp", "meantp", "rain"]].mean()
    print("\n" + "*" * 50)
    print("YEARLY AVERAGES")
    print("*" * 50)
    print(yearly.head(10))

    print("\n" + "*" * 50)
    print("NORMALS DATA")
    print("*" * 50)
    print(normals_df.head())


if __name__ == "__main__":
    main()
