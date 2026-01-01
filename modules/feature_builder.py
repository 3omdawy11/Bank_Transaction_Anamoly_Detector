from . import pd, np
import os

class FeatureBuilder:
    def build_features(self, data):
        # Placeholder for feature building logic
        print("Building features...")
        return data
    
    def build_customer_dataset(self, df):

    
        if os.path.exists('customer_features_dataset.csv'):
            print("Loading existing 'customer_features_dataset.csv'...")
            customer_df = pd.read_csv('customer_features_dataset.csv')
            return customer_df


        print("Transforming transactions into customer features...")

        df['day'] = (df['step'] // 24) + 1


        customer_df = df.groupby('nameOrig').agg({
            'amount': ['count', 'sum', 'mean', 'max'],
            'step': ['max', 'min']
        })

        customer_df.columns = [
            'transaction_count', 
            'total_amount', 
            'average_amount', 
            'max_amount', 
            'last_active_step', 
            'first_active_step'
        ]

        total_days = (df['day'].max() - df['day'].min()) + 1
        customer_df['daily_velocity'] = customer_df['transaction_count'] / total_days

        
        df['rolling_avg_3'] = df.groupby('nameOrig')['amount'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
        
        
        latest_rolling = df.groupby('nameOrig')['rolling_avg_3'].last()
        customer_df['current_rolling_avg'] = latest_rolling

        customer_df.to_csv('customer_features_dataset.csv')
        print("Success! Created 'customer_features_dataset.csv'")
        
        return customer_df
    

    def apply_risk_scoring(self, customer_df):


        if os.path.exists('customer_risk_scoring.csv'):
            print("Loading existing 'customer_risk_scoring.csv'...")

            customer_df = pd.read_csv('customer_risk_scoring.csv')
            return customer_df


        print("Applying log transformation and calculating risk scores...")
        
        features_to_score = ['total_amount', 'daily_velocity', 'current_rolling_avg']
        
        for feature in features_to_score:
 
            customer_df[feature] = np.log1p(customer_df[feature])

            mu = customer_df[feature].mean()
            sigma = customer_df[feature].std()
            
            customer_df[f'{feature}_zscore'] = (customer_df[feature] - mu) / sigma
        
        z_cols = [f'{f}_zscore' for f in features_to_score]
        customer_df['max_z'] = customer_df[z_cols].max(axis=1)
        
        customer_df.to_csv('customer_risk_scoring.csv')
        print("Success! Created 'customer_risk_scoring.csv'")

        return 
    

    def build_customer_features(self, df):
        customer_df = self.build_customer_dataset(df)
        customer_df = self.apply_risk_scoring(customer_df)
        print("Customer scoring complete.")
        return 