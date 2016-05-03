# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:19:50 2016

@author: wu34
"""


import artificialDataGenerator
import numpy as np
import pandas as pd 
import copy

def originalData():
    df,cols = artificialDataGenerator.originalData() 
    
    dd = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        dd[i] = [0,0,0] 
        temp = df[df[i]>0]
    #    dd[i][0] = temp[temp['label']==0].shape[0] 
    #    dd[i][1] = temp[temp['label']==1].shape[0]
    #    dd[i][2] = temp[temp['label']==2].shape[0]
        dd[i][0] = sum(temp[temp['label']==0][i])
        dd[i][1] = sum(temp[temp['label']==1][i])
        dd[i][2] = sum(temp[temp['label']==2][i])
        ll = copy.deepcopy(dd)
        dd[i][0] = dd[i][0]/float(sum(ll[i]))
        dd[i][1] = dd[i][1]/float(sum(ll[i]))
        dd[i][2] = dd[i][2]/float(sum(ll[i]))
        dd_low[i] = dd[i][0] + dd[i][1]
        dd_high[i] = dd[i][1] + dd[i][2]
        
    temp = df[df['workStudy']>0]
    print temp[temp['label']==2].shape
    
    return dd_low,dd_high

def artificialData():
    df,labels = artificialDataGenerator.artificialData()
    print df.columns 
    
    dd = {}
    dd_low = {}
    dd_high = {}
    for i in df.columns:
        dd[i] = [0,0,0] 
        temp = df[df[i]>0]
    #    dd[i][0] = temp[temp['label']==0].shape[0] 
    #    dd[i][1] = temp[temp['label']==1].shape[0]
    #    dd[i][2] = temp[temp['label']==2].shape[0]
        dd[i][0] = sum(temp[temp['label']==0][i])
        dd[i][1] = sum(temp[temp['label']==1][i])
        dd[i][2] = sum(temp[temp['label']==2][i])
        ll = copy.deepcopy(dd)
        dd[i][0] = dd[i][0]/float(sum(ll[i]))
        dd[i][1] = dd[i][1]/float(sum(ll[i]))
        dd[i][2] = dd[i][2]/float(sum(ll[i]))
        dd_low[i] = dd[i][0] + dd[i][1]
        dd_high[i] = dd[i][1] + dd[i][2]
        
    temp = df[df['workStudy']>0]
    print temp[temp['label']==2].shape
    
    return dd_low,dd_high

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

def bikeAnalysis():
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
dd_low,dd_high = artificialData()
