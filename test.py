# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:48:33 2016
@author: jingjing
"""

'''
stack plot 
'''
#import numpy as np
#import matplotlib.pyplot as plt 
#
#d = np.array([[0, 2, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
#              [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
#[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
#[2, 1, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0],
#[0, 0, 3, 2, 0, 0, 0, 3, 2, 2, 1, 1],
#[1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 1, 0],
#[1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
#[1, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
#[1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
#[0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
#[2, 1, 1, 0, 0, 0, 1, 1, 0, 2, 1, 1],
#[1, 1, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0],
#[1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]])
#
#x = np.arange(13)
#print d.shape

#plt.figure()
#plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7],d[:,8],d[:,9],d[:,10],d[:,11])
#plt.xlabel('days')




'''
excel operation 
'''
#import xlrd 
#import xlwt 
#location = 'slpGroupInfo.xls'
#workbookR = xlrd.open_workbook(location)
#sheet = workbookR.sheet_by_index(0) 
#
#workbookW = xlwt.Workbook()
#ws = workbookW.add_sheet('sheet1')
#
#for i in range(2,sheet.nrows):
#    if sheet.cell_value(i,0) == sheet.cell_value(i-1,0):
#        date = sheet.cell_value(i,1) 
#        previous_date = sheet.cell_value(i-1,1)

'''
PCA and factor analysis 
'''
#import validation4DC
#from sklearn.decomposition import PCA
#from sklearn.decomposition import FactorAnalysis

#X = validation4DC.getDietTypeTFArray4DC()
#pca = PCA()
#pca.fit(X)
##print pca.explained_variance_ratio_  
##print pca.get_covariance()
##print pca.fit_transform(X)
#
#fa = FactorAnalysis()
#fa.fit(X)
#print fa.components_

'''
df test 
'''
import dataGen4SlpPrd
import numpy as np
import pandas as pd 
import copy
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

col1 = dataGen4SlpPrd.genDietTypeLabel()
col2 = dataGen4SlpPrd.genActTypeLabel()
cols = col1+col2
cols.append('gender')
cols.append('sleepTime')
cols.append('label')

print cols 
dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
gender = dataGen4SlpPrd.getGender()
dataset = np.c_[dataset,gender.ravel()]

time = dataGen4SlpPrd.getSlpTime() 
dataset = np.c_[dataset,time.ravel()]

label1 = dataGen4SlpPrd.getSlpTimeLabel()
dataset_l1 = np.c_[dataset,label1.ravel()]
df = pd.DataFrame(dataset_l1,columns=cols)

dd = {}
dd_low = {}
dd_high = {}
for i in df.columns:
    if i != 'label':
        dd[i] = [0,0,0] 
        temp = df[df[i]>0]
    #    dd[i][0] = temp[temp['label']==0].shape[0] 
    #    dd[i][1] = temp[temp['label']==1].shape[0]
    #    dd[i][2] = temp[temp['label']==2].shape[0]
#        if temp[temp['label']==0].shape[0] == 0:
#            print i 
#            break 
        dd[i][0] = sum(temp[temp['label']==0][i])#/(temp[temp['label']==0].shape[0])
        dd[i][1] = sum(temp[temp['label']==1][i])#/(temp[temp['label']==1].shape[0])
        dd[i][2] = sum(temp[temp['label']==2][i])#/(temp[temp['label']==2].shape[0])
        ll = copy.deepcopy(dd)
        dd[i][0] = dd[i][0]/float(sum(ll[i]))
        dd[i][1] = dd[i][1]/float(sum(ll[i]))
        dd[i][2] = dd[i][2]/float(sum(ll[i]))
        dd_low[i] = dd[i][0] + dd[i][1]
        dd_high[i] = dd[i][1] + dd[i][2]
    
temp = df[df['workStudy']>0]
print temp[temp['label']==2].shape

#a = df[df['label']==0]
#b = a.mean().to_frame()
#a = df[df['label']==1]
#b[1] = a.mean().to_frame() 
#a = df[df['label']==2]
#b[2] = a.mean().to_frame() 
#
#
#print df.mean() 
#print df.std() 
##df.plot.box(vert=False)
##scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
#print type(df['cafeSnack']) 
#se = df['cafeSnack']
##se.hist()
#
#a = df[df['label']==0]
#b = df[df['label']==1]
#c = df[df['label']==2]
#
#for i in df.columns:
#    if i != 'label':
#        plt.figure()
#        a[i].plot.kde(label='Group0')
#        b[i].plot.kde(label='Group1')
#        c[i].plot.kde(label='Group2')
#        df[i].plot.kde(label='all')
##        df[i].hist()
#        if i == 'transportation1':
#            i = 'walk'
#        if i == 'transportation2':
#            i = 'car'
#        if i == 'transportation3':
#            i = 'bike' 
#        plt.legend()
#        plt.title(i)
#        plt.savefig('distribution/'+i)
#    

