# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:26:06 2015

@author: wu34
"""
import matplotlib.pyplot as plt
import extractDietAct 
import extractDietActWithTime  
import preprocessDiary
import buildItemFreqTXTFile
import buildTypeFreqTXTFile
import visDietActPattern
import buildSimilarityTableExcel
import visSimilarityDistribution
import visSimilarityMat
import visTFMat 
import visTFIDFMat
import visDailyPatternInterGroup
import visDailyPatternIntraGroup
import buildDietActTable
import clsKmeansLabels
import groupAnalysis
import buildDietActTableWithFreq
import buildSubAveInfoTable 

plt.close('all')
plt.clf()

# extract diet and activity information from excel
extractDietAct.extractDietAct()
extractDietAct.extractDailyActDiet()

# extract diet and activity information from excel with date and timing info 
extractDietActWithTime.extractDietActWithDate()
extractDietActWithTime.extractDailyDietActWithTime()

# preprocessing include: tokenization, word removal, spell checking, lemmatization
preprocessDiary.preprocessDiary()
preprocessDiary.preprocessDailyDiary()
preprocessDiary.preprocessDailyDiaryWithTime()

# build the diet/activity index with Item frequency in txt files 
buildItemFreqTXTFile.buildItemFreqTXTFile()
buildItemFreqTXTFile.buildDailyItemFreqTXTFile()

# build diet/activity type frequency in txt file 
buildTypeFreqTXTFile.buildTypeFreqTXTFile()

# data visualization (pie chart) for diet/activity pattern 
visDietActPattern.visDietActPattern()

# build excel table for the similarity between two users 
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'jaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'novelJaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFCosin')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFEclud')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFIDFCosin')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFIDFEclud')


# visualization of similarity distribution (histogram)
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
visSimilarityDistribution.plotSimilarityDistribution('jaccard')
visSimilarityDistribution.plotSimilarityDistribution('novelJaccard')
visSimilarityDistribution.plotSimilarityDistribution('TFCosin')
visSimilarityDistribution.plotSimilarityDistribution('TFEclud')
visSimilarityDistribution.plotSimilarityDistribution('TFIDFCosin')
visSimilarityDistribution.plotSimilarityDistribution('TFIDFEclud')


# visualization of similarity matrix 
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
visSimilarityMat.plotSimilarityMatrix('jaccard')
visSimilarityMat.plotSimilarityMatrix('novelJaccard')
visSimilarityMat.plotSimilarityMatrix('TFCosin')
visSimilarityMat.plotSimilarityMatrix('TFEclud')
visSimilarityMat.plotSimilarityMatrix('TFIDFCosin')
visSimilarityMat.plotSimilarityMatrix('TFIDFEclud')

# visualization of TF and TFIDF matrix
visTFMat.visTFMatrix()
visTFIDFMat.visTFIDFMatrix()

# # build excel file that combine the act/diet with sleep informaiton 
buildDietActTable.buildDietActTableWithSlp()
buildDietActTableWithFreq.buildDietActTableWithSlpWithFreq()

# '''
# The following steps are done after we finish the Kmeans and get the best labels 
# '''
# # plot best labels got from KMeans 
# visKmeansLabels.clusteringKmeansLabels()

# # grouping analysis will give the demo and sleep info of the groups and also the integration 
# groupAnalysis.groupAnalysis()

# # visualization of subject's daily pattern based best grouping results from KMeans
# visDailyPatternIntraGroup.visDailyPatternIntraGroup()
# visDailyPatternInterGroup.visDailyPatternInterGroup()

# # build table 1 for subjects' demo and avrage sleep info with their grouping info 
# # table 2 for diet type TF table; table 3 for avtivity type TF table; 
# buildSubAveInfoTable.buildSubAveInfo()
