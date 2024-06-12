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


def get_weight_data():
    """
    Get the body weight figure based on the input from the user
    """

    print("Please enter your bodyweight in kilograms")
    print("Data should be one number")
    print("Example: 73\n")

    data_str = input("Enter your weight here: ")
    
    weight_data = data_str.split(",")
    validate_data(weight_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there isn't exactly 1 value.
    """
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Exactly 1 value reuired, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")        


get_weight_data()
