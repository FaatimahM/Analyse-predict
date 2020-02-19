def word_splitter(df):
    """
    Splits the sentences in a dataframe's column into a list of the separate words. 
    The created lists should be placed in a column named 'Split Tweets' in the original dataframe.

    parameters
    ----------
    df: Dataframe
        It should take a pandas dataframe as an input.

    Returns
    -------
    df: DataFrame
        The function should return the modified dataframe.
    """

    df['Split Tweets'] = df['Tweets'].str.lower().str.split()
    return df