import pandas as pd


def save_csv_google_sheet():
    """
    read data from google sheet on website and save it in local
    """
    url = r"https://docs.google.com/spreadsheets/d/1qIYw7vRh9zHJkt8DkS0SS1SbDTNEfiGFz5axAvxTwGs/edit#gid=0"
    url = url.replace("/edit#gid=", "/export?format=csv&gid=")
    df = pd.read_csv(url)
    file_path = "dane/sample.csv"
    df.to_csv(file_path, index=False)
    df = pd.read_csv(file_path)
    return df
