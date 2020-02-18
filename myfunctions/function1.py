def dictionary_of_metrics(items):
    import numpy as np
    ave = round(np.mean(items),2)
    median = round(np.median(items),2)
    variance = round(np.var(items, ddof = 1),2)
    standard_dev = round(np.std(items, ddof = 1),2)
    mini = min(items)
    maxi = max(items)
    a= {'mean': ave,
        'median': median,
        'variance': variance,
        'standard deviation': standard_dev,
        'min': mini,
        'max': maxi}
    return a