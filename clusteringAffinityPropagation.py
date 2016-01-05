# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 09:49:57 2016

@author: wu34
"""

from sklearn.cluster import AffinityPropagation
import matplotlib.pyplot as plt
from itertools import cycle
import dietItemSimilarityTable
import actItemSimilarityTable
import dietTypeSimilarityTable
import actTypeSimilarityTable
import visSimilarityMat

Domain = ['DietItem','ActItem','DietType','ActType']
# dist is to set the similarity measurement method, the default is TFIDF
# jaccard,novelJaccard,TFIDF
dist = 'jaccard'
for domain in Domain:
	dietSimilarity_dict = {}
	if domain == 'DietItem':
		Similarity_dict = dietItemSimilarityTable.dietItemSimilarityDict(dist)
	elif domain == 'ActItem':
		Similarity_dict = actItemSimilarityTable.actItemSimilarityDict(dist)
	elif domain == 'DietType':
		Similarity_dict = dietTypeSimilarityTable.dietTypeSimilarityDict(dist)
	elif domain == 'ActType':
		Similarity_dict = actTypeSimilarityTable.actTypeSimilarityDict(dist)
	X = visSimilarityMat.similarityDict2array(Similarity_dict)

	af = AffinityPropagation(preference=-50).fit(X)
	cluster_centers_indices = af.cluster_centers_indices_
	print cluster_centers_indices
	labels = af.labels_
	print labels
	n_clusters_ = len(cluster_centers_indices)
	print('Estimated number of clusters: %d' % n_clusters_)

	plt.figure()
	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	for k, col in zip(range(n_clusters_), colors):
		class_members = labels == k
		cluster_center = X[cluster_centers_indices[k]]
		plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
		plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
				 markeredgecolor='k', markersize=14)
		for x in X[class_members]:
			plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

	plt.title('Estimated number of clusters: %d' % n_clusters_)
	plt.savefig('VisClustering'+domain+'Pattern/AffinityPropagation_'+dist)
	plt.show()