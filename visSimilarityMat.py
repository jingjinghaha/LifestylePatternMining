# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:13:59 2015

@author: wu34
"""

import numpy as np
import matplotlib.pyplot as plt
import dietItemSimilarityTable
import actItemSimilarityTable
import dietTypeSimilarityTable
import actTypeSimilarityTable

def similarityDict2array(input_dict):
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	x = len(available_list)
	dims = (x, x)
	aa = np.zeros(dims)
	i = 0 
	for key1 in input_dict:
		j = 0 
		for key2 in input_dict:
			aa[i,j] = input_dict[key1][key2]
			j += 1
		i += 1
	sorted = np.sort(aa)
	return sorted 


def plotSimilarityMatrix(dist = 'novelJaccard'):
	actSimilarity_dict = actItemSimilarityTable.actItemSimilarityDict(dist)
	a = similarityDict2array(actSimilarity_dict)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('actSimilarityMatrix_'+dist)
	plt.savefig('actSimilarityMatrix_'+dist)

	dietSimilarity_dict = dietItemSimilarityTable.dietItemSimilarityDict(dist)
	a = similarityDict2array(dietSimilarity_dict)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('dietSimilarityMatrix_'+dist)
	plt.savefig('dietSimilarityMatrix_'+dist)

	actTypeSimilarity_dict = actTypeSimilarityTable.actTypeSimilarityDict(dist)
	a = similarityDict2array(actTypeSimilarity_dict)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('actTypeSimilarityMatrix_'+dist)
	plt.savefig('actTypeSimilarityMatrix_'+dist)

	dietTypeSimilarity_dict = dietTypeSimilarityTable.dietTypeSimilarityDict(dist)
	a = similarityDict2array(dietTypeSimilarity_dict)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('dietTypeSimilarityMatrix_'+dist)
	plt.savefig('dietTypeSimilarityMatrix_'+dist)

plotSimilarityMatrix('TFIDF')