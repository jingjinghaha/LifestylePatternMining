# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:26:50 2016

@author: wu34
"""

import xlwt
import xlrd
import slpInfoRetrv
sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def buildSubAveInfo():
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	
	Age, Gender, Height, Weight, BMI, FatFree, FatMass, PercFat, Vo2max = slpInfoRetrv.getDemoGInfo() 
	SlpHours = slpInfoRetrv.getSlpHours()
	MedianHR = slpInfoRetrv.getMedianHR() 
	MedianHRBefore = slpInfoRetrv.getMedianHRBefore() 
	MedianHRAfter = slpInfoRetrv.getMedianHRAfter() 
	
	titles = ['SubjId','HoursSleep','MedianHR','MedianHRBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
	
	for i in range(len(titles)):
		ws.write(0,i,titles[i])
	
	rowW = 1 
	
	for index in range(len(sleep_list)): 
		ws.write(rowW,0,sleep_list[index])
		ws.write(rowW,1,SlpHours[index])
		ws.write(rowW,2,MedianHR[index])
		ws.write(rowW,3,MedianHRBefore[index])
		ws.write(rowW,4,MedianHRAfter[index])
		ws.write(rowW,5,Age[index])
		ws.write(rowW,6,Gender[index])
		ws.write(rowW,7,Height[index])
		ws.write(rowW,8,Weight[index])
		ws.write(rowW,9,BMI[index])
		ws.write(rowW,10,FatFree[index])
		ws.write(rowW,11,FatMass[index])
		ws.write(rowW,12,PercFat[index])
		ws.write(rowW,13,Vo2max[index])
		rowW += 1 
	
	workbookW.save('SubAveInfo.xls')

buildSubAveInfo()
