# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:31:40 2016

@author: wu34
"""

import xlrd 
import numpy as np
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def getDemoGInfo():
	file_location = 'allSubjectsSleepDatamatrix.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	
	Age = []
	Gender = [] 
	Height = []
	Weight = [] 
	BMI = []
	FatFree = []
	FatMass = []
	PercFat = []
	Vo2max = []
	gender = [0, 0]

	for subject in available_list:
		for rowRSlp in range(1,sheet.nrows):
			sub = unicode(int(sheet.cell_value(rowRSlp,0)))
			sub = '0'+sub
			# print sub
			if sub == subject: 
				print sub
				Age.append(sheet.cell_value(rowRSlp,15))
				Gender.append(sheet.cell_value(rowRSlp,16))
				Height.append(sheet.cell_value(rowRSlp,17))
				Weight.append(sheet.cell_value(rowRSlp,18))
				BMI.append(sheet.cell_value(rowRSlp,19))
				FatFree.append(sheet.cell_value(rowRSlp,20))
				FatMass.append(sheet.cell_value(rowRSlp,21))
				PercFat.append(sheet.cell_value(rowRSlp,22))
				Vo2max.append(sheet.cell_value(rowRSlp,23))
				break 
	
	# print Age,Gender,Height,Weight,BMI,FatFree,FatMass,PercFat,Vo2max

	age = sum(Age)/float(len(Age))
	gender[0] = Gender.count(1.0)
	gender[1] = Gender.count(0.0)
	height = sum(Height)/float(len(Height))
	weight = sum(Weight)/float(len(Weight))
	bmi = sum(BMI)/float(len(BMI))
	fatFree = sum(FatFree)/float(len(FatFree))
	fatMass = sum(FatMass)/float(len(FatMass))
	percFat = sum(PercFat)/float(len(PercFat))
	vo2max = sum(Vo2max)/float(len(Vo2max))

	print 'Average age is: ', age
	print 'Men, Women: ', gender
	print 'Average height is: ', height
	print 'Average weight is: ', weight
	print 'Average BMI is: ', bmi
	print 'Average fat_free is: ', fatFree
	print 'Average fat_mass is: ', fatMass
	print 'Average perc_fat is: ', percFat
	print 'Average vo2max is: ', vo2max

def getSlpFeatTabl():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	
	x = sheet.nrows-1
	n = 6 
	dims = (x,n)
	feaTable = np.zeros(dims)
	
	for row in range(1,sheet.nrows):
		for i in range(n):
			feaTable[row-1][i] = sheet.cell_value(row,i+8)
			
	return feaTable
		
def getMornessLabel():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	label = [] 

	for row in range(1,sheet.nrows):
		label.append(sheet.cell_value(row,4))

	return label 

def getEvenessLabel():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	label = [] 

	for row in range(1,sheet.nrows):
		label.append(sheet.cell_value(row,5))

	return label

def getLarkLabel():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	label = [] 

	for row in range(1,sheet.nrows):
		label.append(sheet.cell_value(row,6))

	return label

def getOwlLabel():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	label = [] 

	for row in range(1,sheet.nrows):
		label.append(sheet.cell_value(row,7))

	return label

def getGender():
	file_location = 'activity/activityTableWithSleep.xls'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)
	Gender = [] 

	for row in range(1,sheet.nrows):
		Gender.append(sheet.cell_value(row,15))

	return Gender

# getDemoGInfo()
# getSlpFeatTabl()
