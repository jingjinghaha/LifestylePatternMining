# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:13:59 2015

@author: wu34
"""

import numpy as np
import matplotlib.pyplot as plt
import utilise
import pylab as pl 

def similarityDict2array(input_dict,Threshold):
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	x = len(available_list)
	dims = (x, x)
	aa = np.zeros(dims)
	i = 0 
	for key1 in input_dict:
		j = 0 
		for key2 in input_dict:
			if Threshold > 0:
				if input_dict[key1][key2] <= Threshold:
					aa[i,j] = 0 
				else:
					aa[i,j] = input_dict[key1][key2]
			else:
				aa[i,j] = input_dict[key1][key2]
			j += 1
		i += 1
	# sorted = np.sort(aa)
	# return sorted 
	# print aa
	return aa 


def plotSimilarityMatrix(sim = 'TFIDFCosin'):
	actSimilarity_dict = utilise.SimilarityDict('ActItem',sim)
	# print actSimilarity_dict
	# print '\n'
	a = similarityDict2array(actSimilarity_dict,0)
	plt.figure()
	plt.matshow(a)
	pl.pcolor(a)
	plt.colorbar()
	plt.title('actSimilarityMatrix_'+sim)
	plt.savefig('visSimilarityMatrix/actSimilarityMatrix_'+sim)

	dietSimilarity_dict = utilise.SimilarityDict('DietItem',sim)
	# print dietSimilarity_dict
	# print '\n'
	a = similarityDict2array(dietSimilarity_dict,0)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('dietSimilarityMatrix_'+sim)
	plt.savefig('visSimilarityMatrix/dietSimilarityMatrix_'+sim)

	actTypeSimilarity_dict = utilise.SimilarityDict('ActType',sim)
	a = similarityDict2array(actTypeSimilarity_dict,0)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('actTypeSimilarityMatrix_'+sim)
	plt.savefig('visSimilarityMatrix/actTypeSimilarityMatrix_'+sim)

	dietTypeSimilarity_dict = utilise.SimilarityDict('DietType',sim)
	a = similarityDict2array(dietTypeSimilarity_dict,0)
	plt.figure()
	plt.matshow(a)
	plt.colorbar()
	plt.title('dietTypeSimilarityMatrix_'+sim)
	plt.savefig('visSimilarityMatrix/dietTypeSimilarityMatrix_'+sim)

# plotSimilarityMatrix('TFIDFCosin')