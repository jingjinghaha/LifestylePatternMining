# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:49:22 2016

@author: jingjing
"""

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import dataGen4SlpPrd 
import utilise 
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from adasyn import ADASYN
import numpy as np
import pandas as pd


#dataset = dataGen4SlpPrd.genDailyActTypeFeatureTable()
dataset = dataGen4SlpPrd.genDailyDietTypeFeatureTable()
dataset = utilise.normArray(dataset)


label1 = dataGen4SlpPrd.getSlpTimeLabel()
label2 = dataGen4SlpPrd.getMorningnessLabel()
label3 = dataGen4SlpPrd.getEveningnessLabel()
label4 = dataGen4SlpPrd.getLarkLabel()
label5 = dataGen4SlpPrd.getOwlLabel()
Labels = [label1,label2,label3,label4,label5]
dataset_l1 = np.c_[dataset,label1.ravel()]
dataset_l2 = np.c_[dataset,label2.ravel()]
dataset_l3 = np.c_[dataset,label3.ravel()]
dataset_l4 = np.c_[dataset,label4.ravel()]
dataset_l5 = np.c_[dataset,label5.ravel()]
header = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','l']
pd.DataFrame(dataset_l1).to_csv('dataset_l1.csv',index = False,header = header)
pd.DataFrame(dataset_l2).to_csv('dataset_l2.csv',index = False,header = header)
pd.DataFrame(dataset_l3).to_csv('dataset_l3.csv',index = False,header = header)
pd.DataFrame(dataset_l4).to_csv('dataset_l4.csv',index = False,header = header)
pd.DataFrame(dataset_l5).to_csv('dataset_l5.csv',index = False,header = header)

#adsn = ADASYN(k=7,imb_threshold=0.6, ratio=0.75)
#new_X, new_y = adsn.fit_transform(dataset,labels)  # your imbalanced dataset is in X,y

#N = [120,130,140,150,160,170,180]
#N = [150]
#for labels in Labels:
#	for n in N: 
#		dataTrain = dataset[0:n,:]
#		labelTrain = labels[0:n]
#		
#		clf = RandomForestClassifier(n_estimators = 100,n_jobs = -1)
#		clf.fit(dataTrain,labelTrain)
#
#		dataTest = dataset[n:,:]
#		labelTest = labels[n:]
#		pre_labels = clf.predict(dataTest)
#
#		accuracy = accuracy_score(labelTest,pre_labels)
#		print n,accuracy 
#		p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
#
#		print cross_val_score(clf, dataset, labels)

