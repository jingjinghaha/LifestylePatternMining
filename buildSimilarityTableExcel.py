# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 16:29:45 2016

@author: wu34
"""

import dietItemSimilarityTable
import actItemSimilarityTable
import dietTypeSimilarityTable
import actTypeSimilarityTable

# build excel table for the similarity between two users 
# the parameter is to set the similarity measurement method, the default is TFIDF
# numberOfSameWord,jaccard,novelJaccard,TFIDF
def buildSimilarityTableExcel(dist = 'TFIDF'):
	# data visualization (table) for the diet Item similarity between two users
	dietItemSimilarityTable.dietItemSimilarityTable(dist)
	# build excel table for the activity Item similarity between two users
	actItemSimilarityTable.actItemSimilarityTable(dist)
	# build excel table for the diet type similarity between two users
	dietTypeSimilarityTable.dietTypeSimilarityTable(dist)
	# build excel table for the activity type similarity between two users
	actTypeSimilarityTable.actTypeSimilarityTable(dist)
