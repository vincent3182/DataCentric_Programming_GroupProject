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

# [- Plot 4: Wind Speed Histogram -]

def plot_wind_distribution(daily_df, save_path=None):
    """Histogram of daily mean wind speed"""
    wind = daily_df["wdsp"].dropna()
    p90 = np.percentile(wind,90)

    fig, ax = plt.subplots(figsize=(9,5))
    ax.hist(wind, bins=30, color ="steelblue", edgecolor="white")
    ax.axvline(p90, color="red",linestyle="--",label=f"90th percentile ({p90:.1f} kts)")
    ax.set_title("Malin Head - Wind Speed Distribution", fontsize=14)
    ax.set_xlabel("Mean Wind Speed (knots) ")
    ax.set_ylabel("NUmber of Days")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path,dpi = 150)
    plt.show()


# [- Plot 5: Actual vs 30 Year Normals Comparison -]

def plot_actual_vs_normals(daily_df, normals_df, save_path=None):
    """Line chart comparing actual monthly mean temp against the 30-year normals
    
    This uses the scraped normals data alongside the daily records to show
    whether recent temperatures sit above or below the long-term average"""

    monthly = get_monthly(daily_df)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(MONTH_ORDER, monthly["meantp"].values, color ="tomato", marker = "o", label="Actual Mean temp")
    ax.plot(MONTH_ORDER, normals_df["normals_meantp"].values, color = "steelblue", marker ="o", linestyle ="--", label = "30-year normal")

    ax.set_title("Malin Head - Actual vs 30 Year Normal Temperature", fontsize = 14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Temperature (Degrees Celcius)")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi = 150)
    plt.show()

#[- Run All Plots -]

if __name__ == "__main__":
    daily_df, normals_df = load_data()
 
    plot_monthly_temp(daily_df,save_path="outputs/figures/monthly_temp.png")
    
    plot_monthly_rainfall(daily_df,save_path="outputs/figures/monthly_rainfall.png")
    
    plot_yearly_temp_trend(daily_df,save_path="outputs/figures/yearly_trend.png")
    
    plot_wind_distribution(daily_df,save_path="outputs/figures/wind_distribution.png")
    
    plot_actual_vs_normals(daily_df,normals_df,save_path="outputs/figures/actual_vs_normals.png")