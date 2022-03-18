"""
To solve this assigment, documentation from gspread.org is used
"""

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
SHEET = GSPREAD_CLIENT.open('measurements')

raw_obs = SHEET.worksheet("observation")


def start():
    """
    Ask user to type a command to start the program.
    """
    while True:
        user_execute = str(input("Please type 'Start' to run the program \n")) 

        if not user_execute == "Start":                     # Validates the user input. If input does not match requierment, printstatement launches
            print("Invalid input, please try again")
        else:                                               # If comamnd is correct, program is allowed to contuine running.
            print("Program is starting up.....")
            break


def file_attributes():
    """
    Give the user a insight of the attribute fields in the speadsheet
    """
    print("The spreadsheet containt theese attribute fields:\n")
    file_attributes = raw_obs.row_values(1)
    print(file_attributes)


def get_observation_data():
    """
    Get all the data stored in "observation"
    """
    values = raw_obs.get_all_records()
    #print(values)
    values


def copy_worksheet():
    """
    Creates a new worksheet within the spre
    
    Copy the data from the observation worksheet to the obs_valid worksheet.
    Reasoning for doing this is to keep the raw measurments intact.
    """
    SHEET.add_worksheet("obs_copy", 1, 1) # Creates a new worksheet within the spreadsheet
    print("\nCopying raw data to new worksheet...")
    
    print("Data is successfully copied!\n")


def main():
    """
    Run the program functions
    """
    start()                     # Ask user to start the program with a defined command.
    file_attributes()           # Give the user information about the file attributes in the spreadsheet.
    get_observation_data()
    copy_worksheet()

print("------------------------------------------------------------------------------------------------------------")
print("Welcome to file cleaner and validator. This program will prepear your file to import into 'program XXX'")
print("------------------------------------------------------------------------------------------------------------")
main()

#def validator_start():
#   print("Do you wish to start validation of observations in spreadseet?")
#validator_start()