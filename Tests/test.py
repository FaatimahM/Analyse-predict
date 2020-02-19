from analysepredict import date_parser
from analysepredict import dict_metrics
from analysepredict import extrct_hashtags
from analysepredict import five_num_summary
from analysepredict import number_of_tweets
from analysepredict import word_split
from analysepredict import words_remover
import pandas as pd
import numpy as np
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

twitter_url = 'https://raw.githubusercontent.comExplore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv('Twitter.csv',usecols=['Tweets','Date'])
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

def dictionary_of_metrics(items):
    '''
    Testing the function of metric dictionary
    '''
    assert myfunctions.dict_metrics(gauteng) == {'mean': 26244.42, 
    'median': 24403.5,'std': 10400.01,'var': 108160153.17,
    'min': 8842.0,'max': 39660.0}, 'incorrect'

def five_num_summary(items):
    '''
    Testing the function of five number summary
    '''
    assert myfunctions.five_num_summary(gauteng) == {'max': 39660.0,
    'median': 24403.5,'min': 8842.0,'q1': 18653.0,
    'q3': 36372.0}, 'incorrect'

def date_parser(dates):
    '''
    Testing the function of date parser
    ''' 
    assert myfunctions.date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
    assert myfunctions.date_parser(dates[-3:]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'

def extract_municipality_hashtags(df):
    '''
    Testing the function of municipality & hashtag Detector
    ''' 
    assert myfunctions.extrct_hashtags(twitter_df.copy()).loc[4,'hashtags'] == ['#eskomfreestate', '#mediastatement'], 'incorrect'

def number_of_tweets_per_day(df):
    '''
    Testing the function of number of tweets per day
    ''' 


def word_splitter(df):
    '''
    Testing the function of word splitter
    ''' 
    assert myfunctions.word_split(twitter_df.copy()).loc[0,'Split Tweets'] == ['@bongadlulane',
    'please','send','an','email','to','mediadesk@eskom.co.za'], 'incorrect'

def stop_words_remover(df):
    '''
    Testing the function of stop words
    '''
    assert myfunctions.words_remover(twitter_df.copy()).loc[0,'Without Stop Words'] == ['@bongadlulane', 
    'send', 'email', 'mediadesk@eskom.co.za'], 'incorrect'

