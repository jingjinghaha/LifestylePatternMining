# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:25:44 2016

@author: wu34
"""

import numpy as np 
import xlrd
import utilise
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def diaryDurationList():
	durationList = []
	for subjectID in available_list:
		durationList.append(getDuration(subjectID))
	return durationList
	
def getDuration(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3)
	duration = 0 
	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			duration += 1 
	return duration 

def getStartEndTime(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3)
	startDate = sheet.cell_value(8,0)
	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			endDate = sheet.cell_value(row,0)
	return startDate, endDate

def getTimeDict(subjectID):
	timeDict = {}
	startDate,endDate = getStartEndTime(subjectID)
	timeDict['startDate'] = startDate
	timeDict['endDate'] = endDate
	timeDict['duration'] = getDuration(subjectID)
	return timeDict 
	
def diaryTimeDict():
	totalTimeDict = {}
	for i in range(len(available_list)):
		totalTimeDict[i] = getTimeDict(available_list[i])
	return totalTimeDict
	
def getGroups(labels):
	groups = {} 

	for k in range(4):
		groups[k] = []
		class_members = labels == k
		# print class_members.shape[0]

		for i in range(class_members.shape[0]):
			if class_members[i] == True:
				groups[k].append(available_list[i])

	return groups 

def string2array(str):
	temp = str.split(' ')
	for i in range(len(temp)):
		token = int(temp[i])
		temp[i] = token
	array = np.array(temp)
	return array 
	
def groupingAnalysis():
	labelsDietType = string2array('0 1 2 1 2 0 1 2 2 3 3 0 2 2 2 2 0 1 2 0 2 2 2 2 3 2 1 3 3')
	labelsActType = string2array('1 3 1 1 2 2 2 2 3 1 2 2 1 2 0 2 3 0 1 2 3 1 1 2 1 0 2 0 0')

	groupDiet = getGroups(labelsDietType)
	groupAct = getGroups(labelsActType)
	print groupAct
	print groupDiet

	dd = {}
	for key1 in groupAct:
		dd[key1] = {}
		for key2 in groupDiet:
			dd[key1][key2] = 0 
			for item in groupAct[key1]:
				if item in groupDiet[key2]:
					dd[key1][key2] += 1 
	print dd 
					
	dd = {}
	for key1 in groupDiet:
		dd[key1] = {}
		for key2 in groupAct:
			dd[key1][key2] = 0 
			for item in groupDiet[key1]:
				if item in groupAct[key2]:
					dd[key1][key2] += 1 
	print dd 			
		
	labelsActItem = string2array('2 3 0 0 3 3 2 2 2 2 1 1 0 1 2 1 3 2 2 1 3 2 0 1 2 2 3 1 2')
	labelsDietItem = string2array('3 3 2 2 2 2 0 2 2 2 2 3 3 2 3 2 0 2 2 3 2 2 2 2 1 2 0 1 1')

	groupDiet = getGroups(labelsDietItem)
	groupAct = getGroups(labelsActItem)
	print groupAct
	print groupDiet

	dd = {}
	for key1 in groupAct:
		dd[key1] = {}
		for key2 in groupDiet:
			dd[key1][key2] = 0 
			for item in groupAct[key1]:
				if item in groupDiet[key2]:
					dd[key1][key2] += 1 
	print dd 
					
	dd = {}
	for key1 in groupDiet:
		dd[key1] = {}
		for key2 in groupAct:
			dd[key1][key2] = 0 
			for item in groupDiet[key1]:
				if item in groupAct[key2]:
					dd[key1][key2] += 1 
	print dd 

# groupingAnalysis()

# print diaryTimeDict()
# tf = utilise.genActItemTFArray()
# print tf.shape
# tf = utilise.genDietItemTFArray()
# print tf.shape