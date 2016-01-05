# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:24:53 2015

@author: wu34
"""

import buildItemIndex

# create single and overall diet/activity Item frequency txt files for all users
def buildItemFreqTXTFile():
	print 'in buildItemFreqTXTFile()'
	singlerun = 0 
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	if singlerun: 
		subjectID = '039'
		print buildItemIndex.build_single_diet_index(subjectID)
		print buildItemIndex.build_single_activity_index(subjectID)
	else:
		f_diet = open('dietItemOverallFreq/all_diet_frequency.txt','w')
		f_act = open('activityItemOverallFreq/all_activity_frequency.txt','w')
		for subjectID in available_list:
			print subjectID
			f_diet_temp = open('dietItemFreq/diet_frequency_'+subjectID+'.txt','w')
			f_act_temp = open('activityItemFreq/activity_frequency_'+subjectID+'.txt','w')
			index_diet = buildItemIndex.build_single_diet_index(subjectID)
			index_act =  buildItemIndex.build_single_activity_index(subjectID)
			for key in index_diet:
				f_diet_temp.write("%-25s%-10s"%(key,index_diet[key]))
				f_diet_temp.write('\n')
			for key in index_act:
				f_act_temp.write("%-25s%-10s"%(key,index_act[key]))
				f_act_temp.write('\n')
			f_act_temp.close()
			f_diet_temp.close()
		index_diet = buildItemIndex.build_all_diet_index(available_list)
		#print index_diet
		index_act = buildItemIndex.build_all_activity_index(available_list)
		#print index_act
		for key in index_diet:
			if index_diet[key] >= 5:
				f_diet.write("%-25s%-10s"%(key,index_diet[key]))
				f_diet.write('\n')
		for key in index_act:
			if index_act[key] >=5 :
				f_act.write("%-25s%-10s"%(key,index_act[key]))
				f_act.write('\n')
		f_act.close()
		f_diet.close()

#buildItemFreqTXTFile()
