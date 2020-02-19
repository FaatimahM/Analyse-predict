def date_parser(dates):
    """Takes an input of a list of datetime strings and returns a list of the date only in `'yyyy-mm-dd'` format."""
    new_dates = []
    for i in dates:
        new_dates.append(i.split(' ')[0])
    return new_dates
