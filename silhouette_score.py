# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:00:43 2015

@author: wu34
"""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np 
import slpInfoRetrv
import utilise

Domain = ['DietType','ActType']
Metric = ['TF','TFIDF']

def string2array(str):
	temp = str.split(' ')
	for i in range(len(temp)):
		token = int(temp[i])
		temp[i] = token
	array = np.array(temp)
	return array 

def sihouetteScore(domain,metric):
	if metric == 'TF':
		if domain == 'DietType':
			X = utilise.genDietTypeTFArray()
		elif domain == 'ActType':
			X = utilise.genActTypeTFArray()
	elif metric == 'TFIDF':
		if domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
	X = utilise.normArray(X)
	
	range_n_clusters = [2, 3, 4, 5, 6] 

	for n_clusters in range_n_clusters:

		if metric == 'TF':
			# the labels are got from KMeans based on TF without PCA
			if domain == 'DietType' and n_clusters == 2:
				labels = string2array('1 0 1 0 1 0 0 1 1 0 0 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 0 0 0')
			if domain == 'ActType' and n_clusters == 2:
				labels = string2array('1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 1')
			if domain == 'DietType' and n_clusters == 3:
				labels = string2array('0 2 1 2 1 0 2 1 0 2 0 0 0 1 1 1 0 0 0 2 1 1 1 1 2 1 2 2 2')
			if domain == 'ActType' and n_clusters == 3:
				labels = string2array('0 2 0 0 1 1 1 1 2 0 1 1 0 1 2 1 1 2 0 1 2 0 0 1 0 2 1 2 2')
			if domain == 'DietType' and n_clusters == 4:
				labels = string2array('1 3 2 0 0 1 3 2 1 0 1 1 1 2 2 0 1 1 1 3 2 2 2 2 0 2 3 3 0')
			if domain == 'ActType' and n_clusters == 4:
				labels = string2array('1 0 1 1 0 2 2 2 0 1 2 2 1 2 3 2 0 3 1 2 0 1 1 0 1 3 2 3 3')
			if domain == 'DietType' and n_clusters == 5:
				labels = string2array('1 4 3 0 2 1 4 3 1 2 1 1 1 3 3 2 1 1 1 4 3 3 3 3 2 3 4 4 2')
			if domain == 'ActType' and n_clusters == 5:
				labels = string2array('1 4 1 1 2 2 3 3 4 1 3 2 1 3 0 3 4 0 1 3 4 1 1 3 1 0 2 0 0')
			if domain == 'DietType' and n_clusters == 6:
				labels = string2array('1 5 2 4 0 1 5 2 3 0 3 1 3 2 2 0 1 1 3 1 2 2 2 2 0 3 5 5 0')
			if domain == 'ActType' and n_clusters == 6:
				labels = string2array('1 0 1 4 2 2 3 3 0 1 3 2 1 3 5 3 0 5 1 3 0 1 1 3 1 5 2 5 5')
		elif metric == 'TFIDF':
			# # the labels are got from KMeans based on TFIDF without PCA
			# if domain == 'DietType' and n_clusters == 2:
				# labels = string2array('1 1 0 1 1 1 0 0 0 0 0 1 1 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0')
			# if domain == 'ActType' and n_clusters == 2:
				# labels = string2array('1 1 1 1 0 0 0 0 0 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 1')
			# if domain == 'DietType' and n_clusters == 3:
				# labels = string2array('1 0 2 0 1 1 0 2 2 0 0 1 0 2 2 2 1 0 1 1 1 2 2 2 2 2 0 2 2')
			# if domain == 'ActType' and n_clusters == 3:
				# labels = string2array('2 0 2 2 1 1 1 1 1 2 1 1 2 1 0 1 1 0 2 1 1 2 2 1 2 0 1 0 0')
			# if domain == 'DietType' and n_clusters == 4:
				# labels = string2array('2 0 1 0 1 2 0 1 1 3 3 2 1 1 1 1 0 0 1 2 2 1 1 1 3 1 0 3 3')
			# if domain == 'ActType' and n_clusters == 4:
				# labels = string2array('2 3 2 2 1 1 1 1 3 2 1 1 0 1 0 1 3 0 2 1 3 2 2 1 2 2 1 0 0')
			# if domain == 'DietType' and n_clusters == 5:
				# labels = string2array('4 3 0 3 4 4 2 0 2 1 2 4 2 0 0 1 2 2 2 4 4 0 0 0 1 2 3 2 1')
			# if domain == 'ActType' and n_clusters == 5:
				# labels = string2array('4 4 2 1 0 0 3 3 3 2 3 3 1 3 4 0 3 4 2 3 0 2 2 3 2 4 0 4 4')
			# if domain == 'DietType' and n_clusters == 6:
				# labels = string2array('4 3 0 3 4 4 2 0 2 1 2 4 2 0 0 1 2 2 2 4 4 0 0 0 1 2 3 2 1')
			# if domain == 'ActType' and n_clusters == 6:
				# labels = string2array('4 4 2 1 0 0 3 3 3 2 3 3 1 3 4 0 3 4 2 3 0 2 2 3 2 4 0 4 4')
			pass 
		
		# The silhouette_score gives the average value for all the samples.
		# This gives a perspective into the density and separation of the formed clusters
		silhouette_avg = silhouette_score(X, labels)
		print(domain, 'For n_clusters =', n_clusters,
			  'The average silhouette_score is :', silhouette_avg)

for domain in Domain:
	sihouetteScore(domain,'TF')
