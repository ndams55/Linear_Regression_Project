import numpy as np
import pandas as pd
from sklearn import datasets
from numpy.core.shape_base import hstack

def get_data():
  data_url = "http://lib.stat.cmu.edu/datasets/boston"
  raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
  X = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
  y = raw_df.values[1::2, 2]
  y = y.reshape(len(y), 1)
  return X,y