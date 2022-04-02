import pandas as pd

def read_sheet_data():
    url = r"https://docs.google.com/spreadsheets/d/1qIYw7vRh9zHJkt8DkS0SS1SbDTNEfiGFz5axAvxTwGs/edit#gid=0"
    url = url.replace("/edit#gid=", "/export?format=csv&gid=")
    df = pd.read_csv(url)
    return df


def save_csv(df):
    file_path = "../dane/sample.csv"
    df.to_csv(file_path, index=False)

a = read_sheet_data()
print(a)
print(a.head(2))
save_csv(a)