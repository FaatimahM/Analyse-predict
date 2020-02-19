def word_splitter(df):
    """Takes a pandas dataframe as an input, splits sentences from the 'Tweets' column and places these sentences into a new column called 
    'Split Tweets'. 
    """
    df['Split Tweets'] = df['Tweets'].str.lower().str.split()
    return df