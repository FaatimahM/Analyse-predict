def date_parser(dates):
    """Takes an input of a list of datetime strings(dates) and returns a list of the date only in `'yyyy-mm-dd'` format."""
    # Create a list: new_dates
    new_dates = []
    for i in dates:
        # return a list of the date only in 'yyyy-mm-dd' format
        new_dates.append(i.split(' ')[0])
    return new_dates
