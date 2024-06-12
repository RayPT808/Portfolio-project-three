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
   while True:


       print("Please enter your bodyweight in kilograms")
       print("Data should be one number")
       print("Example: 73\n")


       data_str = input("Enter your weight in kilograms here: ")
      
       weight_data = data_str.split(",")
      


       if validate_data(weight_data):
           print("Data is valid!")
           break
  
   return weight_data






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
       return False       
  
   return True


def update_weight_worksheet(data):
   """
   Update body weight worksheet, add new row with provided value."
   """
   print("Updating weight worksheet...\n")
   weight_worksheet = SHEET.worksheet("weight")
   weight_worksheet.append_row(data)
   print("Weight worksheet updated successfully.\n")


def get_height_data():
   """
   Get the height figure in meters, based on the input from the user
   """
   while True:


       print("Please enter your height in meters")
       print("Data should be a decimal number")
       print("Example: 1.85\n")


       data_str = input("Enter your height in meters here: ")
      
       try:
           # Convert the input string to a float
        height_data = float(data_str)
        print("Data is valid!")
        return height_data
       except ValueError:
        print("Invalid data: Please enter a valid floating-point number.\n")
      
   return height_data   


def validate_data(values):
   """
   Inside the try, converts all string values into float.
   Raises ValueError if strings cannot be converted into float ,
   or if there isn't exactly 1 value.
   """
   try:
       [float(value) for value in values]
       if len(values) != 1:
           raise ValueError(
               f"Exactly 1 value reuired, you provided {len(values)}"
           )
   except ValueError as e:
       print(f"Invalid data: {e}, please try again.\n")
       return False       
  
   return True
 




def update_height_worksheet(height):
   """
   Update height worksheet, add new row with provided value."
   """
   print("Updating height worksheet...\n")
   height_worksheet = SHEET.worksheet("height")
   height_worksheet.append_row([height_data])
   print("Height worksheet updated successfully.\n")




def main():
   """
   Run all program functions
   """
weight_data = get_weight_data()
weight_data = [int(num) for num in weight_data]
update_weight_worksheet(weight_data)


height_data = get_height_data()
update_height_worksheet([height_data]) # Pass the float value in a list


if __name__ == "__main__":
 print("Welcome to the Body Mass Index calculator")
main()

