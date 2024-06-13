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

import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bmi_calculator')


def get_float_input(prompt, data_type):
    """
    Requesting an input from the user.
    The data_type specifies whether the input is 'weight' or 'height'.
    """
    while True:
        print(f"Please enter your {data_type} in kilograms" if data_type == "weight" else f"Please enter your {data_type} in meters")
        print("Data should be a number")
        print(f"Example: {'73' if data_type == 'weight' else '1.85'}\n")

        data_str = input(f"Enter your {data_type} here: ")
        try:
            value = float(data_str)
            if value <= 0:
                raise ValueError(f"Please enter a positive {data_type}.")
            print("Data is valid!")
            return value
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

def update_worksheet(data, sheet_name):
    """
    Update the specified worksheet with the provided data.
    """
    print(f"Updating {sheet_name} worksheet...\n")
    worksheet = SHEET.worksheet(sheet_name)
    worksheet.append_row(data)
    print(f"{sheet_name.capitalize()} worksheet updated successfully.\n")

def calculate_bmi(weight, height):
    """
    Calculate the BMI given weight in kilograms and height in meters.
    """
    return round(weight / (height ** 2), 2)

def determine_bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 24.9 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def calculate_weight_change_needed(weight, height):
    """
    Calculate the weight change needed to fall into the normal BMI category (18.5 to 24.9).
    """
    normal_bmi_min = 18.5
    normal_bmi_max = 24.9

    min_normal_weight = normal_bmi_min * (height ** 2)
    max_normal_weight = normal_bmi_max * (height ** 2)

    if weight < min_normal_weight:
        weight_needed = min_normal_weight - weight
        print(f"You need to gain at least {round(weight_needed, 2)} kg to reach the normal BMI category.")
    elif weight > max_normal_weight:
        weight_needed = weight - max_normal_weight
        print(f"You need to lose at least {round(weight_needed, 2)} kg to reach the normal BMI category.")
    else:
        print("You are already within the normal BMI category.")        

def main():
    """
    Run all program functions
    """
    weight = get_float_input("weight", "weight")
    height = get_float_input("height", "height")

    update_worksheet([weight], "weight")
    update_worksheet([height], "height")

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi}")

    determine_bmi_category(bmi)
    calculate_weight_change_needed(weight, height)


    update_worksheet([bmi], "bmi")

if __name__ == "__main__":
    print("Welcome to the Body Mass Index calculator")
    main()
