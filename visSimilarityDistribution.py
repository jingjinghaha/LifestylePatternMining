# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:42:24 2015

@author: wu34
"""

import matplotlib.pyplot as plt
import utilise

def similarityDict2list(input_dict):
	list_temp = []
	# available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	i = 0 
	for  key1 in input_dict:
		j = 0 
		for key2 in input_dict:
			if j > i:
				list_temp.append(input_dict[key1][key2])
			j += 1
		i += 1
	# print list 
	return list_temp


def plotSimilarityDistribution(sim = 'TFIDFCosin'):
	actSimilarity_dict = utilise.SimilarityDict('ActItem',sim)
	similarityList = similarityDict2list(actSimilarity_dict)
	plt.figure()
	plt.hist(similarityList)
	plt.title('actSimilarityDistribution_'+sim)
	plt.xlim(0.0,1.0)
	plt.savefig('visSimilarityDistributionHist/actSimilarityDistribution_'+sim)

	dietSimilarity_dict = utilise.SimilarityDict('DietItem',sim)
	similarityList = similarityDict2list(dietSimilarity_dict)
	plt.figure()
	plt.hist(similarityList)
	plt.title('dietSimilarityDistribution_'+sim)
	plt.xlim(0.0,1.0)
	plt.savefig('visSimilarityDistributionHist/dietSimilarityDistribution_'+sim)

	actTypeSimilarity_dict = utilise.SimilarityDict('ActType',sim)
	similarityList = similarityDict2list(actTypeSimilarity_dict)
	plt.figure()
	plt.hist(similarityList)
	plt.title('actTypeSimilarityDistribution_'+sim)
	plt.xlim(0.0,1.0)
	plt.savefig('visSimilarityDistributionHist/actTypeSimilarityDistribution_'+sim)

	dietTypeSimilarity_dict = utilise.SimilarityDict('DietType',sim)
	similarityList = similarityDict2list(dietTypeSimilarity_dict)
	plt.figure()
	plt.hist(similarityList)
	plt.title('dietTypeSimilarityDistribution_'+sim)
	plt.xlim(0.0,1.0)
	plt.savefig('visSimilarityDistributionHist/dietTypeSimilarityDistribution_'+sim)

plotSimilarityDistribution('jaccard')
plotSimilarityDistribution('novelJaccard')
plotSimilarityDistribution('TFCosin')
plotSimilarityDistribution('TFEclud')
plotSimilarityDistribution('TFIDFCosin')
plotSimilarityDistribution('TFIDFEclud')
