# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:33:36 2016

@author: jingjing
"""

import matplotlib.pyplot as plt
import dataGen4DietAct 
import utilise 
import pandas as pd 

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def visDailyPatternStack():
    
    for sub in available_list:
        d = dataGen4DietAct.genDailySingleActTypeTFArray(sub)
        
#        for i in range(d.shape[0]):
#            for j in range(d.shape[1]):
#                if d[i][j] > 1:
#                    d[i][j] = 1
        labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
        df = pd.DataFrame(d,columns=labels)
#        x = np.arange(d.shape[0])
#        plt.figure()
#        plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7])
#        plt.title('DailyActivityPattern_'+sub)
#        plt.xlabel('days')
#        plt.savefig('visDailyActTypePattStack/DailyActivityPattern_'+sub)
        
        df.plot.bar(stacked = True)
#        df.plot.area()
        plt.title('DailyActivityPattern_'+sub)
        plt.xlabel('days')
        plt.savefig('visDailyActTypePattStack/DailyActivityPattern_'+sub)
    
    for sub in available_list:
        d = dataGen4DietAct.genDailySingleDietTypeTFArray(sub)
        
#        for i in range(d.shape[0]):
#            for j in range(d.shape[1]):
#                if d[i][j] > 1:
#                    d[i][j] = 1
        labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
        df = pd.DataFrame(d,columns=labels)
#        x = np.arange(d.shape[0])
#        plt.figure()
#        plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7],d[:,8],d[:,9],d[:,10],d[:,11])
#        plt.title('DailyDietPattern_'+sub)
#        plt.xlabel('days')
#        plt.savefig('visDailyDietTypePattStack/DailyDietPattern_'+sub)
        
        df.plot.bar(stacked = True)
#        df.plot.area()
        plt.title('DailyDietPattern_'+sub)
        plt.xlabel('days')
        plt.savefig('visDailyDietTypePattStack/DailyDietPattern_'+sub)
    
visDailyPatternStack()
