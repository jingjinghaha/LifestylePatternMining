# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 16:47:37 2016

@author: wu34
"""

from sklearn.svm import SVC
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
import dataGen4SlpPrd 
import utilise 
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
import pandas as pd
import artificialDataGenerator

'''
grid search for parameters 
'''
#dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DCWithP()
#dataset = np.c_[dataset,gender.ravel()]
#
##dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, label5, train_size =180, random_state=10)
##clf = SVC()
##clf.fit(dataTrain,labelTrain)
##pre_labels = clf.predict(dataTest)
##accuracy = accuracy_score(labelTest,pre_labels)
##print accuracy
##p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
##print p,r,f,s
#
#tuned_parameters = [{'kernel':['linear','poly','rbf','sigmoid'],'C':[0.1,0.3,0.5,0.8,1,5,10,20,30]}]
## cv: integer, to specify the number of folds
#clf = GridSearchCV(SVC(), tuned_parameters, cv=5)
#clf.fit(dataset,label1)
#print clf.best_params_
##print clf.best_estimator_
#print clf.best_score_
##print clf.scorer_  
##for params, mean_score, scores in clf.grid_scores_:
##    print("%0.2f (+/-%0.02f) for %r"% (mean_score, scores.std()*2, params))

'''
best performance on old data 
'''
label1 = dataGen4SlpPrd.getSlpTimeLabel()
label2 = dataGen4SlpPrd.getMorningnessLabel()
label3 = dataGen4SlpPrd.getEveningnessLabel()
label4 = dataGen4SlpPrd.getLarkLabel()
label5 = dataGen4SlpPrd.getOwlLabel()
Labels = [label1]#,label2,label3,label4,label5]

gender = dataGen4SlpPrd.getGender()
time = dataGen4SlpPrd.getSlpTime()

dataset1 = dataGen4SlpPrd.genDailyDietActTypeFeaT()
dataset2 = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
dataset3 = dataGen4SlpPrd.genDailyDietActTypeFeaTWithP()
dataset4 = dataGen4SlpPrd.genDailyDietActTypeFeaT4DCWithP()
dataset5 = np.c_[dataset2,gender.ravel()]
Dataset = [dataset5]#,dataset3,dataset4,dataset5]
#dataset = np.c_[dataset,gender.ravel()]
#dataset = utilise.normArray(dataset)

for labels in Labels:
    
    print 'change label'
    for dataset in Dataset:
        
        bestAcc = 0
        
        for i in range(500):
            dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, labels, train_size =180)
            
            clf = SVC(kernel='linear',C=1)
            clf.fit(dataTrain,labelTrain)
            
            pre_labels = clf.predict(dataTest)
            # http://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
            accuracy = accuracy_score(labelTest,pre_labels)
            
            scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
            accuracy = scores.mean()
            
            if accuracy > bestAcc:
                bestAcc = accuracy
                #p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
                    
            # p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
            # cross_val_score(clf, dataset, labels) 
        print bestAcc#,p,r,f,s
    

'''
artificial data test 
'''
#df,labels = artificialDataGenerator.artificialData()
#dataset = df.as_matrix()
#clf = SVC(kernel='linear',C=1)
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy


