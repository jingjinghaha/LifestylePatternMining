# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:48:33 2016

@author: jingjing
"""
import numpy as np
import xlrd 
import xlwt 
import matplotlib.pyplot as plt 
import pandas as pd

import validation4DC
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis

d = np.array([[0, 2, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
[2, 1, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0],
[0, 0, 3, 2, 0, 0, 0, 3, 2, 2, 1, 1],
[1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
[1, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
[1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[2, 1, 1, 0, 0, 0, 1, 1, 0, 2, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0],
[1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]])

x = np.arange(13)
print d.shape

#plt.figure()
#plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7],d[:,8],d[:,9],d[:,10],d[:,11])
#plt.xlabel('days')


d = pd.DataFrame(d)
a = d[d[0]>=2]
print d.iloc[0]

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

X = validation4DC.getDietTypeTFArray4DC()
pca = PCA()
pca.fit(X)
#print pca.explained_variance_ratio_  
#print pca.get_covariance()
#print pca.fit_transform(X)

fa = FactorAnalysis()
fa.fit(X)
print fa.components_

