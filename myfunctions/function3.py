def date_parser(dates):
    new_dates = []
    for i in dates:
        new_dates.append(i.split(' ')[0])
    return new_dates
