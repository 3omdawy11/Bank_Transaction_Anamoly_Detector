from modules import ConsoleApp
from modules import getChoice
if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
    while True:
        try:
            user_input = getChoice("(0 to exit): ")
            result = app.action(user_input)
            if result == 0:
                break
        except ValueError:
            print("Please enter a valid integer.")