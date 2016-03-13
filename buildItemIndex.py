# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""

def buildIndex(file):
	index = {}
	for line in open(file):
		line = line.split('[')[1].split(']')[0].split(',')
		for word in line: 
			word = word.strip(' ')
			word = word.split("'")[1]
			# print word
			if word in index:
				index[word] += 1
			else:
				index[word] = 1
	# print index
	return index 

def build_single_diet_index(subjectID):
	'''
	build the diet index for single user
	'''
	index = buildIndex('diet/dietProcessed/processed_diet_'+subjectID+'.txt')
	return index 

def build_daily_single_diet_index(subjectID,n):
	'''
	build the daily diet index for single user
	'''
	index = buildIndex('diet/dietProcessed/processed_diet_'+subjectID+'_'+str(n)+'.txt')
	return index 

def build_single_activity_index(subjectID):
	'''
	build the activity index for single user
	'''
	index = buildIndex('activity/activityProcessed/processed_activity_'+subjectID+'.txt')
	return index 

def build_daily_single_activity_index(subjectID,n):
	'''
	build the daily diet index for single user
	'''
	index = buildIndex('activity/activityProcessed/processed_activity_'+subjectID+'_'+str(n)+'.txt')
	return index 

def build_all_diet_index(available_list):
	'''
	build the diet index for all users
	'''
	index = {}
	for subjectID in available_list:
		small_index = build_single_diet_index(subjectID)
		for key in small_index:
			if key in index:
				index[key] += small_index[key]
			else:
				index[key] = small_index[key]
	return index

def build_all_activity_index(available_list):
	'''
	build the activity index for all users
	'''
	index = {}
	for subjectID in available_list:
		small_index = build_single_activity_index(subjectID)
		for key in small_index:
			if key in index:
				index[key] += small_index[key]
			else:
				index[key] = small_index[key]
	return index

# buildIndex('activity/activityProcessed/processed_activity_'+'039'+'_'+str(1)+'.txt')
