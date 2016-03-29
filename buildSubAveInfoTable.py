# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:26:50 2016

@author: wu34
"""

import xlwt
import utilise
import dataGen4DietAct
import slpInfoRetrv
import dietActInfoRetrv
import validation4DC
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

labelsDietType = utilise.string2array('1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 1 1 1')
labelsActType = utilise.string2array('1 0 1 1 0 0 2 2 2 1 2 0 1 2 1 2 0 1 1 2 0 1 1 2 1 1 0 2 1')

def buildSubAveInfo():
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('AveInfo')
    
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
    
    ws2 = workbookW.add_sheet('DietTF')
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
    
    X = utilise.normArray(dataGen4DietAct.genDietTypeTFArray())

    ws2.write(0,0,'SubjId')
    ws2.write(0,1,'DietGroup')

    for i in range(len(row_labels)):
        ws2.write(0,i+2,row_labels[i])

    rowW = 1 
    for index in range(len(available_list)):
        ws2.write(rowW,0,available_list[index])

        for key in groupDiet:
            if available_list[index] in groupDiet[key]:
                ws2.write(rowW,1,key)
                break

        for i in range(len(row_labels)):
            ws2.write(rowW,i+2,X[index][i])

        rowW += 1

    ws3 = workbookW.add_sheet('ActTF')
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
    
    X = utilise.normArray(dataGen4DietAct.genActTypeTFArray())

    ws3.write(0,0,'SubjId')
    ws3.write(0,1,'ActGroup')
    
    for i in range(len(row_labels)):
        ws3.write(0,i+2,row_labels[i])

    rowW = 1 
    for index in range(len(available_list)):
        ws3.write(rowW,0,available_list[index])

        for key in groupAct: 
            if available_list[index] in groupAct[key]:
                ws3.write(rowW,1,key)
                break 

        for i in range(len(row_labels)):
            ws3.write(rowW,i+2,X[index][i])

        rowW += 1

    workbookW.save('SubAveInfo.xls')

def buildSubAveInfo4DC():
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('AveInfo')
    
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
    
    ws2 = workbookW.add_sheet('DietTF')
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
    
    X = utilise.normArray(validation4DC.getDietTypeTFArray4DC())

    ws2.write(0,0,'SubjId')
    ws2.write(0,1,'DietGroup')

    for i in range(len(row_labels)):
        ws2.write(0,i+2,row_labels[i])

    rowW = 1 
    for index in range(len(available_list)):
        ws2.write(rowW,0,available_list[index])

        for key in groupDiet:
            if available_list[index] in groupDiet[key]:
                ws2.write(rowW,1,key)
                break

        for i in range(len(row_labels)):
            ws2.write(rowW,i+2,X[index][i])

        rowW += 1

    ws3 = workbookW.add_sheet('ActTF')
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
    
    X = utilise.normArray(validation4DC.getActTypeTFArray4DC())

    ws3.write(0,0,'SubjId')
    ws3.write(0,1,'ActGroup')
    
    for i in range(len(row_labels)):
        ws3.write(0,i+2,row_labels[i])

    rowW = 1 
    for index in range(len(available_list)):
        ws3.write(rowW,0,available_list[index])

        for key in groupAct: 
            if available_list[index] in groupAct[key]:
                ws3.write(rowW,1,key)
                break 

        for i in range(len(row_labels)):
            ws3.write(rowW,i+2,X[index][i])

        rowW += 1

    workbookW.save('SubAveInfo.xls')

#buildSubAveInfo()
buildSubAveInfo4DC()
