from Set import Set
import pandas as pd


def get_data(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    print(df.head())
    return df

#def 


if __name__ == "__main__":
    data = get_data("../data/strong.csv")
