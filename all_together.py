# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:26:06 2015

@author: wu34
"""

import extractDietAct 
import preprocessDiary
import buildItemFreqTXTFile
import buildTypeFreqTXTFile
import visDietActPattern
import buildSimilarityTableExcel
import visSimilarityDistribution
import visSimilarityMat

# extract diet and activity information from excel
extractDietAct.extractDietAct()

# preprocessing include: tokenization, word removal, spell checking, lemmatization
preprocessDiary.preprocessDiary()

# build the diet/activity index with Item frequency in txt files 
buildItemFreqTXTFile.buildItemFreqTXTFile()

# build diet/activity type frequency in txt file 
buildTypeFreqTXTFile.buildTypeFreqTXTFile()

# data visualization (pie chart) for diet/activity pattern 
visDietActPattern.visDietActPattern()

# build excel table for the similarity between two users 
# the parameter is to set the similarity measurement method, the default is TFIDF
# numberOfSameWord,jaccard,novelJaccard,TFIDF
buildSimilarityTableExcel.buildSimilarityTableExcel(dist = 'jaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(dist = 'novelJaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(dist = 'TFIDF')

# visualization of similarity distribution (histogram)
# the parameter is to set the similarity measurement method, the default is TFIDF
# numberOfSameWord,jaccard,novelJaccard,TFIDF
visSimilarityDistribution.plotSimilarityDistribution('jaccard')
visSimilarityDistribution.plotSimilarityDistribution('novelJaccard')
visSimilarityDistribution.plotSimilarityDistribution('TFIDF')

# visualization of similarity matrix 
# the parameter is to set the similarity measurement method, the default is TFIDF
# numberOfSameWord,jaccard,novelJaccard,TFIDF
visSimilarityMat.plotSimilarityMatrix('jaccard')
visSimilarityMat.plotSimilarityMatrix('novelJaccard')
visSimilarityMat.plotSimilarityMatrix('TFIDF')
