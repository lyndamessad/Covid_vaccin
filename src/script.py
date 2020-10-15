
import numpy as np
import pandas as pd

from multiprocessing import Pool

import os
import gc
import json
import glob
from tqdm.notebook import tqdm

# ceci permet de repertorier les fichier existant dans le repertoire 
for dirname,_, filenames in os.walk('/home/lynda/Bureau/covid_vaccine'):
    for filename in filenames:
        print(os.path.join(dirname, filename))



"""
import lightgbm as lgb
import itertools
import time
import pprint

from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold, KFold, GroupKFold, train_test_split
from sklearn.cluster import KMeans
"""
SEEDS = 42
MAX_THRE =4
debug=True
n_candidates = 2



#ouvrir les fichiers json test et train 
train = pd.read_json('/home/lynda/Bureau/covid_vaccine/train.json', lines = True)  # 2400rows * 19columns
test = pd.read_json('/home/lynda/Bureau/covid_vaccine/test.json', lines = True)
sub = pd.read_csv("/home/lynda/Bureau/covid_vaccine/sample_submission.csv")


test_pub = test[test["seq_length"] == 107]
test_pri = test[test["seq_length"] == 130]

As = []
for id in tqdm(train["id"]):
    a = np.load(f"home/lynda/Bureau/covid_vaccine/BPPS/{id}.npy")
    As.append(a)
As = np.array(As)
As_pub = []
for id in tqdm(test_pub["id"]):
    a = np.load(f"home/lynda/Bureau/covid_vaccine/BPPS/{id}.npy")
    As_pub.append(a)
As_pub = np.array(As_pub)
As_pri = []
for id in tqdm(test_pri["id"]):
    a = np.load(f"home/lynda/Bureau/covid_vaccine/BPPS/{id}.npy")
    As_pri.append(a)
As_pri = np.array(As_pri)


