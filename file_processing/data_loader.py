import pandas as pd

class DataLoader():
    def load_data(self, data_dir):
        df = pd.read_csv(data_dir)
        print(df)

if __name__ == '__main__':
    dl = DataLoader()
    
    dl.load_data(data_dir = "datasets/grocery_data.csv")