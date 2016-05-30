# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 14:46:56 2016

@author: wu34
"""
import xlwt
import utilise 
import dietActInfoRetrv 
import slpInfoRetrv

sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

labelsDietType = utilise.string2array('1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 1 1 1')
labelsActType = utilise.string2array('1 0 1 1 0 0 2 2 2 1 2 0 1 2 1 2 0 1 1 2 0 1 1 2 1 1 0 2 1')

def genDemoInfoDietGroups():
	groupDiet = dietActInfoRetrv.getGroups(labelsDietType)
	Age, Gender, Height, Weight, BMI, FatFree, FatMass, PercFat, Vo2max = slpInfoRetrv.getDemoGInfo() 
	SlpHours = slpInfoRetrv.getSlpHours()
	MedianHR = slpInfoRetrv.getMedianHR()
	MedianHRBefore = slpInfoRetrv.getMedianHRBefore()
	MedianHRAfter = slpInfoRetrv.getMedianHRAfter()
	
	# write the info to excel file 
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	rowW = 0 
	
	titles = ['age','men','women','height','weight','BMI','fat_free','fat_mass','perc_fat','vo2max','slpHours','medianHR','medianHRBefore','medianHRAfter']
	col = 0 
	for item in titles:
		ws.write(rowW,col,item)
		col += 1
	rowW += 1 
	
	demoDict = {} 
	
	for key in groupDiet:
	
		demoDict[key] = {}
		
		temp_Age = []
		temp_Gender = [] 
		temp_Height = []
		temp_Weight = [] 
		temp_BMI = []
		temp_FatFree = []
		temp_FatMass = []
		temp_PercFat = []
		temp_Vo2max = []
		temp_slpHours = [] 
		temp_MedianHR = []
		temp_MedianHRBefore = []
		temp_MedianHRAfter = []
		
		for index in range(len(sleep_list)):
			if sleep_list[index] in groupDiet[key]:
				temp_Age.append(Age[index])
				temp_Gender.append(Gender[index])
				temp_Height.append(Height[index])
				temp_Weight.append(Weight[index])
				temp_BMI.append(BMI[index])
				temp_FatFree.append(FatFree[index])
				temp_FatMass.append(FatMass[index])
				temp_PercFat.append(PercFat[index])
				temp_Vo2max.append(Vo2max[index])
				temp_slpHours.append(SlpHours[index])
				temp_MedianHR.append(MedianHR[index])
				temp_MedianHRBefore.append(MedianHRBefore[index])
				temp_MedianHRAfter.append(MedianHRAfter[index])
		
		demoDict[key]['age'] = sum(temp_Age)/float(len(temp_Age))
		demoDict[key]['men'] = temp_Gender.count(1.0)
		demoDict[key]['women'] = temp_Gender.count(0.0)
		demoDict[key]['height'] = sum(temp_Height)/float(len(temp_Height))
		demoDict[key]['weight'] = sum(temp_Weight)/float(len(temp_Weight))
		demoDict[key]['BMI'] = sum(temp_BMI)/float(len(temp_BMI))
		demoDict[key]['fat_free'] = sum(temp_FatFree)/float(len(temp_FatFree))
		demoDict[key]['fat_mass'] = sum(temp_FatMass)/float(len(temp_FatMass))
		demoDict[key]['perc_fat'] = sum(temp_PercFat)/float(len(temp_PercFat))
		demoDict[key]['vo2max'] = sum(temp_Vo2max)/float(len(temp_Vo2max))
		demoDict[key]['slpHours'] = sum(temp_slpHours)/float(len(temp_slpHours))
		demoDict[key]['medianHR'] = sum(temp_MedianHR)/float(len(temp_MedianHR))
		demoDict[key]['medianHRBefore'] = sum(temp_MedianHRBefore)/float(len(temp_MedianHRBefore))
		demoDict[key]['medianHRAfter'] = sum(temp_MedianHRAfter)/float(len(temp_MedianHRAfter))
		
		col = 0 
		for item in titles:
			if item in demoDict[key]:
				ws.write(rowW,col,demoDict[key][item])
				col += 1 
		rowW += 1 
	
	workbookW.save('tempDietGroupDemo.xls')
	print demoDict

def genDemoInfoActGroups():
	groupAct = dietActInfoRetrv.getGroups(labelsActType)
	Age, Gender, Height, Weight, BMI, FatFree, FatMass, PercFat, Vo2max = slpInfoRetrv.getDemoGInfo() 
	SlpHours = slpInfoRetrv.getSlpHours()
	MedianHR = slpInfoRetrv.getMedianHR()
	MedianHRBefore = slpInfoRetrv.getMedianHRBefore()
	MedianHRAfter = slpInfoRetrv.getMedianHRAfter()
	
	# write the info to excel file 
	workbookW = xlwt.Workbook()
	ws = workbookW.add_sheet('sheet1')
	rowW = 0 
	
	titles = ['age','men','women','height','weight','BMI','fat_free','fat_mass','perc_fat','vo2max','slpHours','medianHR','medianHRBefore','medianHRAfter']
	col = 0 
	for item in titles:
		ws.write(rowW,col,item)
		col += 1
	rowW += 1 
	
	demoDict = {} 
	
	for key in groupAct:
	
		demoDict[key] = {}
		
		temp_Age = []
		temp_Gender = [] 
		temp_Height = []
		temp_Weight = [] 
		temp_BMI = []
		temp_FatFree = []
		temp_FatMass = []
		temp_PercFat = []
		temp_Vo2max = []
		temp_slpHours = []
		temp_MedianHR = []
		temp_MedianHRBefore = []
		temp_MedianHRAfter = []
		
		for index in range(len(sleep_list)):
			if sleep_list[index] in groupAct[key]:
				temp_Age.append(Age[index])
				temp_Gender.append(Gender[index])
				temp_Height.append(Height[index])
				temp_Weight.append(Weight[index])
				temp_BMI.append(BMI[index])
				temp_FatFree.append(FatFree[index])
				temp_FatMass.append(FatMass[index])
				temp_PercFat.append(PercFat[index])
				temp_Vo2max.append(Vo2max[index])
				temp_slpHours.append(SlpHours[index])
				temp_MedianHR.append(MedianHR[index])
				temp_MedianHRBefore.append(MedianHRBefore[index])
				temp_MedianHRAfter.append(MedianHRAfter[index])
		
		demoDict[key]['age'] = sum(temp_Age)/float(len(temp_Age))
		demoDict[key]['men'] = temp_Gender.count(1.0)
		demoDict[key]['women'] = temp_Gender.count(0.0)
		demoDict[key]['height'] = sum(temp_Height)/float(len(temp_Height))
		demoDict[key]['weight'] = sum(temp_Weight)/float(len(temp_Weight))
		demoDict[key]['BMI'] = sum(temp_BMI)/float(len(temp_BMI))
		demoDict[key]['fat_free'] = sum(temp_FatFree)/float(len(temp_FatFree))
		demoDict[key]['fat_mass'] = sum(temp_FatMass)/float(len(temp_FatMass))
		demoDict[key]['perc_fat'] = sum(temp_PercFat)/float(len(temp_PercFat))
		demoDict[key]['vo2max'] = sum(temp_Vo2max)/float(len(temp_Vo2max))
		demoDict[key]['slpHours'] = sum(temp_slpHours)/float(len(temp_slpHours))
		demoDict[key]['medianHR'] = sum(temp_MedianHR)/float(len(temp_MedianHR))
		demoDict[key]['medianHRBefore'] = sum(temp_MedianHRBefore)/float(len(temp_MedianHRBefore))
		demoDict[key]['medianHRAfter'] = sum(temp_MedianHRAfter)/float(len(temp_MedianHRAfter))
		
		col = 0 
		for item in titles:
			if item in demoDict[key]: 
				ws.write(rowW,col,demoDict[key][item])
				col += 1 
		rowW += 1 
	
	workbookW.save('tempActGroupDemo.xls')
	print demoDict

def groupingAnalysis():

	groupDiet = dietActInfoRetrv.getGroups(labelsDietType)
	groupAct = dietActInfoRetrv.getGroups(labelsActType)
	print groupAct
	print groupDiet
					
	dd = {}
	for key1 in groupDiet:
		dd[key1] = {}
		for key2 in groupAct:
			dd[key1][key2] = 0 
			for item in groupDiet[key1]:
				if item in groupAct[key2]:
					dd[key1][key2] += 1 
	print dd 
	
	dd = {}
	for key1 in groupAct:
		dd[key1] = {}
		for key2 in groupDiet:
			dd[key1][key2] = 0 
			for item in groupAct[key1]:
				if item in groupDiet[key2]:
					dd[key1][key2] += 1 
	print dd 
			
		
	# labelsActItem = string2array('2 3 0 0 3 3 2 2 2 2 1 1 0 1 2 1 3 2 2 1 3 2 0 1 2 2 3 1 2')
	# labelsDietItem = string2array('3 3 2 2 2 2 0 2 2 2 2 3 3 2 3 2 0 2 2 3 2 2 2 2 1 2 0 1 1')

	# groupDiet = getGroups(labelsDietItem)
	# groupAct = getGroups(labelsActItem)
	# print groupAct
	# print groupDiet

	# dd = {}
	# for key1 in groupAct:
		# dd[key1] = {}
		# for key2 in groupDiet:
			# dd[key1][key2] = 0 
			# for item in groupAct[key1]:
				# if item in groupDiet[key2]:
					# dd[key1][key2] += 1 
	# print dd 
					
	# dd = {}
	# for key1 in groupDiet:
		# dd[key1] = {}
		# for key2 in groupAct:
			# dd[key1][key2] = 0 
			# for item in groupDiet[key1]:
				# if item in groupAct[key2]:
					# dd[key1][key2] += 1 
	# print dd 

def groupAnalysis():
	genDemoInfoActGroups() 
	genDemoInfoDietGroups()
	groupingAnalysis()

#groupAnalysis()


def getGroups(labels):
    import numpy as np 
    groups = {} 
    
    N = np.max(labels) + 1 

    for k in range(N):
        groups[k] = []
        class_members = labels == k
        # print class_members.shape[0]

        for i in range(class_members.shape[0]):
            if class_members[i] == True:
                groups[k].append(i)

    return groups

def groupingAnalysisNewData():

    labelsDietType = utilise.string2array('0 0 1 0 0 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 1 0 0 1 1 0 0 0 0')   
    labelsActType = utilise.string2array('1 2 0 0 0 1 2 0 1 1 2 2 0 1 0 0 1 0 1 1 0 0 1 2 1 2 2 0 0 2')
    
    groupDiet = getGroups(labelsDietType)
    groupAct = getGroups(labelsActType)
    print groupAct
    print groupDiet
				
    dd = {}
    for key1 in groupDiet:
        dd[key1] = {}
        for key2 in groupAct:
            dd[key1][key2] = 0 
            for item in groupDiet[key1]:
                if item in groupAct[key2]:
                    dd[key1][key2] += 1   
    print dd 

    dd = {}
    for key1 in groupAct:
        dd[key1] = {}
        for key2 in groupDiet:
            dd[key1][key2] = 0 
            for item in groupAct[key1]:
                if item in groupDiet[key2]:
                    dd[key1][key2] += 1 
    print dd 

groupingAnalysisNewData()

    