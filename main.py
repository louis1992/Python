# Python 3.5
# Spacemacs

import pandas as pd

# Loading data.
def load_data():
    train_df = pd.read_csv("./train_data.csv")
    cols = ["Age"]
    data = train_df[cols].values
    return data

def get_average(data):
    sum = 0.0
    for data_ in data:
        sum = sum + data_
    return sum/len(data)

def main():
    data = load_data()
    print (get_average(data))

if __name__ == '__main__':
    main()

