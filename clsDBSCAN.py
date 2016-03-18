# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:12:45 2016

@author: jingjing
"""

from sklearn.cluster import DBSCAN
import utilise

Domain = ['DietType','ActType']
for domain in Domain:

    if domain == 'DietType':
        X = utilise.genDietTypeTFArray()
    elif domain == 'ActType':
        X = utilise.genActTypeTFArray()
    X = utilise.normArray(X)

    db = DBSCAN(0.8, 1).fit(X)
    labels = db.labels_
    print db.components_
    print labels
