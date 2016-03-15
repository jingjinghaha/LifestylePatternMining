# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:49:22 2016

@author: jingjing
"""

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import dataGen 
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from adasyn import ADASYN
import numpy as np


#dataset = dataGen.genDailyActTypeFeatureTable()
dataset = dataGen.genDailyDietTypeFeatureTable()
np.save('dataset.npy',dataset)

#labels = dataGen.getSlpTimeLabel()
labels = dataGen.getMorningnessLabel()
#labels = dataGen.getEveningnessLabel()
#labels = dataGen.getLarkLabel()
#labels = dataGen.getOwlLabel()
np.save('labels.npy',labels)

adsn = ADASYN(k=7,imb_threshold=0.6, ratio=0.75)
new_X, new_y = adsn.fit_transform(dataset,labels)  # your imbalanced dataset is in X,y

clf = RandomForestClassifier(n_estimators = 100,n_jobs = -1)

dataTrain = dataset[0:160,:]
labelTrain = labels[0:160]

clf.fit(dataTrain,labelTrain)

dataTest = dataset[160:,:]
labelTest = labels[160:]
pre_labels = clf.predict(dataTest)

accuracy = accuracy_score(labelTest,pre_labels)
p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)

print cross_val_score(clf, dataset, labels)

