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

def buildSingleExcel(subjectID):
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


for subjectID in available_list:
	buildSingleExcel(subjectID)

