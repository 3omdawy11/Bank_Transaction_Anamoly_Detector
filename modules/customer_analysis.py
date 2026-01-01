
from . import pd, os
class CustomerAnalysis:
    

    @staticmethod
    def classify(z):
            if z > 3: return 'Critical'
            if z > 1.5: return 'High'
            if z > 0: return 'Medium'
            return 'Low'

    @staticmethod
    def score_customers():
        if os.path.exists('customer_risk_bands.csv'):
            print("Loading existing 'customer_risk_bands.csv'...")
            customer_df = pd.read_csv('customer_risk_bands.csv')
            return customer_df

        print("Scoring customers...")
        # read customer_risk_bands.csv
        customer_df = pd.read_csv('customer_risk_scoring.csv')
        
        
        customer_df['risk_band'] = customer_df['max_z'].apply(CustomerAnalysis.classify)

        # 6. Save the risk-banded dataset
        customer_df[['nameOrig', 'risk_band']].to_csv('customer_risk_bands.csv')
        print("Success! Created 'customer_risk_bands.csv'")

        return
    @staticmethod
    def flag_suspicious_transactions(df):
         suspicious_transactions = df[df['isFraud'] == 1]
         suspicious_transactions.to_csv('suspicious_transactions.csv', index=False)
         print("Success! Created 'suspicious_transactions.csv'")
        