# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 16:35:07 2016

@author: wu34
"""

import xlwt
import xlrd
import actType
from nltk import wordpunct_tokenize

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def buildSingleActExcel(subjectID):
	'''
	build activity excel for single subject, including the date, activity item and type
	'''
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbookR = xlrd.open_workbook(file_location)
	sheet = workbookR.sheet_by_index(3)

	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	
	rowW = 0 
	index = 0 
	itemString = ''
	typeString = '' 
	
	for rowR in range(8,sheet.nrows):
		if sheet.cell_value(rowR,0):
			ws.write(rowW,0,subjectID)
			ws.write(rowW,1,sheet.cell_value(rowR,0))
			index += 1 
			for line in open('activity/activityItemFreq/activity_frequency_'+subjectID+'_'+str(index)+'.txt','r'):
				line = line.strip('\n')
				words = wordpunct_tokenize(line)
				itemString = itemString+' '+words[0]
				type = actType.actType(words[0])
				typeString = typeString+' '+type 
			ws.write(rowW,2,itemString)
			ws.write(rowW,3,typeString)
			rowW += 1
		
	workbookW.save('activity/activityTable_'+subjectID+'.xls')

def buildSingleDietExcel(subjectID):
	'''
	build diet excel for single subject, including the date, diet item and type
	'''
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbookR = xlrd.open_workbook(file_location)
	sheet = workbookR.sheet_by_index(3)

	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	
	rowW = 0 
	index = 0 
	itemString = ''
	typeString = '' 
	
	for rowR in range(8,sheet.nrows):
		if sheet.cell_value(rowR,0):
			ws.write(rowW,0,subjectID)
			ws.write(rowW,1,sheet.cell_value(rowR,0))
			index += 1 
			for line in open('diet/dietItemFreq/diet_frequency_'+subjectID+'_'+str(index)+'.txt','r'):
				line = line.strip('\n')
				words = wordpunct_tokenize(line)
				itemString = itemString+' '+words[0]
				type = actType.actType(words[0])
				typeString = typeString+' '+type 
			ws.write(rowW,2,itemString)
			ws.write(rowW,3,typeString)
			rowW += 1
		
	workbookW.save('diet/dietTable_'+subjectID+'.xls')

def buildActExcel():
	'''
	build activity excel for all the subjects, including the date, activity item and type
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')

	rowW = 0

	for subjectID in available_list:
		file_location = 'activity/activityTable_'+subjectID+'.xls'
		workbookR = xlrd.open_workbook(file_location)
		sheet = workbookR.sheet_by_index(0)
		for rowR in range(0,sheet.nrows):
			ws.write(rowW,0,sheet.cell_value(rowR,0))
			ws.write(rowW,1,sheet.cell_value(rowR,1))
			ws.write(rowW,2,sheet.cell_value(rowR,2))
			rowW += 1

	workbookW.save('activity/activityTable.xls')

def buildDietExcel():
	'''
	build diet excel for all the subjects, including the date, diet item and type
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')

	rowW = 0

	for subjectID in available_list:
		file_location = 'diet/dietTable_'+subjectID+'.xls'
		workbookR = xlrd.open_workbook(file_location)
		sheet = workbookR.sheet_by_index(0)
		for rowR in range(0,sheet.nrows):
			ws.write(rowW,0,sheet.cell_value(rowR,0))
			ws.write(rowW,1,sheet.cell_value(rowR,1))
			ws.write(rowW,2,sheet.cell_value(rowR,2))
			rowW += 1

	workbookW.save('diet/dietTable.xls')

for subjectID in available_list:
	buildSingleActExcel(subjectID)
	buildSingleDietExcel(subjectID)

# buildActExcel()
# buildDietExcel()
