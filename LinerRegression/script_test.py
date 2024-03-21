import pandas as pd
import numpy as np

def cost_func(theta_0: int, theta_1: int, x: list, y: list):
  return np.mean(np.square(y - (theta_0 + theta_1 * x)))

def test(theta_0: int, theta_1: int, x: list, y: list):
  return np.square(y - (theta_0 + theta_1 * x))