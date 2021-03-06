def dictionary_of_metrics(items):
    """ 
    Takes a list(items) of numbers as an input, returns a dictionary containing the mean, median, variance, standard deviation, minimum and maximum of
    of items.   

    Parameters
    ----------
    items: a list 

    Returns
    -------
    dict_metrics: a dictionary in the format {'mean': mean of item ,
                                             'median': median of item ,
                                             'var': variance of item,
                                             'std': standard deviation of item,
                                             'min': minimum of item,
                                             'max': maximum of item}


    """
    import numpy as np
    gauteng_arr = np.array([items])
    keys_arr = np.array(['mean', 'median', 'std', 'var', 'min', 'max'])
    values_arr = np.array([np.mean(gauteng_arr), np.median(gauteng_arr), np.std(gauteng_arr, ddof = 1),
                           np.var(gauteng_arr, ddof = 1), np.min(gauteng_arr), np.max(gauteng_arr)])
    rounded_arr = np.around(values_arr, 2)
    dict_metrics = {}
    for keys, values in zip(keys_arr, rounded_arr):
        dict_metrics[keys] = values
    return dict_metrics