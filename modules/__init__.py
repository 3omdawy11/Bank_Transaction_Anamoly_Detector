
print("******************************")
print("Welcome to Bank Transaction Anomaly Detector")

import numpy as np
import pandas as pd


def getChoice(extraMessage=""):
    while True:
        try:
            choice = int(input("\n Select an action " + extraMessage))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


from .console_app import ConsoleApp

__all__ = ['ConsoleApp', 'getChoice', 'np', 'pd']