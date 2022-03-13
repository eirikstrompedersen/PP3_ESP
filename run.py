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
    print(file_attributes)

def main():
    """
    Run the program functions
    """
    file_content()



print("Welcome to file cleaner and validator")
main()

#def validator_start():
#   print("Do you wish to start validation of observations in spreadseet?")
#validator_start()