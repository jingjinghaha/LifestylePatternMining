# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:59:57 2016

@author: wu34
"""

import xlrd
import dietActInfoRetrv
import pandas as pd 
import numpy as np

#dframe = pd.read_csv('SlpGroupInfo.csv')

def genDailyActTypeFeatureTable():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)
	
	table = []

	for row in range(1,sheet.nrows):
		vector = sheet.cell_value(row,3)
		vector = vector.split('[')[1].split(']')[0].split(',') 
		table.append(vector)

	FT = np.array(table)

	return FT

def genDailyDietTypeFeatureTable():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)
	
	table = []

	for row in range(1,sheet.nrows):
		vector = sheet.cell_value(row,5)
		vector = vector.split('[')[1].split(']')[0].split(',') 
		table.append(vector)

	FT = np.array(table)

	return FT

def getSlpTimeLabel():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)

	labels = [] 

	for row in range(1,sheet.nrows):
		labels.append(sheet.cell_value(row,7))

	labels = np.array(labels)

	return labels

def getMorningnessLabel():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)

	labels = [] 

	for row in range(1,sheet.nrows):
		labels.append(sheet.cell_value(row,8))

	labels = np.array(labels)

	return labels

def getEveningnessLabel():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)

	labels = [] 

	for row in range(1,sheet.nrows):
		labels.append(sheet.cell_value(row,9))

	labels = np.array(labels)

	return labels

def getLarkLabel():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)

	labels = [] 

	for row in range(1,sheet.nrows):
		labels.append(sheet.cell_value(row,10))

	labels = np.array(labels)

	return labels

def getOwlLabel():
	file = 'SlpGroupInfo.xlsx'
	workbook = xlrd.open_workbook(file)
	sheet = workbook.sheet_by_index(0)

	labels = [] 

	for row in range(1,sheet.nrows):
		labels.append(sheet.cell_value(row,11))

	labels = np.array(labels)

	return labels

#print type(dframe.iloc[3][3])
##dframe['frequency'][0:1] = dframe['frequency'][0:1].split('[')[1].split(']')[0].split(',')
#print type(dframe.iloc[0][3])
#
#print type(dframe['SubjId'])
#print dframe.ix[1]

#FT, labels = genDailyActTypeFeatureTable()
#print FT
