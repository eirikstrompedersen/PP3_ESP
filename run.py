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

        if not user_execute == "Start":                     # Validates the user input. If input does not match requierment, printstatement launches.
            print("Invalid input, please try again")
        else:                                               # If comamnd is correct (aka 'Start'), program is allowed to contuine running.
            print("Program is starting up.....")
            break


def file_attributes():
    """
    Give the user a insight of the attribute fields in the speadsheet
    """
    print("The spreadsheet containt theese attribute fields:\n")
    file_attributes = raw_obs.row_values(1)
    print(file_attributes)


def dublicate_worksheet():
    """
    Dublicates 'observations" into a new worksheet called obs_copy.
    Reasoning for doing this is to keep the raw measurments intact.
    """
    print("Dublicate 'observation' in the spreadsheet...")
    raw_obs.duplicate(insert_sheet_index=1, new_sheet_name="obs_copy") # Dublicates the "observation" worksheet, and gives the dublication the name "obs_copy". Indexing the new worksheet to index 1.
    print("Worksheet 'obs_copy' is created")
    obs_copy = SHEET.worksheet("obs_copy")


def main():
    """
    Run the program functions
    """
    start()                     # Ask user to start the program with a defined command.
    dublicate_worksheet()
    file_attributes()           # Give the user information about the file attributes in the spreadsheet.


print("-------------------------------------------------------")
print("Welcome to file cleaner and validator. This program will \nprepear your file to import into 'program XXX'")
print("-------------------------------------------------------")
main()
