# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 10:15:38 2016

@author: wu34
"""

import dataGen4SlpPrd
import numpy as np
import pandas as pd 
import matplotlib.pylab as plt


#cols = dataGen4SlpPrd.genDietTypeLabel()
#cols.append('gender')
#cols.append('label')
#
#print cols 
#dataset = dataGen4SlpPrd.genDailyDietTypeFeatureTable()
#gender = dataGen4SlpPrd.getGender()
#dataset = np.c_[dataset,gender.ravel()]
#label1 = dataGen4SlpPrd.getSlpTimeLabel()
#
#dataset_l1 = np.c_[dataset,label1.ravel()]
#df = pd.DataFrame(dataset_l1,columns=cols)
#print df.corr()
#plt.figure()
#plt.matshow(df.corr())
#plt.colorbar()
#
#
#
#cols = dataGen4SlpPrd.genActTypeLabel()
#cols.append('gender')
#cols.append('label')
#
#print cols 
#dataset = dataGen4SlpPrd.genDailyActTypeFeatureTable()
#gender = dataGen4SlpPrd.getGender()
#dataset = np.c_[dataset,gender.ravel()]
#label1 = dataGen4SlpPrd.getSlpTimeLabel()
#
#dataset_l1 = np.c_[dataset,label1.ravel()]
#df = pd.DataFrame(dataset_l1,columns=cols)
#print df.corr()
#plt.figure()
#plt.matshow(df.corr())
#plt.colorbar()



cols = dataGen4SlpPrd.genDietActTypeLabel()
cols.append('gender')
cols.append('label')

print cols 
dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT()

gender = dataGen4SlpPrd.getGender()
dataset = np.c_[dataset,gender.ravel()]

label1 = dataGen4SlpPrd.getSlpTimeLabel()
dataset_l1 = np.c_[dataset,label1.ravel()]

df = pd.DataFrame(dataset_l1,columns=cols)

print df.corr()
plt.figure()
plt.matshow(df.corr())
plt.colorbar()
