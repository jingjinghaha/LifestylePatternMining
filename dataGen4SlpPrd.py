# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:59:57 2016

@author: wu34
"""

import xlrd
import dietActInfoRetrv
import pandas as pd 
import numpy as np

#dframe = pd.read_csv('SlpGroupInfo.csv')

def genDailyActTypeFeatureTable():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,3)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        table.append(vector)
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def genDailyDietTypeFeatureTable():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,5)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        table.append(vector)
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def genDailyActTypeFeatureTable4DC():
    file = 'SlpGroupInfo4DC.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,3)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        table.append(vector)
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def genDailyDietTypeFeatureTable4DC():
    file = 'SlpGroupInfo4DC.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,5)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        table.append(vector)
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def genDailyActTypeFeatureTableWithP():
    file = 'SlpGroupInfoWithP.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,4)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        
        temp_vector = sheet.cell_value(row,6)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector 
        
        temp_vector = sheet.cell_value(row,8)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector 
        
        table.append(vector)
        
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def genDailyDietTypeFeatureTableWithP():
    file = 'SlpGroupInfoWithP.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    
    table = []

    for row in range(1,sheet.nrows):
        vector = sheet.cell_value(row,11)
        vector = vector.split('[')[1].split(']')[0].split(',') 
        
        temp_vector = sheet.cell_value(row,13)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector 
        
        temp_vector = sheet.cell_value(row,15)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector 
        
        temp_vector = sheet.cell_value(row,17)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector
        
        temp_vector = sheet.cell_value(row,19)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector
        
        temp_vector = sheet.cell_value(row,21)
        temp_vector = temp_vector.split('[')[1].split(']')[0].split(',')
        
        vector = vector + temp_vector
        
        table.append(vector)
        for i in range(len(vector)):
            vector[i] = int(vector[i])

    FT = np.array(table)

    return FT

def getSlpTimeLabel():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)

    labels = [] 

    for row in range(1,sheet.nrows):
        labels.append(int(sheet.cell_value(row,7)))

    labels = np.array(labels)

    return labels

def getMorningnessLabel():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)

    labels = [] 

    for row in range(1,sheet.nrows):
        labels.append(int(sheet.cell_value(row,8)))

    labels = np.array(labels)

    return labels

def getEveningnessLabel():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)

    labels = [] 

    for row in range(1,sheet.nrows):
        labels.append(int(sheet.cell_value(row,9)))

    labels = np.array(labels)

    return labels

def getLarkLabel():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)

    labels = [] 

    for row in range(1,sheet.nrows):
        labels.append(int(sheet.cell_value(row,10)))

    labels = np.array(labels)

    return labels

def getOwlLabel():
    file = 'SlpGroupInfo.xlsx'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)

    labels = [] 

    for row in range(1,sheet.nrows):
        labels.append(int(sheet.cell_value(row,11)))

    labels = np.array(labels)

    return labels

#print type(dframe.iloc[3][3])
##dframe['frequency'][0:1] = dframe['frequency'][0:1].split('[')[1].split(']')[0].split(',')
#print type(dframe.iloc[0][3])
#
#print type(dframe['SubjId'])
#print dframe.ix[1]

#FT = genDailyActTypeFeatureTable()
#print FT.shape
#for i in range(FT.shape[0]):
#    print FT[i]
#
#FT2 = genDailyDietTypeFeatureTable()
#print FT2.shape
##for i in range(FT2.shape[0]):
##    print FT2[i]
#
#print getSlpTimeLabel()
#print getMorningnessLabel()
#print getEveningnessLabel()
