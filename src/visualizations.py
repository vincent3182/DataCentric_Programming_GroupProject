import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from data_loading import LoadCsv


sns.set_theme(style="whitegrid")
MONTH_ORDER = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def LoadCsv():
    """Loads csv file of Malin Head from Met Eireann"""
    df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)
    return df

def plot_monthly_temp(df, save_path=None):
    """Bar chart of mean max temperature per month."""
    df = df.copy()
    df["date"]= pd.to_datetime(df["date"],dayfirst=True)
    df["month_name"] = pd.Categorical(
        df["date"].dt.strftime("%b"), categories=MONTH_ORDER, ordered= True)
    df["maxtp"] = pd.to_numeric(df["maxtp"],errors = "coerce")
    monthly = df.groupby("month_name",observed= True)["maxtp"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=df, x="month_name",y="maxtp",palette="coolwarm",ax=ax)
    ax.set_title("Malin Head - Average Max Temperature by Month", fontsize = 14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Max Temperature (Degrees C)")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path,dpi=150)    
    plt.show()
df = LoadCsv()
plot_monthly_temp(df)

def plot_monthly_rainfall(df,save_path=None):
    """Bar chart of mean daily rainfall per month"""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"],dayfirst=True)
    df["month_name"] = pd.Categorical(df["date"].dt.strftime("%b"), categories=MONTH_ORDER, ordered= True)
    df["rain"] = pd.to_numeric(df["rain"],errors = "coerce")

    monthly = df.groupby("month_name", observed = True)["rain"].mean().reset_index()

    fig, ax = plt.subplots(figsize = (10,5))
    sns.barplot(data=monthly, x = "month_name", y = "rain", palette ="Blues_d", ax = ax)
    ax.set_title("Malin Head - Average Daily Rainfall by Month", fontsize=14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Rainfall (mm)")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()
df = LoadCsv()
plot_monthly_rainfall(df)

def plot_yearly_temp_trend(df, save_path = None):
    """Line chart of yearly mean man temperature with a trend line"""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"],dayfirst=True)
    df["year"] = df["date"].dt.year
    df["maxtp"] = pd.to_numeric(df["maxtp"],errors="coerce")

    yearly = df.groupby("year")["maxtp"].mean().reset_index().dropna()
    z = np.polyfit(yearly["year"],yearly["maxtp"],1)
    trend = np.poly1d(z)

    fig, ax = plt.subplots(figsize=(12,5))
    sns.lineplot(data=yearly, x = "year", y = "maxtp", color = "steelblue", marker = "o", markersize=4, ax = ax, label = "Annual mean max temp")
    ax.plot(yearly["year"],trend(yearly["year"]),color="red",linestyle="--", label="Trend")
    ax.set_title("Malin Head - Annual Mean Max Temperature with trend", fontsize=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Max Temperature (Degrees C)")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path,dpi=150)
    plt.show()
df = LoadCsv()
plot_yearly_temp_trend(df)

def plot_wind_distrbution(df, save_path=None):
    """Histogram of daily mean wind speed """
    df = df.copy()
    df["wdsp"] = pd.to_numeric(df["wdsp"], errors="coerce")
    p90 = df["wdsp"].quantile(0,90)

    fig, ax = plt.subplots(figsize=(9,5))
    sns.histplot(df["wdsp"].dropna(), bins=30, kde=True, color="steelblue", ax = ax)
    ax.axline(p90, color="red",linestyle="--", label=f"90th percentile({p90:.1f}kts")
    ax.set_title("Malin Head - Wind Speed Distribution", fontsize=14)
    ax.set_xlabel("Mean Wind Speed(knots)")
    ax.set_ylabel("Number of Days")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()
df = LoadCsv()
plot_wind_distrbution(df)    