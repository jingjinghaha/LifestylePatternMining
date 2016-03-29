# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:47:04 2016

@author: wu34
"""

import xlwt
import xlrd
import utilise
import dataGen4DietAct
import buildTypeIndex 

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
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
    

    for rowR in range(8,sheet.nrows):
    
        if sheet.cell_value(rowR,0):

            index += 1

            dd = {}
            PList = ['P1','P2','P3']
            for key in PList:
                dd[key] = {}
            
            for key in dd: 
                for label in row_labels:
                    dd[key][label] = 0

            temp = buildTypeIndex.build_daily_single_activity_index_with_time4DC(subjectID,index)
            
            for key in dd: 
                for type in temp[key]:
                    if type in dd[key]:
                        dd[key][type] = temp[key][type] 

            ws.write(rowW,0,subjectID)
            ws.write(rowW,1,sheet.cell_value(rowR,0))
            ws.write(rowW,2,str(dd['P1'].keys()))
            ws.write(rowW,3,'P1')
            ws.write(rowW,4,str(dd['P1'].values()))
            ws.write(rowW,5,'P2')
            ws.write(rowW,6,str(dd['P2'].values()))
            ws.write(rowW,7,'P3')
            ws.write(rowW,8,str(dd['P3'].values()))
            rowW += 1
            
    workbookW.save('activity/activityTable_'+subjectID+'_withFreqP.xls')

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
    
    row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())

    for rowR in range(8,sheet.nrows):

        if sheet.cell_value(rowR,0):
        
            index += 1 

            dd = {}
            PList = ['P1','P2','P3','P4','P5','P6']
            for key in PList:
                dd[key] = {}
            
            for key in dd: 
                for label in row_labels:
                    dd[key][label] = 0

            temp = buildTypeIndex.build_daily_single_diet_index_with_time4DC(subjectID,index)
            
            for key in dd: 
                for type in temp[key]:
                    if type in dd[key]:
                        dd[key][type] = temp[key][type] 

            ws.write(rowW,0,subjectID)
            ws.write(rowW,1,sheet.cell_value(rowR,0))
            ws.write(rowW,2,str(dd['P1'].keys()))
            ws.write(rowW,3,'P1')
            ws.write(rowW,4,str(dd['P1'].values()))
            ws.write(rowW,5,'P2')
            ws.write(rowW,6,str(dd['P2'].values()))
            ws.write(rowW,7,'P3')
            ws.write(rowW,8,str(dd['P3'].values()))
            ws.write(rowW,9,'P4')
            ws.write(rowW,10,str(dd['P4'].values()))
            ws.write(rowW,11,'P5')
            ws.write(rowW,12,str(dd['P5'].values()))
            ws.write(rowW,13,'P6')
            ws.write(rowW,14,str(dd['P6'].values()))
            rowW += 1

    workbookW.save('diet/dietTable_'+subjectID+'_withFreqP.xls')

def buildActExcel():
    '''
    build activity excel for all the subjects, including the date, activity item and type
    '''
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')

    rowW = 0

    for subjectID in available_list:
        file_location = 'activity/activityTable_'+subjectID+'_withFreqP.xls'
        workbookR = xlrd.open_workbook(file_location)
        sheet = workbookR.sheet_by_index(0)

        for rowR in range(0,sheet.nrows):
            for colR in range(0,sheet.ncols):
                ws.write(rowW,colR,sheet.cell_value(rowR,colR))
            rowW += 1

    workbookW.save('activity/activityTable_withFreqP.xls')

def buildDietExcel():
    '''
    build diet excel for all the subjects, including the date, diet item and type
    '''
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')

    rowW = 0

    for subjectID in available_list:
        file_location = 'diet/dietTable_'+subjectID+'_withFreqP.xls'
        workbookR = xlrd.open_workbook(file_location)
        sheet = workbookR.sheet_by_index(0)
        
        for rowR in range(0,sheet.nrows):
            for colR in range(0,sheet.ncols):
                ws.write(rowW,colR,sheet.cell_value(rowR,colR))
            rowW += 1

    workbookW.save('diet/dietTable_withFreqP.xls')

def buildActWithSleepExcel():
    '''
    build activity excel for all the subjects, including the date, activity item and type, sleep
    '''
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    titles = ['SubjId','Day','ActType','Period','frequency','Period','frequency','Period','frequency','Morningness','Eveningness','Lark','Owl','HoursSleep','SleepMoveCount','SleepQuality','MedianHR','MedianBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
    
    for i in range(len(titles)):
        ws.write(0,i,titles[i])

    rowW = 1
    file_location1 = 'activity/activityTable_withFreqP.xls'
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
                                    for i in range(2,9):
                                        ws.write(rowW,i,sheet1.cell_value(rowRAct-1,i))
                                
                                else: 
                                    break
                            else:
                                break 
                        else:
                            day = sheet2.cell_value(rowRSlp,1)
                            temp = int(day.split('.')[1])
                            day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
                            for i in range(2,9):
                                ws.write(rowW,i,sheet1.cell_value(rowRAct,i))
                    else: 
                        day = sheet2.cell_value(rowRSlp,1)
                        temp = int(day.split('.')[1])
                        day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
                        for i in range(2,9):
                            ws.write(rowW,i,sheet1.cell_value(rowRAct,i))
                    
                    ws.write(rowW,0,sub)
                    ws.write(rowW,1,day)
                    for i in range(9,28):
                        ws.write(rowW,i,sheet2.cell_value(rowRSlp,i-4))
                    rowW += 1

    workbookW.save('activity/activityTableWithSleep_withFreqP.xls')

def buildDietWithSleepExcel():
    '''
    build diet excel for all the subjects, including the date, activity item and type, sleep
    '''
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    titles = ['SubjId','Day','DietType','Period','frequency','Period','frequency','Period','frequency','Period','frequency','Period','frequency','Period','frequency','Morningness','Eveningness','Lark','Owl','HoursSleep','SleepMoveCount','SleepQuality','MedianHR','MedianBefore','MedianHRAfter','age','gender','height','weight','BMI','FatFreeMass','FatMass','PercFat','vo2max']
    
    for i in range(len(titles)):
        ws.write(0,i,titles[i])

    rowW = 1
    file_location1 = 'diet/dietTable_withFreqP.xls'
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
                                    for i in range(2,15):
                                        ws.write(rowW,i,sheet1.cell_value(rowRDiet-1,i))
                                else: 
                                    break
                            else:
                                break 
                        else:
                            day = sheet2.cell_value(rowRSlp,1)
                            temp = int(day.split('.')[1])
                            day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
                            for i in range(2,15):
                                ws.write(rowW,i,sheet1.cell_value(rowRDiet,i))
                    else: 
                        day = sheet2.cell_value(rowRSlp,1)
                        temp = int(day.split('.')[1])
                        day = day.split('.')[0]+'.'+str(temp)+'.'+day.split('.')[2]
                        for i in range(2,15):
                            ws.write(rowW,i,sheet1.cell_value(rowRDiet,i))
                    
                    ws.write(rowW,0,sub)
                    ws.write(rowW,1,day)
                    for i in range(15,34):
                        ws.write(rowW,i,sheet2.cell_value(rowRSlp,i-10))

                    rowW += 1

    workbookW.save('diet/dietTableWithSleep_withFreqP.xls')

def buildDietActTableWithSlpWithFreq():
    for subjectID in available_list:
        buildSingleActExcel(subjectID)
        buildSingleDietExcel(subjectID)

    buildActExcel()
    buildDietExcel()

    buildActWithSleepExcel()
    buildDietWithSleepExcel()

buildDietActTableWithSlpWithFreq() 
