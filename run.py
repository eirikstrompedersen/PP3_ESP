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

raw_obs = SHEET.worksheet('observation')




"""
Test connection with worksheet
"""
data = raw_obs.get_all_values()

print(data)





#def get_point_id():
"""
Get id for each observation in the spreadsheet
"""
#    id.get_all_values(id)
#    print(id)



#get_point_id()



#def sort_data():
"""
Sorting of data
"""