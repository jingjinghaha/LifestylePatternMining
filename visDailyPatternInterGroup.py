# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:08:48 2016

@author: wu34
"""

import numpy as np
import utilise 
import dataGen4DietAct
import buildItemIndex
import buildTypeIndex
import dietActInfoRetrv
import matplotlib.pyplot as plt

# Domain = ['ActItem','DietItem','DietType','ActType']
Domain = ['DietType','ActType']
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

labelsDietType = utilise.string2array('1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 1 1 1')
labelsActType = utilise.string2array('1 0 1 1 0 0 2 2 2 1 2 0 1 2 1 2 0 1 1 2 0 1 1 2 1 1 0 2 1')

def singleSubjectDailyArray(domain,subjectID):
    '''
    build daily item TF array 
    '''
    if domain == 'DietType':
        item_dict = dataGen4DietAct.genDietTypeDict()
    elif domain == 'ActType':
        item_dict = dataGen4DietAct.genActTypeDict()
    # print item_dict
    
    duration = dietActInfoRetrv.getDuration(subjectID)
    x = duration 
    n = len(item_dict)
    dims = (x,n)
    array = np.zeros(dims)
    
    if domain == 'ActItem':
        for i in range(duration):
            ItemIndex = buildItemIndex.build_daily_single_activity_index(subjectID,i+1)
            for key in item_dict:
                if item_dict[key] in ItemIndex:
                    array[i,key] = ItemIndex[item_dict[key]]
                else:
                    array[i,key] = 0.0
    
    if domain == 'DietItem':
        for i in range(duration):
            ItemIndex = buildItemIndex.build_daily_single_diet_index(subjectID,i+1)
            # print ItemIndex
            for key in item_dict:
                if item_dict[key] in ItemIndex:
                    array[i,key] = ItemIndex[item_dict[key]]
                else:
                    array[i,key] = 0.0
    
    if domain == 'DietType':
        for i in range(duration):
            ItemIndex = buildTypeIndex.build_daily_single_diet_index(subjectID,i+1)
            # print ItemIndex
            for key in item_dict:
                if item_dict[key] in ItemIndex:
                    array[i,key] = ItemIndex[item_dict[key]]
                else:
                    array[i,key] = 0.0
    
    if domain == 'ActType':
        for i in range(duration):
            ItemIndex = buildTypeIndex.build_daily_single_activity_index(subjectID,i+1)
            for key in item_dict:
                if item_dict[key] in ItemIndex:
                    array[i,key] = ItemIndex[item_dict[key]]
                else:
                    array[i,key] = 0.0
    '''
    change the TF array to TFIDF array. But the DF here is not equal to the one we use for mean Vector 
    '''
    # transformer = TfidfTransformer(norm=None)
    # tfidf = transformer.fit_transform(array)
    # aa = tfidf.toarray() 
    # tfidfNorm = utilise.normArray(aa)
    
    # result = utilise.normArray(array)
    
    # print array 
    return array 

def whichGroup(domain,subjectID):
    '''
    To find which group is the subject belong to 
    '''
    if domain == 'DietType':
        labels = labelsDietType
    if domain == 'ActType':
        labels = labelsActType
    
    for i in range(len(available_list)):
        if available_list[i] == subjectID:
            groupID = labels[i]
    
    return groupID

def getMeanVec(domain):
    '''
    get the intergroup mean TF vector 
    '''

    if domain == 'DietType':
        labels = labelsDietType
        X = dataGen4DietAct.genDietTypeTFArray()
    if domain == 'ActType':
        labels = labelsActType
        X = dataGen4DietAct.genActTypeTFArray()
    
    N = np.max(labels) + 1

    dims = (N,X.shape[1])
    MeanVec = np.zeros(dims)

    for k in range(N):
        class_members = labels == k
        number = 0
        sumVec = np.zeros(X.shape[1])
        
        for x in X[class_members]:
            number += 1
            sumVec += x 
        
        meanVec = sumVec/number 
        meanVec.tolist()
        
        firstMax = np.max(meanVec)
        meanVec = meanVec/firstMax
        
        MeanVec[k] = meanVec
    
    return MeanVec

def visSBDailyPatternInterGroup(domain,subjectID):
    '''
    single subject inter group daily pattern view 
    ''' 
    groupID = whichGroup(domain,subjectID)
    MeanVec = getMeanVec(domain)
    tf = singleSubjectDailyArray(domain,subjectID)

    if domain == 'DietType':
        labels = labelsDietType
    if domain == 'ActType':
        labels = labelsActType

    N = np.max(labels) + 1 

    dims = (N,tf.shape[0])
    s = np.zeros(dims)
    p = np.zeros(dims)
    x = range(tf.shape[0])
    
    plt.figure()

    for i in range(N):
        for j in range(tf.shape[0]):
            s[i][j] = 1/np.sqrt(sum(np.power(tf[j] - MeanVec[i], 2)))
            # print i,j,tf[j],MeanVec[i],s[i][j]
    
    for i in range(N):
        for j in range(tf.shape[0]):
            p[i][j] = ((s[i][j])/np.sum(s[:,j]))*100

        plt.plot(x,p[i])
        plt.text(x[-1],p[i][-1],i)
    
    plt.title(domain+'_'+subjectID+'_'+str(groupID)+'_InterGroupDailyPattern')
    plt.xlabel('Days')
    plt.ylabel('Percentage')
    data = dietActInfoRetrv.getDaysList(subjectID)
    plt.xticks(x,data)
    plt.savefig('visInterGroupDailyPattern/'+domain+'/daily'+domain+'Pattern_'+subjectID)

def visDailyPatternInterGroup():
    for domain in Domain:
        for subjectID in available_list:
            visSBDailyPatternInterGroup(domain,subjectID)

# visSBDailyPatternInterGroup('DietItem','039')
visDailyPatternInterGroup()
