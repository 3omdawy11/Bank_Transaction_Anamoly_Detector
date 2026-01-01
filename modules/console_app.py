from modules.export_reports import ExportReports
from .data_manager import DataManager
from .data_preparation import DataPreparation
from . import getChoice
from .feature_builder import FeatureBuilder
from .customer_analysis import CustomerAnalysis
from modules import feature_builder

class ConsoleApp:
    dataset = None
    cusotomer_rfm_scores = None
    data_manager = DataManager()
    data_preparation = DataPreparation()
    data_preparation_done = False
    feature_builder = FeatureBuilder()
    feature_builder_done = False

    def run(self):
        print("Console Application is running.")
    
    def stop(self):
        print("Console Application is stopping.")

    
    def options_menu(self):
        menu = """
        Main Menu:
        1. Data Manager
        2. Data Preparation
        3. Feature Building
        4. Customer Analysis
        5. Anomaly Detection
        6. Reporting
        7. Summary
        0. Exit
        """
        print(menu)
        

    def action(self, number):
        if number == 0:
            self.stop()
            return 0
        elif number == 1:
            print("Action 1 executed.")
            self.data_manager.list_data_manager_menu()
            choice = getChoice()
            self.dataset = self.data_manager.action(choice)  
            print(f"Current dataset: {self.dataset.head() if self.dataset is not None else 'No dataset loaded.'}")  

        elif number == 2:
            print("Action 2 executed.")
            if self.dataset is not None:
                self.dataset = self.data_preparation.prepare_data(self.dataset)
                print("Data prepared successfully.")
                self.data_preparation_done = True
            else:
                print("No dataset loaded. Please load a dataset first.")
        elif number == 3:
            if self.data_preparation_done:
                print("Action 3 executed.")
                self.feature_builder.build_customer_features(self.dataset)

                print("Customer RFM scores built successfully.")
                self.feature_builder_done = True
            else:
                print("Data preparation not done. Please prepare the data first.")
                

        elif number == 4:
            if self.feature_builder_done:
                print("Action 4 executed.")
                CustomerAnalysis.score_customers()
            else: 
                print("Feature building not done. Please build features first.")
            print("Action 4 executed.")
        elif number == 5:
            CustomerAnalysis.flag_suspicious_transactions(self.dataset)
            print("Action 5 executed.")
        elif number == 6:
            ExportReports.export_reports_menu()
            choice = getChoice(" to select a report to export (0 to exit): ")

            ExportReports.action(choice)

            print("Action 6 executed.")
        elif number == 7:
            print("In this application you can manage data, prepare it, build features, analyze customers, detect anomalies, and generate reports.")
        else:
            print("Invalid action number.")