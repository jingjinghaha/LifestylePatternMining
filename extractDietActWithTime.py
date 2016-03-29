# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:24:45 2015

@author: wu34
"""
import xlrd
import dietActInfoRetrv

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#extract the diet and activity information with date into a txt file 
def extract_act_diet_with_date(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3) 
	
	f_act = open('activity/activityFromExcel/activity_'+subjectID+'_with_date'+'.txt','w')
	f_diet = open('diet/dietFromExcel/diet_'+subjectID+'_with_date'+'.txt','w')

	for row in range(8,sheet.nrows):
	
		if sheet.cell_value(row,0):
			temp_date = str(sheet.cell_value(row,0))
		date = temp_date 
		#print date
		#print type(sheet.cell_value(row,0))
		
		if sheet.cell_value(row, 3):
			temp = str(sheet.cell_value(row, 3).encode('utf-8'))
			f_act.write("%-12s%s"%(date,temp))
			f_act.write('\n')
		
		if sheet.cell_value(row, 4):
			temp = str(sheet.cell_value(row, 4))
			f_diet.write("%-12s%s"%(date,temp))
			f_diet.write('\n')
		
	f_act.close()
	f_diet.close()

#extract the diet and activity information with time into a txt file 
def extract_daily_act_diet_with_time(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3) 

	duration = dietActInfoRetrv.getDuration(subjectID)

	for n in range(1,duration+1):
		f_act = open('activity/activityFromExcel/activity_'+subjectID+'_'+str(n)+'_with_time.txt','w')
		f_diet = open('diet/dietFromExcel/diet_'+subjectID+'_'+str(n)+'_with_time.txt','w')
		f_act.close()
		f_diet.close()
	
	count = 0 
	for row in range(8,sheet.nrows):
	
		if sheet.cell_value(row,1):
			temp_time = int(sheet.cell_value(row,1))
		time = temp_time 
		
		if sheet.cell_value(row,0):
			count += 1
			
		if sheet.cell_value(row,3):
			temp = str(sheet.cell_value(row,3).encode('utf-8'))
			f_act = open('activity/activityFromExcel/activity_'+subjectID+'_'+str(count)+'_with_time.txt','a')
			f_act.write("%-12s%s"%(time,temp))
			f_act.write('\n')
			f_act.close()
			
		if sheet.cell_value(row,4):
			temp = str(sheet.cell_value(row,4))
			f_diet = open('diet/dietFromExcel/diet_'+subjectID+'_'+str(count)+'_with_time.txt','a')
			f_diet.write("%-12s%s"%(time,temp))
			f_diet.write('\n')
			f_diet.close()

#extract the diet and activity information with date into a txt file
def extractDietActWithDate():
	for subjectID in available_list:
		print subjectID
		extract_act_diet_with_date(subjectID)

#extract the daily diet and activity information with time into a txt file
def extractDailyDietActWithTime():
	for subjectID in available_list:
		print subjectID
		extract_daily_act_diet_with_time(subjectID)

#extractDietActWithDate()
#extractDailyDietActWithTime()
