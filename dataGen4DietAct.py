# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:13:17 2016

@author: jingjing
"""

from nltk import wordpunct_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
import buildItemIndex
import buildTypeIndex 
import numpy as np
import dietActInfoRetrv


available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

'''
return all diet item in dictionary format {1:item1, 2:item2, ... n:itemn}
'''
def genDietItemDict():
    item_dict = {}
    n = 0
    for line in open('diet/dietOverallItemFreq/all_diet_frequency.txt','r'):
        line = line.strip('\n')
        words = wordpunct_tokenize(line)
        item_dict[n] = words[0]
        n += 1
    # print item_dict
    return item_dict

'''
return all diet type in dictionary format {1:type1, 2:type2, ... n:typen}
'''
def genDietTypeDict():
    item_dict = {}
    n = 0
    for line in open('diet/dietOverallTypeFreq/all_dietType_frequency.txt','r'):
        line = line.strip('\n')
        words = wordpunct_tokenize(line)
        item_dict[n] = words[0]
        n += 1
    # print item_dict
    return item_dict

'''
return all activity item in dictionary format {1:item1, 2:item2, ... n:itemn}
'''
def genActItemDict():
    item_dict = {}
    n = 0
    for line in open('activity/activityOverallItemFreq/all_activity_frequency.txt','r'):
        line = line.strip('\n')
        words = wordpunct_tokenize(line)
        item_dict[n] = words[0]
        n += 1
    # print item_dict
    return item_dict

'''
return all activity type in dictionary format {1:type1, 2:type2, ... n:typen}
'''
def genActTypeDict():
    item_dict = {}
    n = 0
    for line in open('activity/activityOverallTypeFreq/all_activityType_frequency.txt','r'):
        line = line.strip('\n')
        words = wordpunct_tokenize(line)
        item_dict[n] = words[0]
        n += 1
    # print item_dict
    return item_dict

'''
generate the acitvity item TF numpy array m(number of subjects)*n(number of items)
'''
def genActItemTFArray():
    item_dict = genActItemDict()
    # print item_dict
    x = len(available_list)
    n = len(item_dict)
    dims = (x,n)
    array = np.zeros(dims)
    i = 0 
    for subjectID in available_list:
        ItemIndex = buildItemIndex.build_single_activity_index(subjectID)
        # print ItemIndex
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
        i += 1
    # print array
    return array

'''
generate the diet item TF numpy array m(number of subjects)*n(number of items)
'''
def genDietItemTFArray():
    item_dict = genDietItemDict()
    x = len(available_list)
    n = len(item_dict)
    dims = (x,n)
    array = np.zeros(dims)
    i = 0 
    for subjectID in available_list:
        ItemIndex = buildItemIndex.build_single_diet_index(subjectID)
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
        i += 1
    return array

'''
generate the diet type TF numpy array m(number of subjects)*n(number of type)
'''
def genDietTypeTFArray():
    item_dict = genDietTypeDict()
    x = len(available_list)
    n = len(item_dict)
    dims = (x,n)
    array = np.zeros(dims)
    i = 0 
    for subjectID in available_list:
        ItemIndex = buildTypeIndex.build_single_diet_index(subjectID)
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
        i += 1
    return array

'''
generate the activity type TF numpy array m(number of subjects)*n(number of type)
'''
def genActTypeTFArray():
    item_dict = genActTypeDict()
    # print item_dict
    x = len(available_list)
    n = len(item_dict)
    dims = (x,n)
    array = np.zeros(dims)
    i = 0 
    for subjectID in available_list:
        ItemIndex = buildTypeIndex.build_single_activity_index(subjectID)
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
        i += 1
    return array

'''
generate the daily diet type TF numpy array for single subject m(number of days)*n(number of type)
'''
def genDailySingleDietTypeTFArray(subjectID):
    
    item_dict = genDietTypeDict()
    duration = dietActInfoRetrv.getDuration(subjectID)
    n = len(item_dict)
    dims = (duration,n)
    array = np.zeros(dims)
    
    for i in range(duration):
        ItemIndex = buildTypeIndex.build_daily_single_diet_index(subjectID,i+1)
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
    return array

'''
generate the daily activity type TF numpy array for single subject m(number of days)*n(number of type)
'''
def genDailySingleActTypeTFArray(subjectID):
    
    item_dict = genActTypeDict()
    duration = dietActInfoRetrv.getDuration(subjectID)
    n = len(item_dict)
    dims = (duration,n)
    array = np.zeros(dims)
    
    for i in range(duration):
        ItemIndex = buildTypeIndex.build_daily_single_activity_index(subjectID,i+1)
        for key in item_dict:
            if item_dict[key] in ItemIndex: 
                # print item_dict[key]
                array[i,key] = ItemIndex[item_dict[key]]
    return array

def DietItemTfidfArray():
    counts = genDietItemTFArray()
    transformer = TfidfTransformer(norm=None)
    # transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts)
    aa = tfidf.toarray()
    return aa

def DietTypeTfidfArray():
    counts = genDietTypeTFArray()
    transformer = TfidfTransformer(norm=None)
    # transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts)
    aa = tfidf.toarray()
    return aa

def ActItemTfidfArray():
    counts = genActItemTFArray()
    # print counts
    transformer = TfidfTransformer(norm=None)
    # transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts)
    aa = tfidf.toarray()
    return aa

def ActTypeTfidfArray():
    counts = genActTypeTFArray()
    transformer = TfidfTransformer(norm=None)
    # transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts)
    aa = tfidf.toarray()
    return aa

def genDietTypeTFArrayWithSlp():
    TF = genDietTypeTFArray()
    
    x = len(sleep_list)
    n = TF.shape[1]
    array = np.zeros((x,n))
    
    cunt = 0
    for i in range(len(available_list)):
        if available_list[i] in sleep_list:
            array[cunt] = TF[i]
            cunt += 1 
    
    return array 
    

def genActTypeTFArrayWithSlp():
    TF = genActTypeTFArray()
    
    x = len(sleep_list)
    n = TF.shape[1]
    array = np.zeros((x,n))
    
    cunt = 0
    for i in range(len(available_list)):
        if available_list[i] in sleep_list:
            array[cunt] = TF[i]
            cunt += 1 
    
    return array 


#print genDailySingleActTypeTFArray('039')