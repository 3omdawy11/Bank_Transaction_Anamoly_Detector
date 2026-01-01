from . import pd, np
import os

class FeatureBuilder:
    def build_features(self, data):
        # Placeholder for feature building logic
        print("Building features...")
        return data
    
    def build_customer_dataset(self, df):

        # try reading from existing file
        if os.path.exists('customer_features_dataset.csv'):
            print("Loading existing 'customer_features_dataset.csv'...")
            customer_df = pd.read_csv('customer_features_dataset.csv')
            return customer_df


        print("Transforming transactions into customer features...")

        # 1. Setup Time Variables
        # PaySim 'step' is hours. 24 steps = 1 day.
        df['day'] = (df['step'] // 24) + 1

        # 2. Aggregate Basic Stats
        # This covers: count, total, average, and max amounts
        customer_df = df.groupby('nameOrig').agg({
            'amount': ['count', 'sum', 'mean', 'max'],
            'step': ['max', 'min']
        })

        # Flatten the MultiIndex columns (e.g., 'amount_sum')
        customer_df.columns = [
            'transaction_count', 
            'total_amount', 
            'average_amount', 
            'max_amount', 
            'last_active_step', 
            'first_active_step'
        ]

        # 3. Calculate Daily Transaction Velocity
        # Velocity = Total Transactions / Total Days present in dataset
        total_days = (df['day'].max() - df['day'].min()) + 1
        customer_df['daily_velocity'] = customer_df['transaction_count'] / total_days

        # 4. Rolling Statistics (Behavioral Shifts)
        # We calculate the rolling average of the last 3 transactions for each user
        # Note: This is done on the original df then mapped back
        df['rolling_avg_3'] = df.groupby('nameOrig')['amount'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())
        
        # Take the most recent rolling average per customer as a feature
        latest_rolling = df.groupby('nameOrig')['rolling_avg_3'].last()
        customer_df['current_rolling_avg'] = latest_rolling

        # 5. Save the new dataset
        customer_df.to_csv('customer_features_dataset.csv')
        print("Success! Created 'customer_features_dataset.csv'")
        
        return customer_df
    

    def apply_risk_scoring(self, customer_df):

        # if customer_risk_band file exists read and return

        if os.path.exists('customer_risk_scoring.csv'):
            print("Loading existing 'customer_risk_scoring.csv'...")

            customer_df = pd.read_csv('customer_risk_scoring.csv')
            return customer_df


        print("Applying log transformation and calculating risk scores...")
        
        # 1. Target features for scoring
        features_to_score = ['total_amount', 'daily_velocity', 'current_rolling_avg']
        
        for feature in features_to_score:
            # 2. Overwrite the original column with its log value
            # We use log1p (log of 1+x) to avoid errors with 0 values
            customer_df[feature] = np.log1p(customer_df[feature])
            
            # 3. Calculate Z-score based on the now-transformed column
            mu = customer_df[feature].mean()
            sigma = customer_df[feature].std()
            
            # Note: We still create a separate Z-score column to keep the logic clean
            customer_df[f'{feature}_zscore'] = (customer_df[feature] - mu) / sigma
        
        # 4. Determine the Maximum Z-score across these factors
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