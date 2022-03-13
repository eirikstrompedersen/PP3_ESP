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
valid = SHEET.worksheet("obs_valid")

def file_attributes():
    """
    Give the user a insight of the attribute fields in the speadsheet
    """
    print("The spreadsheet containt theese attribute fields:\n")
    file_attributes = raw_obs.row_values(1)
    print(file_attributes)

def start():
    """
    User has to input "Start" to start the operation
    """
    
    try:
        execute = str(input("\nType 'Start' here: "))
        print("Process is starting...")
    except ValueError:
        print("Invalid command")


def copy_worksheet():
    """
    Copy the data from the observation worksheet to the obs_valid worksheet.
    Reasoning for doing this is to keep the raw measurments intact.
    """
    print("\nCopying raw data to new worksheet...")
    get_all = raw_obs.get_all_values()
    get_all.append("valid")
    print("Data is successfully copied!\n")


def main():
    """
    Run the program functions
    """
    file_attributes()
    start()
    copy_worksheet()




print("Welcome to file cleaner and validator. This program will prepear your file to import into 'program XXX'\n")

main()

#def validator_start():
#   print("Do you wish to start validation of observations in spreadseet?")
#validator_start()