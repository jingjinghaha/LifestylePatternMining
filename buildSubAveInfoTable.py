# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:26:50 2016

@author: wu34
"""

import xlwt
import slpInfoRetrv
import dietActInfoRetrv
sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

labelsDietType = dietActInfoRetrv.string2array('0 1 2 1 2 0 1 2 2 3 3 0 2 2 2 2 0 1 2 0 2 2 2 2 3 2 1 3 3')
labelsActType = dietActInfoRetrv.string2array('1 3 1 1 2 2 2 2 3 1 2 2 1 2 0 2 3 0 1 2 3 1 1 2 1 0 2 0 0')

def buildSubAveInfo():
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	
	groupAct = dietActInfoRetrv.getGroups(labelsActType)
	groupDiet = dietActInfoRetrv.getGroups(labelsDietType)
	
	Age, Gender, Height, Weight, BMI, FatFree, FatMass, PercFat, Vo2max = slpInfoRetrv.getDemoGInfo() 
	SlpHours = slpInfoRetrv.getSlpHours()
	MedianHR = slpInfoRetrv.getMedianHR() 
	MedianHRBefore = slpInfoRetrv.getMedianHRBefore() 
	MedianHRAfter = slpInfoRetrv.getMedianHRAfter() 
	
	titles = ['SubjId','ActGroup','DietGroup','HoursSleep','MedianHR','MedianHRBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
	
	for i in range(len(titles)):
		ws.write(0,i,titles[i])
	
	rowW = 1 
	
	for index in range(len(sleep_list)): 
		ws.write(rowW,0,sleep_list[index])
		
		for key in groupAct: 
			if sleep_list[index] in groupAct[key]:
				ws.write(rowW,1,key)
				break 
				
		for key in groupDiet:
			if sleep_list[index] in groupDiet[key]:
				ws.write(rowW,2,key)
				break
				
		ws.write(rowW,1+2,SlpHours[index])
		ws.write(rowW,2+2,MedianHR[index])
		ws.write(rowW,3+2,MedianHRBefore[index])
		ws.write(rowW,4+2,MedianHRAfter[index])
		ws.write(rowW,5+2,Age[index])
		ws.write(rowW,6+2,Gender[index])
		ws.write(rowW,7+2,Height[index])
		ws.write(rowW,8+2,Weight[index])
		ws.write(rowW,9+2,BMI[index])
		ws.write(rowW,10+2,FatFree[index])
		ws.write(rowW,11+2,FatMass[index])
		ws.write(rowW,12+2,PercFat[index])
		ws.write(rowW,13+2,Vo2max[index])
		rowW += 1 
	
	workbookW.save('SubAveInfo.xls')

buildSubAveInfo()
