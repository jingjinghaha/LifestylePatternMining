# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:48:39 2016

@author: wu34
"""

import numpy as np
import utilise 
import buildItemIndex
import buildTypeIndex
import infoRetrival
import matplotlib.pyplot as plt

def string2array(str):
	temp = str.split(' ')
	for i in range(len(temp)):
		token = int(temp[i])
		temp[i] = token
	array = np.array(temp)
	return array 

Domain = ['ActItem','DietItem','DietType','ActType']
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
labelsActItem = string2array('3 3 2 2 3 3 0 0 0 0 1 1 2 1 0 1 3 0 0 1 3 0 2 1 0 0 3 1 0')
labelsDietItem = string2array('2 3 2 0 2 1 1 2 2 1 1 2 1 2 3 1 1 1 2 2 2 2 2 2 3 2 1 3 1')
labelsDietType = string2array('1 2 3 2 3 1 1 3 1 0 1 1 1 3 3 0 1 1 1 1 1 3 3 3 0 3 2 1 0')
labelsActType = string2array('1 1 2 2 3 3 0 0 0 2 0 0 2 0 1 3 0 1 2 0 3 2 2 0 2 1 3 1 1')

def singleSubjectDailyArray(domain,subjectID):
	'''
	build daily item TF array 
	'''
	if domain == 'ActItem':
		item_dict = utilise.genActItemDict()
	elif domain == 'DietItem':
		item_dict = utilise.genDietItemDict()
	elif domain == 'DietType':
		item_dict = utilise.genDietTypeDict()
	elif domain == 'ActType':
		item_dict = utilise.genActTypeDict()
	# print item_dict
	
	duration = infoRetrival.getDuration(subjectID)
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
	if domain == 'ActItem':
		labels = labelsActItem
	if domain == 'DietItem':
		labels = labelsDietItem
	if domain == 'DietType':
		labels = labelsDietType
	if domain == 'ActType':
		labels = labelsActType
	
	for i in range(len(available_list)):
		if available_list[i] == subjectID:
			groupID = labels[i]
	
	return groupID

def getMeanVec(domain,groupID):
	'''
	get the intragroup mean TF vector 
	'''
	if domain == 'ActItem':
		labels = labelsActItem
		X = utilise.genActItemTFArray()
	if domain == 'DietItem':
		labels = labelsDietItem
		X = utilise.genDietItemTFArray()
	if domain == 'DietType':
		labels = labelsDietType
		X = utilise.genDietTypeTFArray()
	if domain == 'ActType':
		labels = labelsActType
		X = utilise.genActTypeTFArray()

	class_members = labels == groupID
	number = 0
	sumVec = np.zeros(X.shape[1])
	for x in X[class_members]:
		number += 1
		sumVec += x 
	meanVec = sumVec/number 
	meanVec.tolist()
	
	# firstMax = np.max(meanVec)
	# meanVec = meanVec/firstMax
	
	return meanVec
	
def visSBDailyPatternIntraGroup(domain,subjectID):
	'''
	single subject intra group daily pattern view 
	'''	
	groupID = whichGroup(domain,subjectID)
	meanVec = getMeanVec(domain,groupID)
	tf = singleSubjectDailyArray(domain,subjectID)
	y = np.zeros(tf.shape[0])
	x = range(tf.shape[0])
	
	for i in range(tf.shape[0]):
		y[i] = 1/np.sqrt(sum(np.power(tf[i] - meanVec, 2)))
		# print i,tf[i],meanVec,y[i]
	
	plt.figure()
	plt.title(domain+'_'+subjectID+'_IntraGroupDailyPattern')
	plt.plot(x,y)
	plt.savefig('visIntraGroupDailyPattern/'+domain+'/daily'+domain+'Pattern_'+subjectID)

for domain in Domain:
	for subjectID in available_list:
		visSBDailyPatternIntraGroup(domain,subjectID)

# visSBDailyPatternIntraGroup('DietItem','060')

# for subjectID in available_list:
	# aa = singleSubjectDailyArray('ActType',subjectID)
	# print aa

# aa = singleSubjectDailyArray('DietItem','039')
# print aa 
# aa = singleSubjectDailyArray('DietType','039')
# print aa 