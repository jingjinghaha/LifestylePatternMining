# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:43:57 2016

@author: wu34
"""
import pandas as pd 
from pandas import DataFrame
import buildTypeIndex 
import dietActInfoRetrv
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

for subjectID in available_list:
	duration = dietActInfoRetrv.getDuration(subjectID)
	
	DF = DataFrame([0,0,0],columns=['P1','P2','P3'],index=['others'])
	for n in range(1,duration+1):
		d = buildTypeIndex.build_daily_single_activity_index_with_time(subjectID,n)
		df = DataFrame(d)
		DF = pd.merge(DF,df,left_index=True, right_index=True, how='outer')
		

print df['P1']