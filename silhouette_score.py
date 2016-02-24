# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:00:43 2015

@author: wu34
"""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import utilise

Domain = ['ActType','DietType']
Metric = ['TF']

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
		clusterer = KMeans(n_clusters=n_clusters, n_init = 300)
		clusterer.fit(X)
		cluster_labels = clusterer.labels_
		
		# The silhouette_score gives the average value for all the samples.
		# This gives a perspective into the density and separation of the formed clusters
		silhouette_avg = silhouette_score(X, cluster_labels)
		print(metric, domain, 'For n_clusters =', n_clusters,
			  'The average silhouette_score is :', silhouette_avg)

for metric in Metric:
	for domain in Domain:
		sihouetteScore(domain,metric)
