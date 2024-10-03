# 사전 준비

# 02
import pandas as pd;
import numpy as np;
import warnings;

warnings.filterwarnings('ignore');
# 03
X_test = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_test.csv");
X_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_X_train.csv");
y_train = pd.read_csv("./yemoonsaBigdata/datasets/Part2/penguin_y_train.csv");