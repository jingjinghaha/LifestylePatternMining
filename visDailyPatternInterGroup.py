# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:08:48 2016

@author: wu34
"""

import numpy as np
import utilise 
import buildItemIndex
import infoRetrival
import matplotlib.pyplot as plt

Domain = ['DietItem','ActItem']
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
labelsActItem = np.array([2, 3, 1, 1, 0, 0, 2, 2, 2, 2, 3, 3, 1, 3, 2, 0, 0, 2, 2, 3, 0, 2, 1, 3, 2, 2, 0, 3, 2])
labelsDietItem = np.array([0, 2, 1, 0, 2, 3, 3, 1, 1, 3, 3, 2, 1, 1, 0, 3, 3, 3, 1, 2, 1, 1, 1, 1, 3, 1, 3, 3, 3])

def singleSubjectDailyArray(domain,subjectID):
	'''
	build daily item TF array 
	'''
	if domain == 'ActItem':
		item_dict = utilise.genActItemDict()
	elif domain == 'DietItem':
		item_dict = utilise.genDietItemDict()
	
	duration = infoRetrival.getDuration(subjectID)
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
				else:
					array[i,key] = 0.0
	
	if domain == 'DietItem':
		for i in range(duration):
			ItemIndex = buildItemIndex.build_daily_single_diet_index(subjectID,i+1)
			for key in item_dict:
				if "'"+item_dict[key]+"'" in ItemIndex:
					array[i,key] = ItemIndex["'"+item_dict[key]+"'"]
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
	if domain == 'ActItem':
		labels = labelsActItem
	if domain == 'DietItem':
		labels = labelsDietItem
	for i in range(len(available_list)):
		if available_list[i] == subjectID:
			groupID = labels[i]
	return groupID

def getMeanVec(domain):
	'''
	get the intergroup mean TF vector 
	'''
	if domain == 'ActItem':
		labels = labelsActItem
		X = utilise.genActItemTFArray()
	if domain == 'DietItem':
		labels = labelsDietItem
		X = utilise.genDietItemTFArray()
	
	dims = (4,X.shape[1])
	MeanVec = np.zeros(dims)
	
	for k in range(4):
		class_members = labels == k
		number = 0
		sumVec = np.zeros(X.shape[1])
		
		for x in X[class_members]:
			number += 1
			sumVec += x 
		
		meanVec = sumVec/number 
		meanVec.tolist()
		MeanVec[k] = meanVec
	
	return MeanVec

def visSBDailyPatternInterGroup(domain,subjectID):
	'''
	single subject inter group daily pattern view 
	'''	
	groupID = whichGroup(domain,subjectID)
	MeanVec = getMeanVec(domain)
	tf = singleSubjectDailyArray(domain,subjectID)
	dims = (4,tf.shape[0])
	s = np.zeros(dims)
	p = np.zeros(dims)
	x = range(tf.shape[0])
	
	plt.figure()
	
	for i in range(4):
		for j in range(tf.shape[0]):
			s[i][j] = 1/np.sqrt(sum(np.power(tf[j] - MeanVec[i], 2)))
			# print i,j,tf[j],MeanVec[i],s[i][j]
	
	for i in range(4):
		for j in range(tf.shape[0]):
			p[i][j] = ((s[i][j])/(s[0][j]+s[1][j]+s[2][j]+s[3][j]))*100
		plt.plot(x,p[i])
		plt.text(x[-1],p[i][-1],i)
	
	plt.title(domain+'_'+subjectID+'_'+str(groupID)+'_InterGroupDailyPattern')
	plt.savefig('visDaily'+domain+'PatternInterGroup/daily'+domain+'Pattern_'+subjectID)

for domain in Domain:
	for subjectID in available_list:
		visSBDailyPatternInterGroup(domain,subjectID)

# visSBDailyPatternInterGroup('DietItem','039')