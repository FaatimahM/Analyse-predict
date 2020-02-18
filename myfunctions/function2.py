def five_num_summary(items):
    import numpy as np
     maxi = max(items)
     medi = np.median(items)
     mini = min(items)
     Q1 = round(np.quantile(items, 0.25),2)
     Q3 = round(np.quantile(items, 0.75),2)
  return {'max': maxi,
          'median': medi,
          'min': mini,
          'q1': Q1,
          'q3': Q3}