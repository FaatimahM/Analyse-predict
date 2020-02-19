def date_parser(dates):
    # 4 white spaces
    """
    Write a function that takes as input a list of datetime strings and returns only the date in 'yyyy-mm-dd' format

    Parameters
    ----------
    dates:String
          The function should take a list of strings as input.

    Returns
    -------
    new_dates:String
              A list of strings where each element contains the date in 'yyyy-mm-dd' format
    """

    new_dates = []    # Initialize an empty list
    for i in dates:
        # 8 white spaces
        new_dates.append(i.split(' ')[0])    # Split the date and time then only take the values in index 0
    return new_dates    #return the date('')
