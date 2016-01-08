# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 17:34:11 2016

@author: wu34
"""

from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from itertools import cycle
import visSimilarityMat
import utilise

Domain = ['DietItem','ActItem','DietType','ActType']
# dist is to set the similarity measurement method, the default is TFIDFCosin
# jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
dist = 'jaccard'
for domain in Domain:
	dietSimilarity_dict = {}
	if domain == 'DietItem':
		Similarity_dict = utilise.SimilarityDict(domain,dist)
	elif domain == 'ActItem':
		Similarity_dict = utilise.SimilarityDict(domain,dist)
	elif domain == 'DietType':
		Similarity_dict = utilise.SimilarityDict(domain,dist)
	elif domain == 'ActType':
		Similarity_dict = utilise.SimilarityDict(domain,dist)
	X = visSimilarityMat.similarityDict2array(Similarity_dict,0)

	af = SpectralClustering(affinity = "precomputed").fit(X)
	labels = af.labels_
	print labels
