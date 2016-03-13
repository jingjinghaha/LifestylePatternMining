# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:57:34 2016

@author: wu34
"""

import xlwt
import xlrd
import utilise
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
	
	row_labels = utilise.itemDict2list(utilise.genActTypeDict())
	

	for rowR in range(8,sheet.nrows):
	
		if sheet.cell_value(rowR,0):

			ws.write(rowW,0,subjectID)
			ws.write(rowW,1,sheet.cell_value(rowR,0))
			index += 1

			dd = {}
			for label in row_labels:
				dd[label] = 0

			for line in open('activity/activityTypeFreq/activityType_frequency_'+subjectID+'_'+str(index)+'.txt','r'):
				line = line.strip('\n')
				words = wordpunct_tokenize(line)
				if words[0] in dd: 
					dd[words[0]] = int(words[1])

			sorted_dd = 
			ws.write(rowW,2,str(dd.keys()))
			ws.write(rowW,3,str(dd.values()))
			rowW += 1	
		
	workbookW.save('activity/activityTable_'+subjectID+'_withFreq.xls')

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
	
	row_labels = utilise.itemDict2list(utilise.genDietTypeDict())

	for rowR in range(8,sheet.nrows):

		if sheet.cell_value(rowR,0):
		
			ws.write(rowW,0,subjectID)
			ws.write(rowW,1,sheet.cell_value(rowR,0))
			index += 1 

			dd = {}
			for label in row_labels:
				dd[label] = 0

			for line in open('diet/dietTypeFreq/dietType_frequency_'+subjectID+'_'+str(index)+'.txt','r'):
				line = line.strip('\n')
				words = wordpunct_tokenize(line)
				if words[0] in dd: 
					dd[words[0]] = int(words[1])

			ws.write(rowW,2,str(dd.keys()))
			ws.write(rowW,3,str(dd.values()))
			rowW += 1

	workbookW.save('diet/dietTable_'+subjectID+'_withFreq.xls')

def buildActExcel():
	'''
	build activity excel for all the subjects, including the date, activity item and type
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')

	rowW = 0

	for subjectID in available_list:
		file_location = 'activity/activityTable_'+subjectID+'_withFreq.xls'
		workbookR = xlrd.open_workbook(file_location)
		sheet = workbookR.sheet_by_index(0)

		for rowR in range(0,sheet.nrows):
			ws.write(rowW,0,sheet.cell_value(rowR,0))
			ws.write(rowW,1,sheet.cell_value(rowR,1))
			ws.write(rowW,2,sheet.cell_value(rowR,2))
			ws.write(rowW,3,sheet.cell_value(rowR,3))
			# ws.write(rowW,4,sheet.cell_value(rowR,4))
			rowW += 1

	workbookW.save('activity/activityTable_withFreq.xls')

def buildDietExcel():
	'''
	build diet excel for all the subjects, including the date, diet item and type
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')

	rowW = 0

	for subjectID in available_list:
		file_location = 'diet/dietTable_'+subjectID+'_withFreq.xls'
		workbookR = xlrd.open_workbook(file_location)
		sheet = workbookR.sheet_by_index(0)
		
		for rowR in range(0,sheet.nrows):
			ws.write(rowW,0,sheet.cell_value(rowR,0))
			ws.write(rowW,1,sheet.cell_value(rowR,1))
			ws.write(rowW,2,sheet.cell_value(rowR,2))
			ws.write(rowW,3,sheet.cell_value(rowR,3))
			# ws.write(rowW,4,sheet.cell_value(rowR,4))
			rowW += 1

	workbookW.save('diet/dietTable_withFreq.xls')

def buildActWithSleepExcel():
	'''
	build activity excel for all the subjects, including the date, activity item and type, sleep
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	titles = ['SubjId','Day','ActType','frequency','Morningness','Eveningness','Lark','Owl','HoursSleep','SleepMoveCount','SleepQuality','MedianHR','MedianBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
	
	for i in range(len(titles)):
		ws.write(0,i,titles[i])

	rowW = 1
	file_location1 = 'activity/activityTable_withFreq.xls'
	workbookR1 = xlrd.open_workbook(file_location1)
	sheet1 = workbookR1.sheet_by_index(0)
	
	file_location2 = 'allSubjectsSleepDatamatrix.xls'
	workbookR2 = xlrd.open_workbook(file_location2)
	sheet2 = workbookR2.sheet_by_index(0)
	
	for rowRAct in range(0,sheet1.nrows):
		for rowRSlp in range(1,sheet2.nrows):
			sub = unicode(int(sheet2.cell_value(rowRSlp,0)))
			sub = '0'+sub 
			# print sub 
			if sheet1.cell_value(rowRAct,0) == sub:
				if sheet1.cell_value(rowRAct,1) == sheet2.cell_value(rowRSlp,1):
					
					if rowRSlp < sheet2.nrows -1:
						if sheet2.cell_value(rowRSlp,1) == sheet2.cell_value(rowRSlp+1,1):
							day = sheet2.cell_value(rowRSlp,1)
							temp = int(day.split('.')[1]) - 1
							day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
							
							if rowRAct >= 1: 
								dd = sheet1.cell_value(rowRAct-1,1) 
								temp = int(dd.split('.')[1])
								dd = dd.split('.')[0]+'.'+str(temp)+'.'+dd.split('.')[2]
								if dd == day: 
									ws.write(rowW,2,sheet1.cell_value(rowRAct-1,2))
									ws.write(rowW,3,sheet1.cell_value(rowRAct-1,3))
								else: 
									break
							else:
								break 
						else:
							day = sheet2.cell_value(rowRSlp,1)
							temp = int(day.split('.')[1])
							day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
							ws.write(rowW,2,sheet1.cell_value(rowRAct,2))
							ws.write(rowW,3,sheet1.cell_value(rowRAct,3))
					else: 
						day = sheet2.cell_value(rowRSlp,1)
						temp = int(day.split('.')[1])
						day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
						ws.write(rowW,2,sheet1.cell_value(rowRAct,2))
						ws.write(rowW,3,sheet1.cell_value(rowRAct,3))
					
					ws.write(rowW,0,sub)
					ws.write(rowW,1,day)
					ws.write(rowW,4,sheet2.cell_value(rowRSlp,5))
					ws.write(rowW,5,sheet2.cell_value(rowRSlp,6))
					ws.write(rowW,6,sheet2.cell_value(rowRSlp,7))
					ws.write(rowW,7,sheet2.cell_value(rowRSlp,8))
					ws.write(rowW,8,sheet2.cell_value(rowRSlp,9))
					ws.write(rowW,9,sheet2.cell_value(rowRSlp,10))
					ws.write(rowW,10,sheet2.cell_value(rowRSlp,11))
					ws.write(rowW,11,sheet2.cell_value(rowRSlp,12))
					ws.write(rowW,12,sheet2.cell_value(rowRSlp,13))
					ws.write(rowW,13,sheet2.cell_value(rowRSlp,14))
					ws.write(rowW,14,sheet2.cell_value(rowRSlp,15))
					ws.write(rowW,15,sheet2.cell_value(rowRSlp,16))
					ws.write(rowW,16,sheet2.cell_value(rowRSlp,17))
					ws.write(rowW,17,sheet2.cell_value(rowRSlp,18))
					ws.write(rowW,18,sheet2.cell_value(rowRSlp,19))
					ws.write(rowW,19,sheet2.cell_value(rowRSlp,20))
					ws.write(rowW,20,sheet2.cell_value(rowRSlp,21))
					ws.write(rowW,21,sheet2.cell_value(rowRSlp,22))
					ws.write(rowW,22,sheet2.cell_value(rowRSlp,23))
					rowW += 1

	workbookW.save('activity/activityTableWithSleep_withFreq.xls')

def buildDietWithSleepExcel():
	'''
	build diet excel for all the subjects, including the date, activity item and type, sleep
	'''
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	titles = ['SubjId','Day','DietType','frequency','Morningness','Eveningness','Lark','Owl','HoursSleep','SleepMoveCount','SleepQuality','MedianHR','MedianBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
	
	for i in range(len(titles)):
		ws.write(0,i,titles[i])

	rowW = 1
	file_location1 = 'diet/dietTable_withFreq.xls'
	workbookR1 = xlrd.open_workbook(file_location1)
	sheet1 = workbookR1.sheet_by_index(0)
	
	file_location2 = 'allSubjectsSleepDatamatrix.xls'
	workbookR2 = xlrd.open_workbook(file_location2)
	sheet2 = workbookR2.sheet_by_index(0)
	
	for rowRDiet in range(0,sheet1.nrows):
		for rowRSlp in range(1,sheet2.nrows):
			sub = unicode(int(sheet2.cell_value(rowRSlp,0)))
			sub = '0'+sub 
			# print sub 
			if sheet1.cell_value(rowRDiet,0) == sub:
				if sheet1.cell_value(rowRDiet,1) == sheet2.cell_value(rowRSlp,1):
					
					if rowRSlp < sheet2.nrows -1:
						if sheet2.cell_value(rowRSlp,1) == sheet2.cell_value(rowRSlp+1,1):
							day = sheet2.cell_value(rowRSlp,1)
							temp = int(day.split('.')[1]) - 1
							day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
							
							if rowRDiet >= 1: 
								dd = sheet1.cell_value(rowRDiet-1,1) 
								temp = int(dd.split('.')[1])
								dd = dd.split('.')[0]+'.'+str(temp)+'.'+dd.split('.')[2]
								if dd == day: 
									ws.write(rowW,2,sheet1.cell_value(rowRDiet-1,2))
									ws.write(rowW,3,sheet1.cell_value(rowRDiet-1,3))
								else: 
									break
							else:
								break 
						else:
							day = sheet2.cell_value(rowRSlp,1)
							temp = int(day.split('.')[1])
							day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
							ws.write(rowW,2,sheet1.cell_value(rowRDiet,2))
							ws.write(rowW,3,sheet1.cell_value(rowRDiet,3))
					else: 
						day = sheet2.cell_value(rowRSlp,1)
						temp = int(day.split('.')[1])
						day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
						ws.write(rowW,2,sheet1.cell_value(rowRDiet,2))
						ws.write(rowW,3,sheet1.cell_value(rowRDiet,3))
					
					ws.write(rowW,0,sub)
					ws.write(rowW,1,day)
					ws.write(rowW,4,sheet2.cell_value(rowRSlp,5))
					ws.write(rowW,5,sheet2.cell_value(rowRSlp,6))
					ws.write(rowW,6,sheet2.cell_value(rowRSlp,7))
					ws.write(rowW,7,sheet2.cell_value(rowRSlp,8))
					ws.write(rowW,8,sheet2.cell_value(rowRSlp,9))
					ws.write(rowW,9,sheet2.cell_value(rowRSlp,10))
					ws.write(rowW,10,sheet2.cell_value(rowRSlp,11))
					ws.write(rowW,11,sheet2.cell_value(rowRSlp,12))
					ws.write(rowW,12,sheet2.cell_value(rowRSlp,13))
					ws.write(rowW,13,sheet2.cell_value(rowRSlp,14))
					ws.write(rowW,14,sheet2.cell_value(rowRSlp,15))
					ws.write(rowW,15,sheet2.cell_value(rowRSlp,16))
					ws.write(rowW,16,sheet2.cell_value(rowRSlp,17))
					ws.write(rowW,17,sheet2.cell_value(rowRSlp,18))
					ws.write(rowW,18,sheet2.cell_value(rowRSlp,19))
					ws.write(rowW,19,sheet2.cell_value(rowRSlp,20))
					ws.write(rowW,20,sheet2.cell_value(rowRSlp,21))
					ws.write(rowW,21,sheet2.cell_value(rowRSlp,22))
					ws.write(rowW,22,sheet2.cell_value(rowRSlp,23))
					rowW += 1

	workbookW.save('diet/dietTableWithSleep_withFreq.xls')

def buildDietActTableWithSlpWithFreq():
	for subjectID in available_list:
		buildSingleActExcel(subjectID)
		buildSingleDietExcel(subjectID)

	buildActExcel()
	buildDietExcel()

	buildActWithSleepExcel()
	buildDietWithSleepExcel()

buildDietActTableWithSlpWithFreq() 
