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

Domain = ['DietItem','ActItem','DietType','ActType','ActDietItem','ActDietType']
Metric = ['TF','TFIDF']

def string2array(str):
	temp = str.split(' ')
	for i in range(len(temp)):
		token = int(temp[i])
		temp[i] = token
	array = np.array(temp)
	return array 

def KM(domain, metric):
	if metric == 'TF':
		if domain == 'DietItem':
			X = utilise.genDietItemTFArray()
		elif domain == 'ActItem':
			X = utilise.genActItemTFArray()
		elif domain == 'DietType':
			X = utilise.genDietTypeTFArray()
		elif domain == 'ActType':
			X = utilise.genActTypeTFArray()
		elif domain == 'ActDietItem':
			X = utilise.genCombiArray(utilise.genActItemTFArray(),utilise.genDietItemTFArray())
		elif domain == 'ActDietType':
			X = utilise.genCombiArray(utilise.genActTypeTFArray(),utilise.genDietTypeTFArray())
	elif metric == 'TFIDF':
		if domain == 'DietItem':
			X = utilise.DietItemTfidfArray()
		elif domain == 'ActItem':
			X = utilise.ActItemTfidfArray()
		elif domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
		elif domain == 'ActDietItem':
			X = utilise.genCombiArray(utilise.ActItemTfidfArray(),utilise.DietItemTfidfArray())
		elif domain == 'ActDietType':
			X = utilise.genCombiArray(utilise.ActTypeTfidfArray(),utilise.DietTypeTfidfArray())
	X = utilise.normArray(X)
	
	range_n_clusters = [5]
	for n_clusters in range_n_clusters:
		# fw = open('labels_KMeans_'+domain+'_'+str(n_clusters)+'.txt','w')
		reduced_data = PCA(n_components=2).fit_transform(X)
		# print X
		# print reduced_data
		kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
		kmeans.fit(reduced_data)
		inertia = kmeans.inertia_
		print domain,metric,inertia
		labels = kmeans.labels_
		print labels
		
		if domain == 'DietItem':
			row_labels = utilise.itemDict2list(utilise.genDietItemDict())
		elif domain == 'ActItem':
			row_labels = utilise.itemDict2list(utilise.genActItemDict())
		elif domain == 'DietType':
			row_labels = utilise.itemDict2list(utilise.genDietTypeDict())
		elif domain == 'ActType':
			row_labels = utilise.itemDict2list(utilise.genActTypeDict())
		
		plt.figure()
		plt.title(domain+'_KMeans_'+str(n_clusters))
		for k in range(n_clusters):
			class_members = labels == k
			i = 0
			dims = (1,X.shape[1])
			sumVec = np.zeros(dims)
			for x in X[class_members]:
				i += 1
				sumVec += x 
			meanVec = sumVec/i 
			meanVec.tolist()
			# totalSum = np.sum(meanVec[0])
			# print totalSum
			# meanVec = meanVec/totalSum
			
			firstMax = np.max(meanVec[0])
			# print firstMax
			tempVec = np.copy(meanVec)
			for j in range(X.shape[1]):
				if tempVec[0,j] == firstMax:
					tempVec[0,j] = 0
			secondMax = np.max(tempVec[0])
			# print secondMax
			tempVec2 = np.copy(tempVec)
			for j in range(X.shape[1]):
				if tempVec2[0,j]==secondMax:
					tempVec2[0,j] = 0
			thirdMax = np.max(tempVec2[0])
			# print thirdMax

			
			x = range(X.shape[1])
			plt.plot(x,meanVec[0])
			# print meanVec[0]
			for j in range(X.shape[1]):
				# if meanVec[0,j] == firstMax:
				if meanVec[0,j] == firstMax or meanVec[0,j] == secondMax:
				# if meanVec[0,j] == firstMax or meanVec[0,j] == secondMax or meanVec[0,j] == thirdMax:
					print row_labels[j]
					print meanVec[0,j]
					plt.text(x[j],meanVec[0,j],row_labels[j])

		# print row_labels
		#plt.xlabel(row_labels)
		plt.savefig('VisClustering'+domain+'Pattern/KMeans_'+metric+'_'+str(n_clusters)+'_groupFreq')

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
		elif domain == 'ActDietItem':
			X = utilise.genCombiArray(utilise.genActItemTFArray(),utilise.genDietItemTFArray())
		elif domain == 'ActDietType':
			X = utilise.genCombiArray(utilise.genActTypeTFArray(),utilise.genDietTypeTFArray())
	elif metric == 'TFIDF':
		if domain == 'DietItem':
			X = utilise.DietItemTfidfArray()
		elif domain == 'ActItem':
			X = utilise.ActItemTfidfArray()
		elif domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
		elif domain == 'ActDietItem':
			X = utilise.genCombiArray(utilise.ActItemTfidfArray(),utilise.DietItemTfidfArray())
		elif domain == 'ActDietType':
			X = utilise.genCombiArray(utilise.ActTypeTfidfArray(),utilise.DietTypeTfidfArray())
	X = utilise.normArray(X)
	
	if domain == 'DietItem':
		row_labels = utilise.itemDict2list(utilise.genDietItemDict())
	elif domain == 'ActItem':
		row_labels = utilise.itemDict2list(utilise.genActItemDict())
	elif domain == 'DietType':
		row_labels = utilise.itemDict2list(utilise.genDietTypeDict())
	elif domain == 'ActType':
		row_labels = utilise.itemDict2list(utilise.genActTypeDict())
	elif domain == 'ActDietItem':
		row_labels = np.append(utilise.itemDict2list(utilise.genActItemDict()),utilise.itemDict2list(utilise.genDietItemDict()))
	elif domain == 'ActDietType':
		row_labels = np.append(utilise.itemDict2list(utilise.genActTypeDict()),utilise.itemDict2list(utilise.genDietTypeDict()))
	print row_labels
	
	# the labels are got based on TFIDF after PCA, which is more centralized than TF
	# if domain == 'ActItem' and n_clusters == 3:
		# labels = np.array([0, 1, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 2, 1, 0, 1, 1, 0, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 0])
	# if domain == 'DietItem' and n_clusters == 3:
		# labels = np.array([1, 1, 2, 1, 1, 0, 0, 2, 2, 0, 0, 1, 2, 2, 1, 0, 0, 0, 2, 1, 2, 2, 2, 2, 0, 2, 0, 0, 0])
	# if domain == 'DietType' and n_clusters == 3:
		# labels = np.array([0, 2, 1, 2, 0, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1])
	# if domain == 'ActType' and n_clusters == 3:
		# labels = np.array([0, 2, 0, 0, 1, 1, 1, 1, 2, 0, 1, 1, 0, 1, 2, 1, 1, 2, 0, 1, 2, 0, 0, 1, 0, 0, 1, 2, 2])
	# if domain == 'ActItem' and n_clusters == 4:
		# labels = np.array([2, 3, 1, 1, 0, 0, 2, 2, 2, 2, 3, 3, 1, 3, 2, 0, 0, 2, 2, 3, 0, 2, 1, 3, 2, 2, 0, 3, 2])
	# if domain == 'DietItem' and n_clusters == 4:
		# labels = np.array([0, 2, 1, 0, 2, 3, 3, 1, 1, 3, 3, 2, 1, 1, 0, 3, 3, 3, 1, 2, 1, 1, 1, 1, 3, 1, 3, 3, 3])
	# if domain == 'DietType' and n_clusters == 4:
		# labels = np.array([0, 3, 2, 3, 0, 3, 1, 2, 2, 1, 1, 0, 3, 2, 2, 1, 3, 3, 0, 0, 0, 2, 2, 2, 1, 2, 3, 2, 1])
	# if domain == 'ActType' and n_clusters == 4:
		# labels = np.array([1, 2, 3, 3, 2, 0, 0, 0, 2, 1, 0, 0, 1, 0, 1, 0, 2, 1, 1, 0, 2, 3, 3, 2, 3, 1, 0, 2, 1])
	# if domain == 'ActItem' and n_clusters == 5:
		# labels = np.array([1, 0, 2, 2, 0, 3, 1, 4, 1, 4, 0, 0, 2, 0, 4, 3, 1, 4, 4, 0, 3, 4, 2, 0, 4, 4, 3, 0, 1])
	# if domain == 'DietItem' and n_clusters == 5:
		# labels = np.array([0, 4, 1, 0, 4, 2, 2, 1, 1, 3, 3, 4, 1, 1, 0, 3, 2, 2, 1, 4, 1, 1, 1, 1, 2, 1, 2, 2, 2])
	# if domain == 'DietType' and n_clusters == 5:
		# labels = np.array([2, 1, 0, 1, 4, 1, 4, 0, 4, 3, 3, 2, 1, 0, 0, 3, 1, 1, 2, 2, 2, 0, 0, 4, 3, 4, 1, 4, 3])
	# if domain == 'ActType' and n_clusters == 5:
		# labels = np.array([0, 1, 2, 2, 1, 3, 4, 4, 1, 0, 3, 4, 0, 4, 0, 3, 1, 0, 0, 3, 1, 2, 2, 4, 2, 0, 3, 1, 0])
	
	# the labels are got before PCA 
	if domain == 'ActItem' and n_clusters == 4:
		labels = string2array('0 1 3 3 1 2 0 0 1 0 1 1 3 1 0 1 1 0 0 1 2 0 3 1 0 0 2 1 0')
	if domain == 'DietItem' and n_clusters == 4:
		labels = string2array('0 3 0 3 1 2 2 0 0 0 0 3 0 0 1 0 2 2 0 3 1 1 1 0 1 1 2 1 1')
	if domain == 'DietType' and n_clusters == 4:
		labels = string2array('1 3 2 3 1 1 2 2 2 0 0 1 1 2 2 0 1 1 1 1 1 2 2 2 0 2 3 2 0')
	if domain == 'ActType' and n_clusters == 4:
		labels = string2array('1 3 1 1 0 0 2 2 2 1 2 2 1 2 3 0 2 3 1 2 0 1 1 2 1 3 0 3 3')
	if domain == 'ActDietItem' and n_clusters == 4:
		labels = string2array('3 3 1 3 3 3 2 2 2 1 0 0 1 2 1 0 2 1 1 0 3 1 1 2 1 1 3 2 1')
	if domain ==  'ActDietType' and n_clusters == 4:
		labels = string2array('0 3 0 3 1 2 2 0 1 0 2 1 3 2 0 2 1 0 0 2 1 0 0 0 0 0 2 1 0')

	
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
				# print k,domain,metric,n_clusters,meanVec[j],row_labels[j]
				plt.text(x[j],meanVec[j],row_labels[j])

	# print row_labels
	# plt.xlabel(row_labels)
	plt.title(domain+'_'+metric+'_KMeans_'+str(n_clusters))
	plt.savefig('VisClustering'+domain+'Pattern/KMeans__'+metric+'_'+str(n_clusters)+'_groupFreq')


# for domain in Domain:
	# for metric in Metric:
		# KM(domain, metric)

for domain in Domain:
	for metric in Metric:
		for n_clusters in range(4,5):
			bestLabel(domain,metric,n_clusters)

# bestLabel('DietItem',4)
# KM('ActItem', 'TFIDF')
