import pandas as pd

class DataController:
    @staticmethod
    def load_data(file_path):
        return pd.read_excel(file_path)

    @staticmethod
    def save_data(dataframe, file_path):
        dataframe.to_excel(file_path, index=False)
