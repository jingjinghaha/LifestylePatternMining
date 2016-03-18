# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 09:49:57 2016

@author: wu34
"""

from sklearn.cluster import AffinityPropagation
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from itertools import cycle
import visSimilarityMat
import utilise

Domain = ['DietType','ActType']
# sim is to set the similarity measurement method, the default is TFIDFCosin
# jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
Sim = ['jaccard','novelJaccard','TFCosin','TFEclud','TFIDFCosin','TFIDFEclud']

def AP(domain, sim):
	Similarity_dict = {}
	if domain == 'DietItem':
		Similarity_dict = utilise.SimilarityDict(domain,sim)
	elif domain == 'ActItem':
		Similarity_dict = utilise.SimilarityDict(domain,sim)
	elif domain == 'DietType':
		Similarity_dict = utilise.SimilarityDict(domain,sim)
	elif domain == 'ActType':
		Similarity_dict = utilise.SimilarityDict(domain,sim)
	X = visSimilarityMat.similarityDict2array(Similarity_dict,0)

	af = AffinityPropagation(affinity = "precomputed").fit(X)
	cluster_centers_indices = af.cluster_centers_indices_
	# print cluster_centers_indices
	# print type(cluster_centers_indices)
	labels = af.labels_
	print domain,sim,labels
	# print type(labels)
	n_clusters_ = len(cluster_centers_indices)
	# print('Estimated number of clusters: %d' % n_clusters_)

	X = PCA(n_components=2).fit_transform(X)

	plt.figure()
	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	for k, col in zip(range(n_clusters_), colors):
		# print k,col
		class_members = labels == k
		cluster_center = X[cluster_centers_indices[k]]
		# print class_members
		# print cluster_center 
		# plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
		# plt.plot(X[class_members, 1], X[class_members, 2], col + '.')
		# plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
		plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=8)
		for x in X[class_members]:
			# print x 
			# plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
			plt.plot(x[0], x[1], col + '.')
			plt.text(x[0], x[1], k)
			plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

	plt.title('AP_'+domain+'_'+sim+'_'+str(n_clusters_))
	plt.savefig('VisClustering'+domain+'Pattern/AffinityPropagation_'+sim+'_'+str(n_clusters_))
	# plt.show()


for domain in Domain:
	for sim in Sim:
		AP(domain,sim)

# AP('ActItem', 'TFIDFEclud')
