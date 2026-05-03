import pandas as pd


def LoadCsv():
    """Loads csv file of Air Quality dataset fromm data/raw folder"""
    df = pd.read_csv('data/raw/global_air_quality_dataset.csv')
    
    print("*"* 50)
    print("Succesfully laoded CSV File")

    print(df.shape)
    return df




if __name__ == "__main__":
    LoadCsv()
