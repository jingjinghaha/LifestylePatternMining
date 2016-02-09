# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:06:17 2015

@author: wu34
"""

import xlrd
import infoRetrival

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#extract total diet and activity information of each subject
def extract_act_diet(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3) 
	# print sheet.cell_value(0,0)
	# print sheet.nrows
	# print sheet.ncols
	
	# for col in range(sheet.ncols):
		# print sheet.cell_value(12,col)
		# print type(sheet.cell_value(12,col))
	f_act = open('activity/activityFromExcel/activity_'+subjectID+'.txt','w')
	f_diet = open('diet/dietFromExcel/diet_'+subjectID+'.txt','w')

	for row in range(8,sheet.nrows):
		if sheet.cell_value(row, 3):
			# print row
			# print type(sheet.cell_value(row, 4))
			temp = str(sheet.cell_value(row, 3).encode('utf-8'))
			f_act.write(temp)
			f_act.write('\n')

	for row in range(8,sheet.nrows):
		if sheet.cell_value(row, 4):
			# print row
			# print type(sheet.cell_value(row, 4))
			temp = str(sheet.cell_value(row, 4))
			f_diet.write(temp)
			f_diet.write('\n')

	f_act.close()
	f_diet.close()

#extract daily diet and activity information of each subject 
def extractSingleDailyActDiet(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3)
	duration = infoRetrival.getDuration(subjectID)
	for n in range(1,duration+1):
		f_act = open('activity/activityFromExcel/activity_'+subjectID+'_'+str(n)+'.txt','w')
		f_diet = open('diet/dietFromExcel/diet_'+subjectID+'_'+str(n)+'.txt','w')
		f_act.close()
		f_diet.close()
	
	count = 0 
	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			count += 1
		if sheet.cell_value(row,3):
			temp = str(sheet.cell_value(row,3).encode('utf-8'))
			f_act = open('activity/activityFromExcel/activity_'+subjectID+'_'+str(count)+'.txt','a')
			f_act.write(temp)
			f_act.write('\n')
			f_act.close()
		if sheet.cell_value(row,4):
			temp = str(sheet.cell_value(row,4))
			f_diet = open('diet/dietFromExcel/diet_'+subjectID+'_'+str(count)+'.txt','a')
			f_diet.write(temp)
			f_diet.write('\n')
			f_diet.close()

#extract diet and activity information from the xlsx files
def extractDietAct():
	print 'in extractDietAct()'
	# extract_act_diet_with_time('039')
	for subjectID in available_list:
		print subjectID
		extract_act_diet(subjectID)

#extract daily diet and activity information into corresponding txt files 
def extractDailyActDiet():
	print 'in extractDailyActDiet()'
	for subjectID in available_list:
		print subjectID
		extractSingleDailyActDiet(subjectID)

# extractDietAct()
