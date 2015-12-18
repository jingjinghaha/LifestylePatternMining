# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:24:45 2015

@author: wu34
"""
import xlrd

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#extract the diet and activity information with time into a txt file 
def extract_act_diet_with_time(subjectID):
	file_location = 'subject_template_'+subjectID+'.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(3) 
	# print sheet.cell_value(0,0)
	# print sheet.nrows
	# print sheet.ncols
	
	# for col in range(sheet.ncols):
		# print sheet.cell_value(12,col)
		# print type(sheet.cell_value(12,col))
	f_act = open('activity_'+subjectID+'_with_time'+'.txt','w')
	f_diet = open('diet_'+subjectID+'_with_time'+'.txt','w')

	for row in range(8,sheet.nrows):
		if sheet.cell_value(row,0):
			temp_date = str(sheet.cell_value(row,0))
		date = temp_date 
		#print date
		#print type(sheet.cell_value(row,0))
		if sheet.cell_value(row,1):
			start_time = sheet.cell_value(row,1)
		else:
			if sheet.cell_value(row,2):
				start_time = sheet.cell_value(row,2)
			else: 
				start_time = 0
		if sheet.cell_value(row,2):
			end_time = sheet.cell_value(row,2)
		else:
			if sheet.cell_value(row,1):
				end_time = sheet.cell_value(row,1)
			else: 
				end_time = 0
		# print start_time
		# print type(start_time)
		# print end_time
		# print type(end_time)
		duration = end_time - start_time 
		# print duration 
		if sheet.cell_value(row, 3):
			temp_diet = str(sheet.cell_value(row, 3).encode('utf-8'))
			f_act.write("%-8s%-8s%-8s%-8s%s"%(date,start_time,end_time,duration,temp_diet))
			f_act.write('\n')
		if sheet.cell_value(row, 4):
			temp_act = str(sheet.cell_value(row, 4))
			f_diet.write("%-8s%-8s%-8s%-8s%s"%(date,start_time,end_time,duration,temp_act))
			f_diet.write('\n')


	f_act.close()
	f_diet.close()

# extract_act_diet_with_time('039')
for subjectID in available_list:
	print subjectID
	extract_act_diet_with_time(subjectID)
