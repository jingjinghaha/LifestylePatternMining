# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:49:22 2016
@author: jingjing
"""

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
import dataGen4SlpPrd 
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from adasyn import ADASYN
import numpy as np
import pandas as pd
import artificialDataGenerator
import newDataProcess

'''
grid search for parameters 
'''
#dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
#dataset = np.c_[dataset,gender.ravel()]
#
##dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, label1, train_size =180, random_state=0)
##clf = RandomForestClassifier(n_estimators = 200,n_jobs = -1)
##clf.fit(dataTrain,labelTrain)
##pre_labels = clf.predict(dataTest)
##accuracy = accuracy_score(labelTest,pre_labels)
##print accuracy
##p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
##print p,r,f,s
##print clf.feature_importances_  
#
#dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, label1, train_size =180, random_state=0)
#tuned_parameters = [{'n_estimators':[50,100,200,300,400,500],'criterion':['gini','entropy']}]
## cv: integer, to specify the number of folds
#clf = GridSearchCV(RandomForestClassifier(), tuned_parameters, cv=5)
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
#label1 = dataGen4SlpPrd.getSlpTimeLabel()
#label2 = dataGen4SlpPrd.getMorningnessLabel()
#label3 = dataGen4SlpPrd.getEveningnessLabel()
#label4 = dataGen4SlpPrd.getLarkLabel()
#label5 = dataGen4SlpPrd.getOwlLabel()
#Labels = [label1]#,label2,label3,label4,label5]
#
##dataset_l1 = np.c_[dataset,label1.ravel()]
##dataset_l2 = np.c_[dataset,label2.ravel()]
##dataset_l3 = np.c_[dataset,label3.ravel()]
##dataset_l4 = np.c_[dataset,label4.ravel()]
##dataset_l5 = np.c_[dataset,label5.ravel()]
##
##header = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','l']
##
##pd.DataFrame(dataset_l1).to_csv('dataset_l1.csv',index = False,header = header)
##pd.DataFrame(dataset_l2).to_csv('dataset_l2.csv',index = False,header = header)
##pd.DataFrame(dataset_l3).to_csv('dataset_l3.csv',index = False,header = header)
##pd.DataFrame(dataset_l4).to_csv('dataset_l4.csv',index = False,header = header)
##pd.DataFrame(dataset_l5).to_csv('dataset_l5.csv',index = False,header = header)
#
##adsn = ADASYN(k=7,imb_threshold=0.6, ratio=0.8)
##new_X, new_y = adsn.fit_transform(dataset,label2)  # your imbalanced dataset is in X,y
#
#time = dataGen4SlpPrd.getSlpTime()
#gender = dataGen4SlpPrd.getGender()
#age = dataGen4SlpPrd.getAge()
#BMI = dataGen4SlpPrd.getBMI()
#percFat = dataGen4SlpPrd.getPercFat()
#
##dataset1 = dataGen4SlpPrd.genDailyDietActTypeFeaT()
##dataset3 = dataGen4SlpPrd.genDailyDietActTypeFeaTWithP()
##dataset4 = dataGen4SlpPrd.genDailyDietActTypeFeaT4DCWithP()
#
#dataset1 = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
#dataset2 = np.c_[dataset1,gender.ravel()]
#dataset3 = np.c_[dataset2,age.ravel()]
#dataset4 = np.c_[dataset3,BMI.ravel()]
#dataset5 = np.c_[dataset4,percFat.ravel()]
#dataset6 = dataGen4SlpPrd.genDailyDietActTypeFeaTWithP() 
#dataset7 = dataGen4SlpPrd.genDailyDietActTypeFeaT4DCWithP()
#dataset8 = np.c_[dataset7,gender.ravel()]
#dataset9 = np.c_[dataset8,age.ravel()]
#dataset10 = np.c_[dataset9,BMI.ravel()]
#dataset11 = np.c_[dataset10,percFat.ravel()]
#Dataset = [dataset8,dataset9,dataset10,dataset11]
#
#for labels in Labels:
#    
#    print 'change label'
#    for dataset in Dataset:
#        
#        bestAcc = 0
#        
#        for i in range(500):
#            dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, labels, train_size =180)
#            
#            clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1)
#            clf.fit(dataTrain,labelTrain)
#            
#            pre_labels = clf.predict(dataTest)
#            # http://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
#            accuracy = accuracy_score(labelTest,pre_labels)
#            
#            scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#            accuracy = scores.mean()
#            
#            if accuracy > bestAcc:
#                bestAcc = accuracy
#                #p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
#                    
#            # p,r,f,s = precision_recall_fscore_support(labelTest,pre_labels)
#            # cross_val_score(clf, dataset, labels) 
#        print bestAcc#,p,r,f,s

'''
original data test 
'''
df = artificialDataGenerator.originalData()
temp_df = df[['compositeP','others','alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy','gender']]
dataset = temp_df.as_matrix()
labels = list(df['label'])
clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1)
scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
accuracy = scores.mean()
print accuracy
clf.fit(dataset,labels)
print clf.feature_importances_

'''
original data test pattern features
'''
df = artificialDataGenerator.originalData()
df['bikeWork'] = 0
df['walkCar'] = 0
df['dairyWork'] = 0
df['fruitSnack'] = 0
for j in range(df.shape[0]): 
    if df['transportation3'][j] > 0 and df['workStudy'][j] > 0:
        df.set_value(j,'bikeWork',1)   
    if df['transportation1'][j] > 0 and df['transportation2'][j] > 0:
        df.set_value(j,'walkCar',1)
    if df['dairyP'][j] > 0 and df['workStudy'][j] > 0:
        df.set_value(j,'dairyWork',1) 
    if df['fruitP'][j] > 0 and df['snack'][j] > 0:
        df.set_value(j,'fruitSnack',1)
temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork','walkCar','fruitSnack']]
for i in temp_df.columns:
    for j in range(temp_df.shape[0]):
        if temp_df[i][j] > 1:
            temp_df.set_value(j,i,1)
dataset = temp_df.as_matrix()
labels = list(df['label'])
clf = DecisionTreeClassifier(criterion='entropy')
scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
accuracy = scores.mean()
print accuracy
clf.fit(dataset,labels)
print clf.feature_importances_

#temp_df = df[['seafood']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#temp_df = df[['bikeWork','eggP']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#temp_df = df[['bikeWork','eggP','seafood']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#temp_df = df[['alcoholD','gender','eggP','seafood']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#
#temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork','walkCar']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
#
#temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork','walkCar','fruitWork']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = DecisionTreeClassifier(criterion='entropy')
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_

'''
artificial data test 
'''
#df = artificialDataGenerator.artificialData()
#temp_df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy','gender']]
#dataset = df.as_matrix()
#labels = list(df['label'])
#clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1)
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_

'''
artificial data test pattern features 
'''
#df = artificialDataGenerator.artificialData()
#df['bikeWork'] = 0
#df['walkCar'] = 0
#for j in range(df.shape[0]): 
#    if df['transportation3'][j] > 0 and df['workStudy'][j] > 0:
#        df.set_value(j,'bikeWork',1)   
#    if df['transportation1'][j] > 0 and df['transportation2'][j] > 0:
#        df.set_value(j,'walkCar',1)
#temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork','walkCar']]
##temp_df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = df.as_matrix()
#labels = list(df['label'])
#clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1)
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_


'''
new data test 
'''
#df = newDataProcess.newFeatureFrame()
#temp_df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender']]
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1) 
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_

'''
new data test pattern test 
'''
#df = newDataProcess.newFeatureFrame()
#df['bikeWork'] = 0
#df['walkCar'] = 0
#for j in range(df.shape[0]): 
#    if df['bike'][j] > 0 and df['workStudy'][j] > 0:
#        df.set_value(j,'bikeWork',1)   
#    if df['walk'][j] > 0 and df['car'][j] > 0:
#        df.set_value(j,'walkCar',1)
##temp_df = df[['alcoholD','eggP','seafood','gender','bikeWork','walkCar']]
#temp_df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy']]
#for i in temp_df.columns:
#    for j in range(temp_df.shape[0]):
#        if temp_df[i][j] > 1:
#            temp_df.set_value(j,i,1)
#dataset = temp_df.as_matrix()
#labels = list(df['label'])
#clf = RandomForestClassifier(n_estimators = 50,criterion='gini',n_jobs = -1) 
#scores = cross_validation.cross_val_score(clf, dataset, labels, cv=5)
#accuracy = scores.mean()
#print accuracy
#clf.fit(dataset,labels)
#print clf.feature_importances_
