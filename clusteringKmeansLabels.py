# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:10:18 2016

@author: wu34
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import utilise

# Domain = ['ActItem','DietItem','DietType','ActType','ActDietItem','ActDietType']
Domain = ['ActItem','DietItem','DietType','ActType']
Metric = ['TF','TFIDF']

def string2array(str):
	temp = str.split(' ')
	for i in range(len(temp)):
		token = int(temp[i])
		temp[i] = token
	array = np.array(temp)
	return array 

def bestLabel(domain,metric,n_clusters):
	if metric == 'TF':
		if domain == 'DietItem':
			X = utilise.genDietItemTFArray()
		elif domain == 'ActItem':
			X = utilise.genActItemTFArray()
		elif domain == 'DietType':
			X = utilise.genDietTypeTFArray()
		elif domain == 'ActType':
			X = utilise.genActTypeTFArray()
		# elif domain == 'ActDietItem':
			# X = utilise.genCombiArray(utilise.genActItemTFArray(),utilise.genDietItemTFArray())
		# elif domain == 'ActDietType':
			# X = utilise.genCombiArray(utilise.genActTypeTFArray(),utilise.genDietTypeTFArray())
	elif metric == 'TFIDF':
		if domain == 'DietItem':
			X = utilise.DietItemTfidfArray()
		elif domain == 'ActItem':
			X = utilise.ActItemTfidfArray()
		elif domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
		# elif domain == 'ActDietItem':
			# X = utilise.genCombiArray(utilise.ActItemTfidfArray(),utilise.DietItemTfidfArray())
		# elif domain == 'ActDietType':
			# X = utilise.genCombiArray(utilise.ActTypeTfidfArray(),utilise.DietTypeTfidfArray())
	X = utilise.normArray(X)
	
	if domain == 'DietItem':
		row_labels = utilise.itemDict2list(utilise.genDietItemDict())
	elif domain == 'ActItem':
		row_labels = utilise.itemDict2list(utilise.genActItemDict())
	elif domain == 'DietType':
		row_labels = utilise.itemDict2list(utilise.genDietTypeDict())
	elif domain == 'ActType':
		row_labels = utilise.itemDict2list(utilise.genActTypeDict())
	# elif domain == 'ActDietItem':
		# row_labels = np.append(utilise.itemDict2list(utilise.genActItemDict()),utilise.itemDict2list(utilise.genDietItemDict()))
	# elif domain == 'ActDietType':
		# row_labels = np.append(utilise.itemDict2list(utilise.genActTypeDict()),utilise.itemDict2list(utilise.genDietTypeDict()))
	# print row_labels
	
	if metric == 'TF':
		# the labels are got from KMeans based on TF without PCA
		if domain == 'ActItem' and n_clusters == 2:
			labels = string2array('1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 1')
		if domain == 'DietItem' and n_clusters == 2:
			labels = string2array('0 1 0 1 0 0 1 0 0 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 1 0 1')
		if domain == 'DietType' and n_clusters == 2:
			labels = string2array('1 1 0 1 0 1 1 0 0 1 1 0 1 0 0 0 1 1 1 0 0 0 0 0 0 0 1 0 0')
		if domain == 'ActType' and n_clusters == 2:
			labels = string2array('0 0 0 0 1 1 1 1 1 0 1 1 0 1 0 1 1 0 0 1 1 0 0 1 0 0 1 1 0')
		# if domain == 'ActDietItem' and n_clusters == 2:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 2:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 3:
			labels = string2array('2 0 1 1 0 0 2 2 2 2 0 0 1 0 2 0 0 2 2 0 0 2 1 0 2 2 0 0 2')
		if domain == 'DietItem' and n_clusters == 3:
			labels = string2array('2 0 2 0 1 0 0 2 2 2 2 2 2 2 1 2 0 0 2 1 1 1 1 2 1 2 0 1 1')
		if domain == 'DietType' and n_clusters == 3:
			labels = string2array('0 2 1 2 1 0 0 1 0 2 0 0 0 1 1 1 0 2 0 0 0 1 1 1 1 1 2 0 1')
		if domain == 'ActType' and n_clusters == 3:
			labels = string2array('2 0 2 2 1 1 1 1 0 2 1 1 2 1 0 1 1 0 2 1 0 2 2 1 2 0 1 0 0')
		# if domain == 'ActDietItem' and n_clusters == 3:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 3:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 4:
			labels = string2array('3 3 2 2 3 3 0 0 0 0 1 1 2 1 0 1 3 0 0 1 3 0 2 1 0 0 3 1 0')
		if domain == 'DietItem' and n_clusters == 4:
			labels = string2array('2 3 2 0 2 1 1 2 2 1 1 2 1 2 3 1 1 1 2 2 2 2 2 2 3 2 1 3 1')
		if domain == 'DietType' and n_clusters == 4:
			labels = string2array('1 2 3 2 3 1 1 3 1 0 1 1 1 3 3 0 1 1 1 1 1 3 3 3 0 3 2 1 0')
		if domain == 'ActType' and n_clusters == 4:
			labels = string2array('1 1 2 2 3 3 0 0 0 2 0 0 2 0 1 3 0 1 2 0 3 2 2 0 2 1 3 1 1')
		# if domain == 'ActDietItem' and n_clusters == 4:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 4:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 5:
			labels = string2array('4 3 0 0 3 3 2 2 2 2 1 1 0 1 2 1 3 2 2 1 3 2 0 1 2 2 3 1 2')
		if domain == 'DietItem' and n_clusters == 5:
			labels = string2array('4 1 3 4 3 0 2 3 3 0 0 1 1 3 1 0 2 4 3 1 3 3 3 3 0 3 2 0 0')
		if domain == 'DietType' and n_clusters == 5:
			labels = string2array('3 2 0 2 0 3 1 0 1 4 1 3 1 0 0 4 3 1 1 3 3 0 0 0 4 1 2 1 4')
		if domain == 'ActType' and n_clusters == 5:
			labels = string2array('3 0 1 1 0 4 2 2 2 3 2 2 1 2 3 4 0 3 1 2 4 1 1 2 1 3 4 0 3')
		# if domain == 'ActDietItem' and n_clusters == 5:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 5:
			# labels = string2array('')
	elif metric == 'TFIDF':
		# the labels are got from KMeans based on TFIDF without PCA
		if domain == 'ActItem' and n_clusters == 2:
			labels = string2array('1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 1')
		if domain == 'DietItem' and n_clusters == 2:
			labels = string2array('1 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 1 0 0 1 0 0 1 1')
		if domain == 'DietType' and n_clusters == 2:
			labels = string2array('1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0')
		if domain == 'ActType' and n_clusters == 2:
			labels = string2array('1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 1')
		# if domain == 'ActDietItem' and n_clusters == 2:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 2:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 3:
			labels = string2array('1 2 1 1 2 0 1 1 1 1 2 2 1 2 1 2 2 1 1 2 0 1 1 2 1 1 0 2 1')
		if domain == 'DietItem' and n_clusters == 3:
			labels = string2array('0 2 1 2 2 0 1 1 1 0 0 2 1 1 2 0 0 0 1 2 2 1 1 1 0 1 0 0 0')
		if domain == 'DietType' and n_clusters == 3:
			labels = string2array('1 0 2 0 1 1 0 2 2 0 0 1 0 2 2 2 1 0 1 1 1 2 2 2 2 2 0 2 2')
		if domain == 'ActType' and n_clusters == 3:
			labels = string2array('2 0 2 2 1 1 1 1 1 2 1 1 2 1 0 1 1 0 2 1 1 2 2 1 2 0 1 0 0')
		# if domain == 'ActDietItem' and n_clusters == 3:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 3:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 4:
			labels = string2array('2 1 0 0 1 3 2 2 2 2 1 1 0 1 2 1 2 2 2 1 3 2 0 1 2 2 3 1 2')
		if domain == 'DietItem' and n_clusters == 4:
			labels = string2array('3 0 2 3 2 3 3 2 3 3 3 0 3 2 1 3 3 3 0 0 2 2 2 2 1 3 3 1 1')
		if domain == 'DietType' and n_clusters == 4:
			labels = string2array('3 0 1 0 3 3 1 1 1 2 2 3 3 1 1 2 3 3 3 3 3 1 1 1 2 1 0 1 2')
		if domain == 'ActType' and n_clusters == 4:
			labels = string2array('1 3 1 1 0 0 2 2 2 1 2 2 1 2 3 0 2 3 1 2 0 1 1 2 1 3 0 3 3')
		# if domain == 'ActDietItem' and n_clusters == 4:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 4:
			# labels = string2array('')
		if domain == 'ActItem' and n_clusters == 5:
			labels = string2array('4 0 1 1 0 3 2 2 4 2 0 0 1 0 2 0 0 2 2 0 3 2 1 0 2 2 3 0 2')
		if domain == 'DietItem' and n_clusters == 5:
			labels = string2array('3 3 1 3 3 1 4 1 2 2 2 3 2 1 3 2 4 4 2 3 1 1 1 1 1 1 4 0 0')
		if domain == 'DietType' and n_clusters == 5:
			labels = string2array('4 3 0 3 4 4 2 0 2 1 2 4 2 0 0 1 2 2 2 4 4 0 0 0 1 2 3 2 1')
		if domain == 'ActType' and n_clusters == 5:
			labels = string2array('4 4 2 1 0 0 3 3 3 2 3 3 1 3 4 0 3 4 2 3 0 2 2 3 2 4 0 4 4')
		# if domain == 'ActDietItem' and n_clusters == 5:
			# labels = string2array('')
		# if domain ==  'ActDietType' and n_clusters == 5:
			# labels = string2array('')
	
	# print type(labels)
	plt.figure()
	
	for k in range(n_clusters):
		class_members = labels == k
		i = 0
		sumVec = np.zeros(X.shape[1])
		for x in X[class_members]:
			i += 1
			sumVec += x 
		meanVec = sumVec/i 
		meanVec.tolist()
		
		# we don't have to do normalization here, as the input X has already been normalized 
		# totalSum = np.sum(meanVec[0])
		# print totalSum
		# meanVec = meanVec/totalSum
		
		# # normalize the meanVec 
		# firstMax = np.max(meanVec)
		# meanVec = meanVec/firstMax
		
		firstMax = np.max(meanVec)
		# print firstMax
		tempVec = np.copy(meanVec)
		for j in range(X.shape[1]):
			if tempVec[j] == firstMax:
				tempVec[j] = 0
		secondMax = np.max(tempVec)
		# print secondMax
		tempVec2 = np.copy(tempVec)
		for j in range(X.shape[1]):
			if tempVec2[j]==secondMax:
				tempVec2[j] = 0
		thirdMax = np.max(tempVec2)
		# print thirdMax

		
		x = range(X.shape[1])
		plt.plot(x,meanVec)
		# print meanVec
		for j in range(X.shape[1]):
			# if meanVec[j] == firstMax:
			# if meanVec[j] == firstMax or meanVec[j] == secondMax:
			if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
				print k,domain,metric,n_clusters,meanVec[j],row_labels[j]
				plt.text(x[j],meanVec[j],row_labels[j])

	# print row_labels
	# plt.xlabel(row_labels)
	plt.title(domain+'_'+metric+'_KMeans_'+str(n_clusters))
	plt.savefig('visClustering'+domain+'Pattern/KMeans__'+metric+'_'+str(n_clusters)+'_groupFreq')


# for domain in Domain:
	# for metric in Metric:
		# KM(domain, metric)

for domain in Domain:
	for n_clusters in range(2,6):
		for metric in Metric:
			bestLabel(domain,metric,n_clusters)

# bestLabel('DietItem',4)
# KM('ActItem', 'TFIDF')
