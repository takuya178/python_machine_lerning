import pandas as pd
import numpy as np

def cost_func(df: pd.DataFrame):
  df_len = len(df)
  slopes = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
  results = {}
  for i in range(len(slopes)):
    x = df.iloc[i]['space']
    y = df.iloc[i]['rent']
    lms = 0
    sigma = slopes[i]
    for j in range(len(df)):
      lms += (y - (sigma * x)) ** 2
    results[f'傾き{slopes[i]}のLMS'] = lms / len(df)
  return results

def fix_cost_func(theta_0: int, theta_1: int, x: int, y: int):
  return np.mean(np.square(y - (theta_0 + theta_1 * x)))

