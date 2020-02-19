def five_num_summary(items):
    # 4 white spaces
    """
    Takes an input of a list of datetime strings(dates) and returns
     a list of the date only in `'yyyy-mm-dd'` format
    
    Parameters
    ----------
    items:List
          The function should take a list as input

     Return
     -------
     five_num_dict:Dictionary
                   The function should return a dict with keys 'max', 
                   'median', 'min', 'q1', and 'q3' 
                   corresponding to the maximum, 
                   median, minimum, 
                   first quartile and third quartile, respectively
    """
    import numpy as np    #import numpy
    gauteng_arr1 = np.array([items])
    keys_arr1 = np.array(['max', 'median', 'min', 'q1', 'q3'])
    values_arr1 = np.array([np.max(gauteng_arr1), np.median(gauteng_arr1), np.min(gauteng_arr1), 
                            np.quantile(gauteng_arr1, 0.25), np.quantile(gauteng_arr1, 0.75)])
    round_arr1 = np.around(values_arr1, 2) #round the array to two decimal places
    five_num_dict = {}    #initialize an empty dictionary
    for keys1, values1 in zip(keys_arr1, round_arr1):    
        five_num_dict[keys1] = values1     # 8 white spaces
    return five_num_dict    #return the five number dictionary