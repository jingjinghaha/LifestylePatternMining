# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:26:06 2015

@author: wu34
"""

import extractDietAct 
import preprocessDiary
import buildFreqIndexTXTFile
import buildTypeFreqTXTFile
import plotDietActItemFreq
import plotOverallDietActItemFreq
import plotDietActTypeFreq
import plotOverallDietActTypeFreq
import dietItemSimilarityTable
import actItemSimilarityTable
import dietTypeSimilarityTable
import actTypeSimilarityTable

# extract diet and activity information from excel
extractDietAct.extractDietAct()

# preprocessing include: tokenization, word removal, spell checking, lemmatization
preprocessDiary.preprocessDiary()

# build the diet/activity index with Item frequency in txt files 
buildFreqIndexTXTFile.buildFreqIndexTXTFile()

# build diet/activity type frequency in txt file 
buildTypeFreqTXTFile.buildTypeFreqTXTFile()

# data visualization (pie chart) for diet/activity Item pattern of each people 
# the parameter is to set the minimal Item frequency 
plotDietActItemFreq.plotDietActItemFreq(3)

# data visualization (pie chart) for overall diet/activity Item pattern
# the parameter is to set the minimal Item frequency 
plotOverallDietActItemFreq.plotOverallDietActItemFreq(10)

# data visualization (pie chart) for diet/activity type pattern of each people 
plotDietActTypeFreq.plotDietActTypeFreq()

# data visualization (pie chart) for overall diet/activity type pattern 
plotOverallDietActTypeFreq.plotOverallDietActTypeFreq()

# data visualization (table) for the diet Item similarity between two users 
dietItemSimilarityTable.dietItemSimilarityTable()

# data visualization (table) for the activity Item similarity between two users 
actItemSimilarityTable.actItemSimilarityTable()

# data visualization (table) for the diet type similarity between two users 
dietTypeSimilarityTable.dietTypeSimilarityTable()

# data visualization (table) for the activity type similarity between two users 
actTypeSimilarityTable.actTypeSimilarityTable()
