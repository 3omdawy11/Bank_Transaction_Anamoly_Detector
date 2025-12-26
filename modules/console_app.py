from .data_manager import DataManager
from . import getChoice

class ConsoleApp:
    dataset = None
    data_manager = DataManager()
    def run(self):
        print("Console Application is running.")
    
    def stop(self):
        print("Console Application is stopping.")

    
        
        

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
        elif number == 3:
            print("Action 3 executed.")
        elif number == 4:
            print("Action 4 executed.")
        elif number == 5:
            print("Action 5 executed.")
        elif number == 6:
            print("Action 6 executed.")
        elif number == 7:
            print("Action 7 executed.")
        else:
            print("Invalid action number.")