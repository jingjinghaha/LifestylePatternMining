# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:24:53 2015

@author: wu34
"""

import buildItemIndex
import infoRetrival
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']


def buildItemFreqTXTFile():
	'''
	create single and overall diet/activity Item frequency txt files for all users
	'''
	print 'in buildItemFreqTXTFile()'
	singlerun = 0 
	if singlerun: 
		subjectID = '039'
		print buildItemIndex.build_single_diet_index(subjectID)
		print buildItemIndex.build_single_activity_index(subjectID)
	else:
		f_diet = open('diet/dietOverallItemFreq/all_diet_frequency.txt','w')
		f_act = open('activity/activityOverallItemFreq/all_activity_frequency.txt','w')
		for subjectID in available_list:
			print subjectID
			'''
			wirte diet and activity index for each subject into txt files 
			'''
			f_diet_temp = open('diet/dietItemFreq/diet_frequency_'+subjectID+'.txt','w')
			f_act_temp = open('activity/activityItemFreq/activity_frequency_'+subjectID+'.txt','w')
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
		'''
		write overall diet and activity index into txt files 
		'''
		index_diet = buildItemIndex.build_all_diet_index(available_list)
		#print index_diet
		index_act = buildItemIndex.build_all_activity_index(available_list)
		#print index_act
		for key in index_diet:
			if index_diet[key] >= 5:
			# if index_diet[key]:
				f_diet.write("%-25s%-10s"%(key,index_diet[key]))
				f_diet.write('\n')
		for key in index_act:
			if index_act[key] >=5 :
			# if index_act[key]:
				f_act.write("%-25s%-10s"%(key,index_act[key]))
				f_act.write('\n')
		f_act.close()
		f_diet.close()

def buildDailyItemFreqTXTFile():
	'''
	write daily diet and activity index of each subject into txt files 
	'''
	for subjectID in available_list:
		duration = infoRetrival.getDuration(subjectID)
		for n in range(1,duration+1):
			print subjectID, n 
			f_act = open('activity/activityItemFreq/activity_frequency_'+subjectID+'_'+str(n)+'.txt','w')
			f_diet = open('diet/dietItemFreq/diet_frequency_'+subjectID+'_'+str(n)+'.txt','w')
			index_act = buildItemIndex.build_daily_single_activity_index(subjectID,n)
			index_diet = buildItemIndex.build_daily_single_diet_index(subjectID,n)
			print index_act
			print index_diet
			for key in index_act:
				f_act.write("%-25s%-10s"%(key,index_act[key]))
				f_act.write('\n')
			for key in index_diet:
				f_diet.write("%-25s%-10s"%(key,index_diet[key]))
				f_diet.write('\n')
			f_act.close()
			f_diet.close()

#buildItemFreqTXTFile()
#buildDailyItemFreqTXTFile() 