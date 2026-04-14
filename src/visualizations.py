import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def LoadCsv():
    """Loads csv file of Malin Head from Met Eireann"""
    df = pd.read_csv('data/raw/dly1575.csv', skiprows= 24)
    return df

sns.set_theme(style="whitegrid")
MONTH_ORDER = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def plot_monthly_temp(df, save_path=None):
    """Box plot of max temperature by month."""
    df["date"] = pd.to_datetime(df["date"])
    df["month_name"] = df["date"].dt.strftime("%b")
    
    if "maxtp" in df.columns:
        df["max_temp"] = df["maxtp"]
    elif "max_temp" not in df.columns:
        raise ValueError("No max temperature column found")
   
    df["month_name"]= pd.Categorical(
        df["month_name"], categories=MONTH_ORDER, ordered=True
    )
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=df, x="month_name", y="max_temp", ax=ax, palette="coolwarm")
    ax.set_title("Malin Head — Monthly Max Temperature Distribution")
    ax.set_xlabel("Month")
    ax.set_ylabel("Max Temp (°C)")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    plt.show()

df = LoadCsv()
plot_monthly_temp(df)

