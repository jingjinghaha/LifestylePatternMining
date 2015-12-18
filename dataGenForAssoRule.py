# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:26:06 2015

@author: wu34
"""
from collections import defaultdict
from nltk import wordpunct_tokenize

import buildItemIndex

def genDietItemList():
	item_list = {}
	n = 0
	for line in open('all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_list[n] = words[1]
		n += 1
	# print item_list
	return item_list
	 
def genDietDataSet():
	dataset = defaultdict(list)
	n = 1
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectid in available_list:
		temp_index = buildItemIndex.build_single_diet_index(subjectid)
		item_list = genItemList()
		# print temp_index
		for key in item_list:
			# print key 
			# print "'"+item_list[key]+"'"
			if "'"+item_list[key]+"'" in temp_index.keys(): 
				# print item_list[key]
				dataset[n].append(key)
		n += 1
		# print n 
	# print dataset
	return dataset


