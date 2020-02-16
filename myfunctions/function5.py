def number_of_tweets_per_day(df):
    import pandas as pd
    df['Date'] = pd.to_datetime(df['Date'])
    new_list = []
    for i in df['Date']:
        new_list.append(i.date())
    df['Date'] = new_list
    df1 = pd.DataFrame(df.groupby('Date').count())
    return df1