import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

sns.set_theme(style="whitegrid")

MONTH_ORDER = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def load_data():
    """Load the cleaned Air Quality dataset from the processed folder."""
    df = pd.read_csv("data/processed/Air_Quality_clean.csv", parse_dates=["date"])
    df["month_name"] = pd.Categorical(
        df["date"].dt.strftime("%b"), categories=MONTH_ORDER, ordered=True
    )
    return df

def get_monthly(daily_df):
    """Group daily data by month and return mean values"""
    daily_df["month_name"]=pd.Categorical(
        daily_df["date"].dt.strftime("%b"), categories= MONTH_ORDER, ordered=True)
    return daily_df.groupby("month_name", observed=True)[
        ["maxtp","mintp","meantp","rain","wdsp"]
    ].mean()
    

# [- Plot 1: Average AQI by City -]
 
def plot_aqi_by_city(df, save_path=None):
    """Bar chart showing mean AQI for each city.
    
    Shows which cities have the worst and best air quality on average.
    """
    city_aqi = df.groupby("city")["aqi"].mean().sort_values(ascending=False).reset_index()
 
    fig, ax = plt.subplots(figsize=(11, 5))
    sns.barplot(data=city_aqi, x="city", y="aqi", palette="Reds_d", ax=ax)
    ax.set_title("Global Air Quality — Average AQI by City", fontsize=14)
    ax.set_xlabel("City")
    ax.set_ylabel("Mean AQI")
    ax.tick_params(axis="x", rotation=15)
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()


# [- Plot 2: Monthly Average AQI Trend (Line Chart) -]
 
def plot_monthly_aqi_trend(df, save_path=None):
    """Line chart of average AQI per month across all cities.
    
    Shows whether air quality gets better or worse at certain times of year.
    """
    monthly = df.groupby("month_name", observed=True)["aqi"].mean().reset_index()
 
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly["month_name"], monthly["aqi"], color="tomato",
            marker="o", markersize=6, label="Mean AQI")
    ax.set_title("Global Air Quality — Average AQI by Month", fontsize=14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean AQI")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()

# [- Plot 3: PM2.5 Distribution Histogram -]
 
def plot_pm25_distribution(df, save_path=None):
    """Histogram of PM2.5 readings across all cities.
    
    PM2.5 is the most harmful pollutant — this shows how often
    dangerous levels occur. The red line marks the WHO guideline of 15 µg/m³.
    """
    pm25 = df["pm25"].dropna()
    who_limit = 15
    p90 = np.percentile(pm25, 90)
 
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(pm25, bins=30, color="steelblue", edgecolor="white")
    ax.axvline(who_limit, color="red", linestyle="--",
               label=f"WHO guideline ({who_limit} µg/m³)")
    ax.axvline(p90, color="orange", linestyle="--",
               label=f"90th percentile ({p90:.1f} µg/m³)")
    ax.set_title("Global Air Quality — PM2.5 Distribution", fontsize=14)
    ax.set_xlabel("PM2.5 (µg/m³)")
    ax.set_ylabel("Number of Readings")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()

# [- Plot 4: Average Pollutant Levels by City (Bar Chart) -]
 
def plot_pollutants_by_city(df, save_path=None):
    """Bar chart comparing mean PM2.5, NO2 and O3 levels across cities.
    
    Groups the three main pollutants side by side for each city
    so they can be directly compared.
    """
    city_poll = df.groupby("city")[["pm25", "no2", "o3"]].mean().reset_index()
 
    x = np.arange(len(city_poll["city"]))
    width = 0.25
 
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(x - width, city_poll["pm25"], width, label="PM2.5", color="tomato")
    ax.bar(x,         city_poll["no2"],  width, label="NO2",   color="steelblue")
    ax.bar(x + width, city_poll["o3"],   width, label="O3",    color="seagreen")
    ax.set_xticks(x)
    ax.set_xticklabels(city_poll["city"], rotation=15)
    ax.set_title("Global Air Quality — Mean Pollutant Levels by City", fontsize=14)
    ax.set_xlabel("City")
    ax.set_ylabel("Mean Concentration (µg/m³ or ppb)")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()


# [- Plot 5: Rolling Average AQI for Top 3 Polluted Cities (Line Chart) -]
 
def plot_rolling_aqi(df, save_path=None):
    """Line chart of 30-day rolling average AQI for the 3 most polluted cities.
    
    Rolling averages smooth out daily noise and reveal the underlying
    pollution trend over the year.
    """
    top3_cities = df.groupby("city")["aqi"].mean().nlargest(3).index.tolist()
    df_top3 = df[df["city"].isin(top3_cities)].copy()
    df_top3 = df_top3.sort_values("date")
 
    fig, ax = plt.subplots(figsize=(12, 5))
 
    for city in top3_cities:
        city_df = df_top3[df_top3["city"] == city].set_index("date")
        rolling = city_df["aqi"].rolling(window=30, min_periods=1).mean()
        ax.plot(rolling.index, rolling.values, marker="", linewidth=2, label=city)
 
    ax.set_title("Global Air Quality — 30-Day Rolling Average AQI (Top 3 Cities)", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("AQI (30-day rolling mean)")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()

# [- Run All Plots -]
 
if __name__ == "__main__":
    df = load_data()
 
    plot_aqi_by_city(df,save_path="outputs/figures/aqi_by_city.png")
    plot_monthly_aqi_trend(df,save_path="outputs/figures/monthly_aqi_trend.png")
    plot_pm25_distribution(df,save_path="outputs/figures/pm25_distribution.png")
    plot_pollutants_by_city(df,save_path="outputs/figures/pollutants_by_city.png")
    plot_rolling_aqi(df,save_path="outputs/figures/rolling_aqi.png")