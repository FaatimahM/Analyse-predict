def number_of_tweets_per_day(df):
    """
    Takes a pandas dataframe as an input, returns a new dataframe, grouped by day, with the number of tweets for that day.
   
    Parameters
    ----------
    df: Dataframe
        Takes a pandas dataframe as an input
    
    Returns
    -------
    df1: Dataframe
         Creates a new dataframe with the index called 'Date'and with a column called 'Tweets', corresponding to the date and number of 
         tweets of the original dataframe. 

    """
    import pandas as pd
    df['Date'] = pd.to_datetime(df['Date'])
    new_list = []
    for i in df['Date']:
        new_list.append(i.date())
    df['Date'] = new_list
    df1 = pd.DataFrame(df.groupby('Date').count())
    return df1