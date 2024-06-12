import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bmi_calculator')


def get_tracker_data():
    """
    Get the trackers's figure based on the input from the user
    """

    print("Please enter your bodyweight in kilograms")
    print("Data should be six numbers, separated by commas")
    print("Example: 55,62,77,69,91,83\n")

    data_str = input("Enter your weight here: ")
    print(f"The data provided is {data_str}")

get_tracker_data()
