# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:48:39 2016

@author: wu34
"""

import numpy as np
import utilise 
import dataGen4DietAct
import buildItemIndex
import dietActInfoRetrv
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer

Domain = ['DietItem','ActItem']
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
labelsActItem = np.array([2, 3, 1, 1, 0, 0, 2, 2, 2, 2, 3, 3, 1, 3, 2, 0, 0, 2, 2, 3, 0, 2, 1, 3, 2, 2, 0, 3, 2])
labelsDietItem = np.array([0, 2, 1, 0, 2, 3, 3, 1, 1, 3, 3, 2, 1, 1, 0, 3, 3, 3, 1, 2, 1, 1, 1, 1, 3, 1, 3, 3, 3])

def singleSubjectDailyArray(domain,subjectID):
	'''
	build daily item TFIDF normalization array 
	'''
	if domain == 'ActItem':
		item_dict = dataGen4DietAct.genActItemDict()
	elif domain == 'DietItem':
		item_dict = dataGen4DietAct.genDietItemDict()
	
	duration = dietActInfoRetrv.getDuration(subjectID)
	x = duration 
	n = len(item_dict)
	dims = (x,n)
	array = np.zeros(dims)
	
	if domain == 'ActItem':
		for i in range(duration):
			ItemIndex = buildItemIndex.build_daily_single_activity_index(subjectID,i+1)
			for key in item_dict:
				if "'"+item_dict[key]+"'" in ItemIndex:
					array[i,key] = ItemIndex["'"+item_dict[key]+"'"]
	if domain == 'DietItem':
		for i in range(duration):
			ItemIndex = buildItemIndex.build_daily_single_diet_index(subjectID,i+1)
			for key in item_dict:
				if "'"+item_dict[key]+"'" in ItemIndex:
					array[i,key] = ItemIndex["'"+item_dict[key]+"'"]
	
	transformer = TfidfTransformer(norm=None)
	tfidf = transformer.fit_transform(array)
	aa = tfidf.toarray() 
	tfidfNorm = utilise.normArray(aa)
	print tfidfNorm.shape 
	return tfidfNorm 

def whichGroup(domain,subjectID):
	if domain == 'ActItem':
		labels = labelsActItem
	if domain == 'DietItem':
		labels = labelsDietItem
	for i in range(len(available_list)):
		if available_list[i] == subjectID:
			groupID = labels[i]
	return groupID

def getMeanVec(domain,groupID):
	if domain == 'ActItem':
		labels = labelsActItem
		X = dataGen4DietAct.ActItemTfidfArray()
	if domain == 'DietItem':
		labels = labelsDietItem
		X = dataGen4DietAct.DietItemTfidfArray()
	for k in range(4):
		class_members = labels == k
		i = 0
		sumVec = np.zeros(X.shape[1])
		for x in X[class_members]:
			i += 1
			sumVec += x 
		meanVec = sumVec/i 
		meanVec.tolist()
	return meanVec
	
def visSBDailyPattern(domain,subjectID):
	groupID = whichGroup(domain,subjectID)
	meanVec = getMeanVec(domain,groupID)
	tfidf = singleSubjectDailyArray(domain,subjectID)
	y = np.zeros(tfidf.shape[0])
	x = range(tfidf.shape[0])
	for i in range(tfidf.shape[0]):
		y[i] = 1/(np.sqrt(sum(np.power(tfidf[i] - meanVec, 2)))+1)
	plt.figure()
	plt.title(domain+'_'+subjectID+'_dailyPattern')
	plt.plot(x,y)
	plt.savefig('visDaily'+domain+'Pattern/daily'+domain+'Pattern_'+subjectID)

for domain in Domain:
	for subjectID in available_list:
		visSBDailyPattern(domain,subjectID)
