
#def validator():
    """
    This function cheks if the spreadsheet is valid. To determind if the spreadsheet is valid, 
    the function will check after a set of values in the spreadsheet. If all values are included, the spreadsheet 
    is accepted as valid
    """


#def remove():
    """
    This function removes unwatned data from the worksheet,
    and copies the wanted data to a new worksheet.
    """
    value_list = raw_obs.col_values(1)
    print(value_list)



#def get_observation_data():
    """
    Get all the data stored in "observation"
    """
    values = raw_obs.get_all_records()
    values.append(obs_copy)
