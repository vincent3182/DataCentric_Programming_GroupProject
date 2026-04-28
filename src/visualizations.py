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


    
#def plot_yearly_temp_trend(df, save_path = None):
   # """Line chart of yearly mean man temperature with a trend line"""
   # df = df.copy()
    #df["date"] = pd.to_datetime(df["date"],dayfirst=True)
    #df["year"] = df["date"].dt.year
    #df["maxtp"] = pd.to_numeric(df["maxtp"],errors="coerce")

    #yearly = df.groupby("year")["maxtp"].mean().reset_index().dropna()
    #z = np.polyfit(yearly["year"],yearly["maxtp"],1)
    #trend = np.poly1d(z)

    #fig, ax = plt.subplots(figsize=(12,5))
    #sns.lineplot(data=yearly, x = "year", y = "maxtp", color = "steelblue", marker = "o", markersize=4, ax = ax, label = "Annual mean max temp")
    #ax.plot(yearly["year"],trend(yearly["year"]),color="red",linestyle="--", label="Trend")
    #ax.set_title("Malin Head - Annual Mean Max Temperature with trend", fontsize=14)
    #ax.set_xlabel("Year")
    #ax.set_ylabel("Mean Max Temperature (Degrees C)")
    #ax.legend()
    #plt.tight_layout()
    #if save_path:
       # fig.savefig(save_path,dpi=150)
   # plt.show()
#df = LoadCsv()
#plot_yearly_temp_trend(df)

#def plot_wind_distrbution(df, save_path=None):
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
#df = LoadCsv()
#plot_wind_distrbution(df)    