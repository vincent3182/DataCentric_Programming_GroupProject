import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as plt

sns.set_theme(style="whitegrid")

MONTH_ORDER = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def load_data():
    """Load the cleaned daily and normals datasets from the processed folder"""
    daily_df = pd.read_csv("data/processed/daily_clean.csv", parse_dates=["date"])
    normals_df = pd.read_csv("data/processed/normals_clean.csv")
    normals_df.index = MONTH_ORDER
    return daily_df, normals_df

def get_monthly(daily_df):
    """Group daily data by month and return mean values"""
    daily_df["month_name"]=pd.Categorical(
        daily_df["date"].dt.strftime("%b"), categories= MONTH_ORDER, ordered=True)
    return daily_df.groupby("month_name", observed=True)[
        ["maxtp","mintp","meantp","rain","wdsp"]
    ].mean()
    

# [- Plot 1: Monthly Average temperature -]

def plot_monthly_rainfall(daily_df,save_path=None):
    """Bar chart of mean max temperature per month"""
    monthly = get_monthly(daily_df)

    fig, ax = plt.subplots(figsize = (10,5))
    monthly["maxtp"].plot(kind="bar", color ="tomato", ax=ax, width=0.6)
    ax.set_title("Malin Head - Average Max Temperature by Month", fontsize =14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Max temperature ( Degrees C )")
    ax.tick_params(axis="x",rotation=0)
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi = 150)
    plt.show


    # [- Plot 2: Monthly Average Rainfall -]

    def plot_monthly_rainfall(daily_df,save_path=None):
        """Bar chart of mean daily rainfall per month"""
        monthly = get_monthly(daily_df)

        fig, ax = plt.subplots(figsize=(10,5))
        monthly["rain"].plot(kind="bar", color ="steelblue", ax=ax, width=0.6)
        ax.set_title("Malin Head - Average Daily Rainfall by Month", fontsize=14)
        ax.set_xlabel("Month")
        ax.set_ylabel("Mean Rainfall (mm)")
        ax.tick_params(axis="x", rotation=0)
        plt.tight_layout()
        if save_path:
            fig.savepath(save_path, dpi = 150)
        plt.show

# [- Plot 3: Yearly mean temperature with trend line -]
def plot_yearly_temp_trend(daily_df, save_path=None):
    """Line chart of yearly mean temperature with a trend line"""
    yearly = daily_df.groupby("year")["meantp"].mean().dropna()

    z = np.polyfit(yearly.index, yearly.values, 1)
    trend = np.poly1d(z)

    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(yearly.index,yearly.values,color = "steelblue", marker = "o",
            markersize=3, label = "Yearly mean temp")
    ax.plot(yearly.index, trend(yearly.index), color ="red", linestyle = "--", label = "Trend")

    ax.set_title("Malin Head - Yearly Mean Temperature with Trend", fontsize =14)
    ax.set_xlable("Year")
    ax.set_ylabel("Mean Temperature (Degrees Celcius)")
    ax.legend()
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi = 150)
    plt.show
    
