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

Domain = ['DietItem','ActItem','DietType','ActType']
Metric = ['TF','TFIDF']

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
	elif metric == 'TFIDF':
		if domain == 'DietItem':
			X = utilise.DietItemTfidfArray()
		elif domain == 'ActItem':
			X = utilise.ActItemTfidfArray()
		elif domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
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
		plt.figure()
		
		if domain == 'DietItem':
			row_labels = utilise.itemDict2list(utilise.genDietItemDict())
		elif domain == 'ActItem':
			row_labels = utilise.itemDict2list(utilise.genActItemDict())
		elif domain == 'DietType':
			row_labels = utilise.itemDict2list(utilise.genDietTypeDict())
		elif domain == 'ActType':
			row_labels = utilise.itemDict2list(utilise.genActTypeDict())
		
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
			plt.title(domain+'_KMeans_'+str(n_clusters))
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

def test(domain,metric):
	ll = ['5','20','26']

for domain in Domain:
	for metric in Metric:
		KM(domain, metric)

KM('ActItem', 'TFIDF')
