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

#dataset = dataGen.genDailyActTypeFeatureTable()
dataset = dataGen.genDailyDietTypeFeatureTable()

labels = dataGen.getMorningnessLabel()
#labels = dataGen.getEveningnessLabel()
#labels = dataGen.getLarkLabel()
#labels = dataGen.getOwlLabel()

clf = RandomForestClassifier(n_estimators = 100,n_jobs = -1)

data1 = dataset[0:160,:]
label1 = labels[0:160]

clf.fit(data1,label1)

data2 = dataset[160:,:]
label2 = labels[160:]
pre_labels = clf.predict(data2)

accuracy = accuracy_score(label2,pre_labels)
p,r,f,s = precision_recall_fscore_support(label2,pre_labels)

print cross_val_score(clf, dataset, labels)

