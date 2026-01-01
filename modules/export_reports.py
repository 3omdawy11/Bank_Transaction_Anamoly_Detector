from . import pd, os, getChoice

class ExportReports:
    

    @staticmethod
    def export_customer_risk_bands():
        if os.path.exists('customer_risk_bands.csv'):
            print("Exporting 'customer_risk_bands.csv'...")
            customer_df = pd.read_csv('customer_risk_bands.csv')
            print(customer_df.head(10))

    @staticmethod
    def export_suspicious_transactions():
        if os.path.exists('suspicious_transactions.csv'):
            print("Exporting 'suspicious_transactions.csv'...")
            suspicous_transactions = pd.read_csv('suspicious_transactions.csv')
            print(suspicous_transactions.head(10))


    @staticmethod
    def export_reports_menu():
        menu = """
        Export Reports Menu:
        1. Export Customer Risk Bands
        2. Export Suspicious Transactions
        0. Exit
        """
        print(menu)

    @staticmethod
    def action(choice):
        
        if choice == 1:
            ExportReports.export_customer_risk_bands()
        elif choice == 2:
            ExportReports.export_suspicious_transactions()
        elif choice == 0:
            print("Exiting Export Reports Menu.")
        else:
            print("Invalid choice in Export Reports Menu.")