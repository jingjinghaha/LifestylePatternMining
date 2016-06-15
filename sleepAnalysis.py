# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:19:50 2016

@author: wu34
"""


import artificialDataGenerator
import newDataProcess 
import numpy as np
import pandas as pd 
import copy

def originalData():
    df = artificialDataGenerator.originalData() 
    print df.columns 
    df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy','gender','label']]
    df.columns = ['alcohol','cafe','dairy','egg','fruit','grain','meat','seafood','snack','starchy','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label']
    
    dd = {}
    dd_low = {}
    dd_high = {}
    dd_diff = {}
    for i in df.columns:
        if i != 'label':
            dd[i] = [0,0] 
            temp = df[df[i]>0]
            
#            dd[i][0] = temp[temp['label']==0].shape[0] 
#            dd[i][1] = temp[temp['label']==1].shape[0]
#            dd[i][2] = temp[temp['label']==2].shape[0]
#            
#            dd[i][0] = sum(temp[temp['label']==0][i])
#            dd[i][1] = sum(temp[temp['label']==1][i])
#            dd[i][2] = sum(temp[temp['label']==2][i])
            
#            dd[i][0] = sum(temp[temp['label']==0][i])/(temp[temp['label']==0].shape[0])
#            dd[i][1] = sum(temp[temp['label']==1][i])/(temp[temp['label']==1].shape[0])
#            dd[i][2] = sum(temp[temp['label']==2][i])/(temp[temp['label']==2].shape[0])
#            ll = copy.deepcopy(dd)
#            dd[i][0] = dd[i][0]/float(sum(ll[i]))
#            dd[i][1] = dd[i][1]/float(sum(ll[i]))
#            dd[i][2] = dd[i][2]/float(sum(ll[i]))
#            dd_low[i] = dd[i][0] #+ dd[i][1]
#            dd_high[i] = dd[i][2] #+ dd[i][1]
#            dd_diff[i] = max(dd[i])-min(dd[i])
            
            dd[i][0] = sum(temp[temp['label']==0][i])/sum(df[i])
            dd[i][1] = sum(temp[temp['label']==1][i])/sum(df[i])
#            dd[i][2] = sum(temp[temp['label']==2][i])/sum(df[i])
            
#            dd[i][0] = float(temp[temp['label']==0][i].shape[0])/temp.shape[0]
#            dd[i][1] = float(temp[temp['label']==1][i].shape[0])/temp.shape[0]
#            dd[i][2] = float(temp[temp['label']==2][i].shape[0])/temp.shape[0]
            
            dd_low[i] = dd[i][0] 
            dd_high[i] = dd[i][1]
            dd_diff[i] = max(dd[i])-min(dd[i])
    
    return dd,dd_low,dd_high,dd_diff

#dd,dd_low,dd_high,dd_diff = originalData()

def artificialData():
    df = artificialDataGenerator.artificialData()
    print df.columns 
    df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy','gender','label']]
    df.columns = ['alcohol','cafe','dairy','egg','fruit','grain','meat','seafood','snack','starchy','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label']
    
    dd = {}
    dd_low = {}
    dd_high = {}
    dd_diff = {}
    for i in df.columns:
        if i != 'label':
            dd[i] = [0,0] 
            temp = df[df[i]>0]
#            dd[i][0] = temp[temp['label']==0].shape[0] 
#            dd[i][1] = temp[temp['label']==1].shape[0]
#            dd[i][2] = temp[temp['label']==2].shape[0]
#            
#            dd[i][0] = sum(temp[temp['label']==0][i])
#            dd[i][1] = sum(temp[temp['label']==1][i])
#            dd[i][2] = sum(temp[temp['label']==2][i])
            
#            dd[i][0] = sum(temp[temp['label']==0][i])/(temp[temp['label']==0].shape[0])
#            dd[i][1] = sum(temp[temp['label']==1][i])/(temp[temp['label']==1].shape[0])
#            dd[i][2] = sum(temp[temp['label']==2][i])/(temp[temp['label']==2].shape[0])
#            ll = copy.deepcopy(dd)
#            dd[i][0] = dd[i][0]/float(sum(ll[i]))
#            dd[i][1] = dd[i][1]/float(sum(ll[i]))
#            dd[i][2] = dd[i][2]/float(sum(ll[i]))
#            dd_low[i] = dd[i][0] #+ dd[i][1]
#            dd_high[i] = dd[i][2] #+ dd[i][1]
#            dd_diff[i] = max(dd[i])-min(dd[i])
            
            dd[i][0] = float(sum(temp[temp['label']==0][i]))/sum(df[i])
            dd[i][1] = float(sum(temp[temp['label']==1][i]))/sum(df[i])
#            dd[i][2] = sum(temp[temp['label']==2][i])/sum(df[i])
            
#            dd[i][0] = float(temp[temp['label']==0][i].shape[0])/temp.shape[0]
#            dd[i][1] = float(temp[temp['label']==1][i].shape[0])/temp.shape[0]
#            dd[i][2] = float(temp[temp['label']==2][i].shape[0])/temp.shape[0]
            
            dd_low[i] = dd[i][0] 
            dd_high[i] = dd[i][1]
            dd_diff[i] = max(dd[i])-min(dd[i])
    
    return dd,dd_low,dd_high,dd_diff

dd,dd_low,dd_high,dd_diff = artificialData()

def newData():
    df = newDataProcess.newFeatureFrame()
    print df.columns 
    df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label']]
    df.columns = ['alcohol','cafe','dairy','egg','fruit','grain','meat','seafood','snack','starchy','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label']
    
    dd = {}
    dd_low = {}
    dd_high = {}
    dd_diff = {} 
    for i in df.columns:
        if i != 'label':
            dd[i] = [0,0] 
            temp = df[df[i]>0]
            
#            dd[i][0] = temp[temp['label']==0].shape[0] 
#            dd[i][1] = temp[temp['label']==1].shape[0]
#            dd[i][2] = temp[temp['label']==2].shape[0]
#            
#            dd[i][0] = sum(temp[temp['label']==0][i])
#            dd[i][1] = sum(temp[temp['label']==1][i])
#            dd[i][2] = sum(temp[temp['label']==2][i])
            
#            dd[i][0] = sum(temp[temp['label']==0][i])/(temp[temp['label']==0].shape[0])
#            dd[i][1] = sum(temp[temp['label']==1][i])/(temp[temp['label']==1].shape[0])
#            dd[i][2] = sum(temp[temp['label']==2][i])/(temp[temp['label']==2].shape[0])
#            ll = copy.deepcopy(dd)
#            dd[i][0] = dd[i][0]/float(sum(ll[i]))
#            dd[i][1] = dd[i][1]/float(sum(ll[i]))
#            dd[i][2] = dd[i][2]/float(sum(ll[i]))
#            dd_low[i] = dd[i][0] #+ dd[i][1]
#            dd_high[i] = dd[i][2] #+ dd[i][1]
#            dd_diff[i] = max(dd[i])-min(dd[i])
            
            dd[i][0] = sum(temp[temp['label']==0][i])/sum(df[i])
            dd[i][1] = sum(temp[temp['label']==1][i])/sum(df[i])
#            dd[i][2] = sum(temp[temp['label']==2][i])/sum(df[i])
            
#            dd[i][0] = float(temp[temp['label']==0][i].shape[0])/temp.shape[0]
#            dd[i][1] = float(temp[temp['label']==1][i].shape[0])/temp.shape[0]
#            dd[i][2] = float(temp[temp['label']==2][i].shape[0])/temp.shape[0]
            
            dd_low[i] = dd[i][0] 
            dd_high[i] = dd[i][1]
            dd_diff[i] = max(dd[i])-min(dd[i])

    return dd,dd_low,dd_high,dd_diff

#dd,dd_low,dd_high,dd_diff = newData()

def supportDict():
    dd,dd_low1,dd_high1,dd_diff1 = originalData()
    dd,dd_low2,dd_high2,dd_diff2 = artificialData()
    dd,dd_low3,dd_high3,dd_diff3 = newData()
    
    dd_low = {}
    dd_high = {}
    dd_diff = {}
    for i in dd_low1.keys():
        dd_low[i] = [0,0,0]
        dd_high[i] = [0,0,0]
        dd_diff[i] = [0,0,0]
        dd_low[i][0] = dd_low1[i]
        dd_low[i][1] = dd_low2[i]
        dd_low[i][2] = dd_low3[i]
        dd_high[i][0] = dd_high1[i]
        dd_high[i][1] = dd_high2[i]
        dd_high[i][2] = dd_high3[i]
        dd_diff[i][0] = dd_diff1[i]
        dd_diff[i][1] = dd_diff2[i]
        dd_diff[i][2] = dd_diff3[i]
    return dd_low,dd_high,dd_diff
  
#dd_low,dd_high,dd_diff = supportDict()


def originalDataSubSupport():
    df = artificialDataGenerator.originalData() 
    print df.columns 
    df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy','gender','label','ID']]
    df.columns = ['alcohol','cafe','dairy','egg','fruit','grain','meat','seafood','snack','starchy','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label','ID']
    
    for i in range(df.shape[0]):    
        df.set_value(i,'ID',int(df['ID'][i]))
    
    sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
    
    dd_low_list = {}
    dd_high_list = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        if i != 'label' and i != 'ID':
            dd_low_list[i] = []
            dd_high_list[i] = []
        
    for sub in sleep_list:
        
        ID = int(sub)
        df_sub = df[df['ID']==ID]

        for i in df.columns:
            if i != 'label' and i != 'ID':
                
                temp = df_sub[df_sub[i]>0]
                if sum(df_sub[i]) != 0:
                    dd_low_list[i].append(sum(temp[temp['label']==0][i])/sum(df_sub[i])) 
                    dd_high_list[i].append(sum(temp[temp['label']==1][i])/sum(df_sub[i]))
#                else:
#                    dd_low_list[i].append(0)
#                    dd_high_list[i].append(0)
    
    for i in dd_low_list.keys():
        dd_low[i] = sum(dd_low_list[i])/len(dd_low_list[i])
        dd_high[i] = sum(dd_high_list[i])/len(dd_high_list[i])
    
    return dd_low,dd_high

#dd_low,dd_high = originalDataSubSupport()

def newDataSubSupport():
    df = newDataProcess.newFeatureFrame()
    print df.columns 
    df = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label','ID']]
    df.columns = ['alcohol','cafe','dairy','egg','fruit','grain','meat','seafood','snack','starchy','vegetables','leisure','social','sport','walk','car','bike','workStudy','gender','label','ID']
    
    for i in range(df.shape[0]):    
        df.set_value(i,'ID',int(df['ID'][i]))
    
    dd_low_list = {}
    dd_high_list = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        if i != 'label' and i != 'ID':
            dd_low_list[i] = []
            dd_high_list[i] = []
        
    for sub in range(30):
        
        ID = int(sub)
        df_sub = df[df['ID']==ID]

        for i in df.columns:
            if i != 'label' and i != 'ID':
                
                temp = df_sub[df_sub[i]>0]
                if sum(df_sub[i]) != 0:
                    dd_low_list[i].append(sum(temp[temp['label']==0][i])/sum(df_sub[i])) 
                    dd_high_list[i].append(sum(temp[temp['label']==1][i])/sum(df_sub[i]))
#                else:
#                    dd_low_list[i].append(0)
#                    dd_high_list[i].append(0)
    
    for i in dd_low_list.keys():
        dd_low[i] = sum(dd_low_list[i])/len(dd_low_list[i])
        dd_high[i] = sum(dd_high_list[i])/len(dd_high_list[i])
    
    return dd_low,dd_high

#dd_low,dd_high = newDataSubSupport()

def genderAnalysis():
    df,labels = artificialDataGenerator.artificialData() 
    df1 = df[df['gender']==1] 
    print 'the total appearance of bike in men is '
    print sum(df1['transportation3'])
    print 'the number of men in the dataset is '
    print (df1.shape[0])
    df2 = df[df['gender']==0]
    print 'the total appearance of bike in women is ' 
    print sum(df2['transportation3'])
    print 'the number of women in the dataset is ' 
    print (df2.shape[0])

#def bikeAnalysis():
    df,labels = artificialDataGenerator.artificialData() 
    df1 = df[df['transportation3']>=1] 
    print 'the total appearance of work/study in people who bike is '
    print sum(df1['workStudy'])
    print 'the number of people who bike in the dataset is '
    print (df1.shape[0])
    df2 = df[df['transportation3']==0]
    print "the total appearance of work/study in people who not bike is " 
    print sum(df2['workStudy'])
    print 'the number of people who not bike in the dataset is ' 
    print (df2.shape[0])

def walkAnalysis():
    df,labels = artificialDataGenerator.artificialData() 
    df1 = df[df['transportation1']>=1] 
    print 'the total appearance of cafe in people who walk is '
    print sum(df1['caffeineD'])
    print 'the number of people who walk in the dataset is '
    print (df1.shape[0])
    df2 = df[df['transportation1']==0]
    print "the total appearance of cafe in people who not walk is " 
    print sum(df2['caffeineD'])
    print 'the number of people who not walk in the dataset is ' 
    print (df2.shape[0])

#walkAnalysis()

