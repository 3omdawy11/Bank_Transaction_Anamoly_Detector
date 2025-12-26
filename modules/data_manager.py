import os
from . import getChoice, np, pd

class DataManager:
   
    def __init__(self):
        self.file_path = os.path.abspath(__file__)

    def list_data_manager_menu(self):
        menu = """
        Data Manager Menu:
        1. Load Dataset
        3. Save Dataset
        0. Exit
        """
        print(menu)

    def action(self, choice):
        if choice == 1:
            datasets = self.list_datasets()
            print("Available Datasets:")
            for idx, dataset in enumerate(datasets, start=1):
                print(f"{idx}. {dataset}")
            # access the getChoice method from the init file
            choice = getChoice(" to select a dataset (0 to exit): ")
            if choice == 0:
                return
            elif 1 <= choice <= len(datasets):
                selected_dataset = datasets[choice - 1]
                print(f"You selected dataset: {selected_dataset}")
                df = pd.read_csv(os.path.join(os.path.dirname(self.file_path), '..', 'datasets', selected_dataset))
                return df
            else:
                print("Invalid dataset selection.")

        elif choice == 2:
            print("Save Dataset action selected.")
        elif choice == 0:
            print("Exiting Data Manager Menu.")
        else:
            print("Invalid choice in Data Manager Menu.")

    def list_datasets(self):
        import os
        # datasets are inside in ../datasets/
        try:
            dataset_dir = os.path.join(os.path.dirname(self.file_path), '..', 'datasets')
            files = os.listdir(dataset_dir)
            return [f for f in files if f.endswith('.csv')]
        except FileNotFoundError:
            return []
        
        # return [f for f in os.listdir('.') if f.endswith('.csv')]

    def load_data(self):
        import pandas as pd
        self.data = pd.read_csv(self.file_path)
        return self.data
    
    def save_data(self, data, output_path):
        if data is None:
            raise ValueError("Cannot save None data. Please provide valid data.")
        
        try:
            data.to_csv(output_path, index=False)
            return True
        except (IOError, OSError, PermissionError) as e:
            raise IOError(f"Failed to save data to {output_path}: {str(e)}")