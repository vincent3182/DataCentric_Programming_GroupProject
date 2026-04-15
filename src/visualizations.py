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

