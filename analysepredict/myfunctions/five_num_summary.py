def five_num_summary(items):
    import numpy as np
    gauteng_arr1 = np.array([items])
    keys_arr1 = np.array(['max', 'median', 'min', 'q1', 'q3'])
    values_arr1 = np.array([np.max(gauteng_arr1), np.median(gauteng_arr1), np.min(gauteng_arr1), 
                            np.quantile(gauteng_arr1, 0.25), np.quantile(gauteng_arr1, 0.75)])
    round_arr1 = np.around(values_arr1, 2)
    five_num_dict = {}
    for keys1, values1 in zip(keys_arr1, round_arr1):
        five_num_dict[keys1] = values1
    return five_num_dict