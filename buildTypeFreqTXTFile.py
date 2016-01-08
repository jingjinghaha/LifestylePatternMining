# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:15:33 2015

@author: wu34
"""
from nltk import wordpunct_tokenize
import dietType
import actType
import buildTypeIndex

#create diet type frequency txt file for every user 
def buildSingleDietTypeFreqFile():
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectID in available_list:
		f_diet = open('dietTypeFreq/dietType_frequency_'+subjectID+'.txt','w')
		singleDietType_dict = buildTypeIndex.build_single_diet_index(subjectID)
		for key in singleDietType_dict:
			# if key != 'others':
			if key:
				f_diet.write("%-25s%-10s"%(key,singleDietType_dict[key]))
				f_diet.write('\n')
		f_diet.close()

#create activity type frequency txt file for every user 
def buildSingleActTypeFreqFile():
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectID in available_list:
		f_act = open('activityTypeFreq/activityType_frequency_'+subjectID+'.txt','w')
		singleActType_dict = buildTypeIndex.build_single_activity_index(subjectID)
		for key in singleActType_dict:
			if key != 'none':
				f_act.write("%-25s%-10s"%(key,singleActType_dict[key]))
				f_act.write('\n')
		f_act.close()

# create overall diet type frequency txt file
def buildDietTypeFreqTXTFile():
	dietType_dict = {}
	f_diet = open('dietOverallTypeFreq/all_dietType_frequency.txt','w')
	for line in open('dietOverallItemFreq/all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: item
		#words[3]: item frequency
		diettype = dietType.dietType(words[1])
		# print diettype
		temp = int(words[3])
		if diettype in dietType_dict:
			dietType_dict[diettype] += temp
			# print dietType_dict[diettype]
			# print type(dietType_dict[diettype])
		else:
			dietType_dict[diettype] = temp
			# print dietType_dict[diettype]
	# print dietType_dict
	for key in dietType_dict:
		# if key != 'others':
		if key:
			f_diet.write("%-25s%-10s"%(key,dietType_dict[key]))
			f_diet.write('\n')
	f_diet.close()

# create overall diet type frequency txt file
def buildActTypeFreqTXTFile():
	actType_dict = {}
	f_act = open('activityOverallTypeFreq/all_activityType_frequency.txt','w')
	for line in open('activityOverallItemFreq/all_activity_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: item
		#words[3]: item frequency
		acttype = actType.actType(words[1]) 
		temp = int(words[3])
		if acttype in actType_dict:
			actType_dict[acttype] += temp
		else:
			actType_dict[acttype] = temp
	# print actType_dict
	for key in actType_dict:
		if key != 'none':
			f_act.write("%-25s%-10s"%(key,actType_dict[key]))
			f_act.write('\n')
	f_act.close()

def buildTypeFreqTXTFile():
	print 'in buildTypeFreqTXTFile()'
	buildSingleDietTypeFreqFile()
	buildSingleActTypeFreqFile()
	buildDietTypeFreqTXTFile()
	buildActTypeFreqTXTFile()

# buildTypeFreqTXTFile()