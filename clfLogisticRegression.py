# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:32:00 2016

@author: jingjing
"""
from sklearn.cross_validation import cross_val_score 
from sklearn.linear_model import LogisticRegression  
from sklearn import cross_validation
import dataGen4SlpPrd 
import utilise 
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
import pandas as pd



label1 = dataGen4SlpPrd.getSlpTimeLabel()
label2 = dataGen4SlpPrd.getMorningnessLabel()
label3 = dataGen4SlpPrd.getEveningnessLabel()
label4 = dataGen4SlpPrd.getLarkLabel()
label5 = dataGen4SlpPrd.getOwlLabel()
Labels = [label1,label2,label3,label4,label5]


dataset1 = dataGen4SlpPrd.genDailyDietTypeFeatureTable4DC()
dataset2 = dataGen4SlpPrd.genDailyActTypeFeatureTable4DC()
dataset = utilise.genCombiArray(dataset1,dataset2)
dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, label5, train_size =180, random_state=10)
clf = LogisticRegression()
clf.fit(dataTrain,labelTrain)
pre_labels = clf.predict(dataTest)
accuracy = accuracy_score(labelTest,pre_labels)
print accuracy
p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
print p,r,f,s
