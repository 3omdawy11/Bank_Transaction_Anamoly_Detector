from . import pd
class DataPreparation:
    

    @staticmethod
    def data_info(df):
        print("Data Information:")
        print(df.info())
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nData Description:")
        print(df.describe())
        return df
    
    @staticmethod
    def remove_missing_values(df):
        df = df.dropna()
        return df

    def remove_duplicates(df):
        df = df.drop_duplicates()
        return df

    @staticmethod
    def add_date_column(df):
        df['date'] = pd.to_datetime(df['step'], unit='h', origin='2025-01-01')
        return df
    
    @staticmethod
    def reset_index(df):
        df = df.reset_index(drop=True)
        return df
    
    def fix_data(df):
        df = df[(df["isFraud"] == 1) | (df["isFlaggedFraud"] == 1) | 
            ((df["amount"] != 0) & (df["oldbalanceOrg"] - df["newbalanceOrig"] == df["amount"]) & 
             ((df["newbalanceDest"] - df["oldbalanceDest"] == df["amount"]) | (df["nameDest"].str.contains("M")))) |
            ((df["amount"] != 0) & (df["newbalanceOrig"] - df["oldbalanceOrg"] == df["amount"]) & ((df["oldbalanceDest"] - df["newbalanceDest"] == df["amount"])))]
        
        return df
    
    @staticmethod
    def prepare_data(df):
        print(f"Initial data shape: {df.shape}")
        df = DataPreparation.data_info(df)
        
        df = DataPreparation.remove_missing_values(df)
        df = DataPreparation.remove_duplicates(df)
        print("Data after removing missing values and duplicates:")
        df = DataPreparation.fix_data(df)
        print(df.shape)
        df = DataPreparation.add_date_column(df)
        df = DataPreparation.reset_index(df)
        print(df.shape)
        return df
    