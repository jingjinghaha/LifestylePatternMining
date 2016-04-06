# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 11:48:23 2016

@author: wu34
"""

from sklearn.cross_validation import cross_val_score 
from sklearn.linear_model import LogisticRegression  
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
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

gender = dataGen4SlpPrd.getGender()

dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
dataset = np.c_[dataset,gender.ravel()]
#dataset = utilise.normArray(dataset)

for labels in Labels:
    bestAcc = 0
    
#    adsn = ADASYN(k=7,imb_threshold=0.6, ratio=0.8)
#    new_X, new_y = adsn.fit_transform(dataset,labels)
    
    for i in range(200):
        dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, labels, train_size =180)
        
        clf = LogisticRegression(penalty = 'l1',C=0.5)
        clf.fit(dataTrain,labelTrain)
        
        pre_labels = clf.predict(dataTest)
        # http://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
        accuracy = accuracy_score(labelTest,pre_labels)
            
        if accuracy > bestAcc:
            bestAcc = accuracy
            p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
                
        # p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
        # cross_val_score(clf, dataset, labels) 
    print bestAcc,p,r,f,s
    

#dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
#dataset = np.c_[dataset,gender.ravel()]
#
##dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, label5, train_size =180, random_state=10)
##clf = LogisticRegression()
##clf.fit(dataTrain,labelTrain)
##pre_labels = clf.predict(dataTest)
##accuracy = accuracy_score(labelTest,pre_labels)
##print accuracy
##p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
##print p,r,f,s
#
#tuned_parameters = [{'penalty':['l1','l2'],'C':[0.1,0.3,0.5,0.8,1,5,10,20,30]}]
## cv: integer, to specify the number of folds
#clf = GridSearchCV(LogisticRegression(), tuned_parameters, cv=5)
#clf.fit(dataset,label1)
#print clf.best_params_
##print clf.best_estimator_
#print clf.best_score_
##print clf.scorer_  
##for params, mean_score, scores in clf.grid_scores_:
##    print("%0.2f (+/-%0.02f) for %r"% (mean_score, scores.std()*2, params))
