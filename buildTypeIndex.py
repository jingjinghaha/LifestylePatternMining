# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""
from nltk import wordpunct_tokenize
import dietType
import actType
'''
build the diet type index for single user
'''
def build_single_diet_index(subjectID):
	singleDietType_dict = {}
	for line in open('diet/dietItemFreq/diet_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		# print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		diettype = dietType.dietType(words[0])
		# print diettype
		temp = int(words[1])
		if diettype != 'others':
			if diettype in singleDietType_dict:
				singleDietType_dict[diettype] += temp
				# print singleDietType_dict[diettype]
				# print type(singleDietType_dict[diettype])
			else:
				singleDietType_dict[diettype] = temp
				# print singleDietType_dict[diettype]
	return singleDietType_dict
'''
build the activity type index for single user
'''
def build_single_activity_index(subjectID):
	singleActType_dict = {}
	for line in open('activity/activityItemFreq/activity_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		acttype = actType.actType(words[0])
		temp = int(words[1])
		if acttype != 'none':
			if acttype in singleActType_dict:
				singleActType_dict[acttype] += temp
				# print singleActType_dict[acttype]
				# print type(singleActType_dict[acttype])
			else:
				singleActType_dict[acttype] = temp
				# print singleActType_dict[acttype]
	return singleActType_dict

'''
build the daily diet type index for single user
'''
def build_daily_single_diet_index(subjectID,n):
	singleDietType_dict = {}
	for line in open('diet/dietItemFreq/diet_frequency_'+subjectID+'_'+str(n)+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		diettype = dietType.dietType(words[0])
		# print diettype
		temp = int(words[1])
		if diettype != 'others':
			if diettype in singleDietType_dict:
				singleDietType_dict[diettype] += temp
				# print singleDietType_dict[diettype]
				# print type(singleDietType_dict[diettype])
			else:
				singleDietType_dict[diettype] = temp
				# print singleDietType_dict[diettype]
	return singleDietType_dict
'''
build the daily activity type index for single user
'''
def build_daily_single_activity_index(subjectID,n):
	singleActType_dict = {}
	for line in open('activity/activityItemFreq/activity_frequency_'+subjectID+'_'+str(n)+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		acttype = actType.actType(words[0])
		temp = int(words[1])
		if acttype != 'none':
			if acttype in singleActType_dict:
				singleActType_dict[acttype] += temp
				# print singleActType_dict[acttype]
				# print type(singleActType_dict[acttype])
			else:
				singleActType_dict[acttype] = temp
				# print singleActType_dict[acttype]
	return singleActType_dict
