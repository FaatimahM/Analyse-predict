def word_splitter(df):
    df['Split Tweets'] = df['Tweets'].str.lower().str.split()
    return df