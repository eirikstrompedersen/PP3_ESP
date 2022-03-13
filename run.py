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


def file_content():
    """
    Give the user a insight of the attribute fields in the speadsheet
    """
    file_attributes = raw_obs.row_values(1)
    print("The spreadsheet containt theese attribute fields:")
    print(file_attributes)


def remove_columns():
    """
    Removes columns from spreadsheet
    """
    columns = []
    



#def field_validator():
    """
    Validate if any datafield does not contain data
    """
    
    if 


#def emtpy_fields():
    """
    Give empty data fields the "None" attribute.
    """
    





def main():
    """
    Run the program functions
    """
    file_content()
    print(raw_obs.get_all_records())




print("Welcome to file cleaner and validator. This program will prepear your file to import into 'program XXX'\n")

main()

#def validator_start():
#   print("Do you wish to start validation of observations in spreadseet?")
#validator_start()