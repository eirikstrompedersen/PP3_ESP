"""
To solve this assigment, documentation from gspread.org is used.
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


def file_attributes():
    """
    Give the user a insight of the attribute fields in the speadsheet
    """
    print("The spreadsheet containt theese attribute fields:\n")
    global file_attri  # Makes the varriable global.
    file_attri = raw_obs.row_values(1)
    print(file_attri)


def start():
    """
    Ask user to type a command to start the program.
    """
    while True:
        user_execute = str(input("\nPlease type 'Start' to run. \n"))
        """
        Validates the user input. If input does not match requierment,
        printstatement launches.
        """
        if not user_execute == "Start":
            print("Invalid input, please try again")
        else:
            """
            If comamnd is correct (aka 'Start'),
            program is allowed to contuine running.
            """
            print("\nProgram is starting up.....")
            break


def dublicate_worksheet():
    global obs_copy         # Makes the varriable global.
    """
    Dublicates 'observations" into a new worksheet called obs_copy.
    Reasoning for doing this is to keep the raw measurments intact.
    """
    print("\nDublicate 'observation' in the spreadsheet...")
    """
    Dublicates the "observation" worksheet,
    and gives the dublication
    the name "obs_copy". Indexing the
    new worksheet to index 1 in the spreadsheet.
    """
    raw_obs.duplicate(insert_sheet_index=1, new_sheet_name="obs_copy")
    print("Worksheet 'obs_copy' is created")
    obs_copy = SHEET.worksheet("obs_copy")


def delete_columns():
    """
    This function removes unwatned columns form the worksheet
    """
    print("\nFile is being cleaned, remain patient...")
    obs_copy.delete_columns(5, 6)
    obs_copy.delete_columns(9, 17)
    obs_copy.delete_columns(9, 15)
    obs_copy.delete_rows(164, 1000)

    file_attri = obs_copy.row_values(1)
    print("File is now processed, here is the remaining file attributes:")
    print(file_attri)


def main():
    """
    Run the program functions
    """
    file_attributes()
    # Give the user insight in the file attributes in the spreadsheet.
    start()
    # Ask user to start the program with a defined command.
    dublicate_worksheet()
    # Dublicates the worksheet, to save the raw measuerments.
    delete_columns()
    # Remove unwanted columns in worksheet

print("-------------------------------------------------------")
print("Welcome to file cleaner and validator.)
print("This program will \nprepear your file to import into 'program XXX'")
print("-------------------------------------------------------")
main()
