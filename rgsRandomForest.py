# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:37:57 2016

@author: jingjing
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import cross_val_score
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
import dataGen4SlpPrd

dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT()
time = dataGen4SlpPrd.getSlpTime()
dataTrain, dataTest, labelTrain, labelTest = cross_validation.train_test_split(dataset, time, train_size =180)

regressor = RandomForestRegressor(random_state=0)
#val = cross_val_score(regressor, dataset, time, cv=10)
#print val

regressor.fit(dataTrain,labelTrain)
pre_time = regressor.predict(dataTest)
print regressor.score(dataTest,labelTest)
diff = labelTest - pre_time 
print diff


#tuned_parameters = [{'n_estimators':[50,100,200,300,400,500,1000,2000,3000]}]
## cv: integer, to specify the number of folds
#clf = GridSearchCV(RandomForestRegressor(), tuned_parameters, cv=5)
#clf.fit(dataset,time)
#print clf.best_params_
#print clf.best_estimator_
#print clf.best_score_
#print clf.scorer_  
#for params, mean_score, scores in clf.grid_scores_:
#    print("%0.2f (+/-%0.02f) for %r"% (mean_score, scores.std()*2, params))
#    