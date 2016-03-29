# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:33:36 2016

@author: jingjing
"""

import matplotlib.pyplot as plt
import dataGen4DietAct 
import dietActInfoRetrv
import utilise 
import pandas as pd 
import numpy as np

#matplotlib.style.use('presentation')
#plt.style.use('classic')
#print plt.style.available

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def visDailyPatternStack():
    
    for sub in available_list:
        d = dataGen4DietAct.genDailySingleActTypeTFArray(sub)
        
#        for i in range(d.shape[0]):
#            for j in range(d.shape[1]):
#                if d[i][j] > 1:
#                    d[i][j] = 1
        labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
        

#        x = np.arange(d.shape[0])
#        plt.figure()
#        plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7])
#        plt.title('DailyActivityPattern_'+sub)
#        plt.xlabel('days')
#        plt.savefig('visDailyActTypePattStack/DailyActivityPattern_'+sub)
        
#        plt.figure()
#        x = np.arange(d.shape[0])
#        data = np.array([d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7]])
#        bottom = np.cumsum(data, axis=0)
#        colors = ('#ff3333', '#33ff33', '#3333ff', '#33ffff','#ff3333', '#33ff33', '#3333ff', '#33ffff')
#        plt.bar(x, data[0], color=colors[0])
#        for j in xrange(1, data.shape[0]):
#            plt.bar(x, data[1], color=colors[j], bottom=bottom[j-1])
    

#        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        colors = plt.cm.Paired
        
        df = pd.DataFrame(d,columns=labels)
        ax = df.plot.bar(colormap=colors,stacked = True)
        plt.legend(bbox_to_anchor=(1.05,1), loc=2)
        plt.title('DailyActivityPattern_'+sub)
        plt.xlabel('days')
        plt.ylabel('frequency per day')
        data = dietActInfoRetrv.getDaysList(sub)
        ax.set_xticklabels(data)
        plt.savefig('visDailyActTypePattStack/DailyActivityPattern_'+sub,bbox_inches='tight')
        
    
    for sub in available_list:
        d = dataGen4DietAct.genDailySingleDietTypeTFArray(sub)
        
#        for i in range(d.shape[0]):
#            for j in range(d.shape[1]):
#                if d[i][j] > 1:
#                    d[i][j] = 1
        labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())

#        x = np.arange(d.shape[0])
#        plt.figure()
#        plt.stackplot(x,d[:,0],d[:,1],d[:,2],d[:,3],d[:,4],d[:,5],d[:,6],d[:,7],d[:,8],d[:,9],d[:,10],d[:,11])
#        plt.title('DailyDietPattern_'+sub)
#        plt.xlabel('days')
#        plt.savefig('visDailyDietTypePattStack/DailyDietPattern_'+sub)
        
        colors = plt.cm.Paired
        
        df = pd.DataFrame(d,columns=labels)
        ax = df.plot.bar(colormap=colors,stacked = True)
        plt.legend(bbox_to_anchor=(1.05,1), loc=2) 
#        df.plot.area()
        plt.title('DailyDietPattern_'+sub)
        plt.ylabel('frequency per day')
        plt.xlabel('days')
        data = dietActInfoRetrv.getDaysList(sub)
        ax.set_xticklabels(data)
        plt.savefig('visDailyDietTypePattStack/DailyDietPattern_'+sub,bbox_inches='tight')
    
visDailyPatternStack()
