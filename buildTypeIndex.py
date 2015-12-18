# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""
from nltk import wordpunct_tokenize
import dietType
import actType

#build the diet type index for single user
def build_single_diet_index(subjectID):
	singleDietType_dict = {}
	for line in open('diet_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: item
		#words[3]: item frequency
		diettype = dietType.dietType(words[1])
		# print diettype
		temp = int(words[3])
		if diettype in singleDietType_dict:
			singleDietType_dict[diettype] += temp
			# print singleDietType_dict[diettype]
			# print type(singleDietType_dict[diettype])
		else:
			singleDietType_dict[diettype] = temp
			# print singleDietType_dict[diettype]
	return singleDietType_dict

#build the activity type index for single user
def build_single_activity_index(subjectID):
	singleActType_dict = {}
	for line in open('activity_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: item
		#words[3]: item frequency
		acttype = actType.actType(words[1])
		temp = int(words[3])
		if acttype in singleActType_dict:
			singleActType_dict[acttype] += temp
			# print singleActType_dict[acttype]
			# print type(singleActType_dict[acttype])
		else:
			singleActType_dict[acttype] = temp
			# print singleActType_dict[acttype]
	return singleActType_dict

