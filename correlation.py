# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:20:22 2016

@author: jingjing
"""
import dataGen4SlpPrd
import numpy as np
import pandas as pd 


cols = dataGen4SlpPrd.genDietTypeLabel()
cols.append('label')

print cols 
dataset = dataGen4SlpPrd.genDailyDietTypeFeatureTable()
label1 = dataGen4SlpPrd.getSlpTimeLabel()

dataset_l1 = np.c_[dataset,label1.ravel()]
df = pd.DataFrame(dataset_l1,columns=cols)
print df.corr()


cols = dataGen4SlpPrd.genActTypeLabel()
cols.append('label')

print cols 
dataset = dataGen4SlpPrd.genDailyActTypeFeatureTable()
label1 = dataGen4SlpPrd.getSlpTimeLabel()

dataset_l1 = np.c_[dataset,label1.ravel()]
df = pd.DataFrame(dataset_l1,columns=cols)
print df.corr()
