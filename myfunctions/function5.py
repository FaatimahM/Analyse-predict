def number_of_tweets_per_day(df):
    """Takes a pandas dataframe as an input, returns a new dataframe, grouped by day, with the number of tweets for that day."""
    import pandas as pd
    df['Date'] = pd.to_datetime(df['Date'])
    new_list = []
    for i in df['Date']:
        new_list.append(i.date())
    df['Date'] = new_list
    df1 = pd.DataFrame(df.groupby('Date').count())
    return df1