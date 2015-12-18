# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:01:17 2015

@author: wu34
"""
import numpy as np
from nltk import wordpunct_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
import buildItemIndex
import buildTypeIndex
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

def genDietItemDict():
	item_dict = {}
	n = 0
	for line in open('all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[1]
		n += 1
	# print item_dict
	return item_dict

def genDietTypeDict():
	item_dict = {}
	n = 0
	for line in open('all_dietType_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[0]
		n += 1
	# print item_dict
	return item_dict

def genActItemDict():
	item_dict = {}
	n = 0
	for line in open('all_activity_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[1]
		n += 1
	# print item_dict
	return item_dict

def genActTypeDict():
	item_dict = {}
	n = 0
	for line in open('all_activityType_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[0]
		n += 1
	# print item_dict
	return item_dict

def genDietItemTFArray():
	item_dict = genDietItemDict()
	x = len(available_list)
	n = len(item_dict)
	dims = (x,n)
	array = np.zeros(dims)
	i = 0 
	for subjectID in available_list:
		ItemIndex = buildItemIndex.build_single_diet_index(subjectID)
		for key in item_dict:
			if "'"+item_dict[key]+"'" in ItemIndex: 
				# print item_dict[key]
				array[i,key] = ItemIndex["'"+item_dict[key]+"'"]
		i += 1
	return array

def genDietTypeTFArray():
	item_dict = genDietTypeDict()
	x = len(available_list)
	n = len(item_dict)
	dims = (x,n)
	array = np.zeros(dims)
	i = 0 
	for subjectID in available_list:
		ItemIndex = buildTypeIndex.build_single_diet_index(subjectID)
		for key in item_dict:
			if item_dict[key] in ItemIndex: 
				# print item_dict[key]
				array[i,key] = ItemIndex[item_dict[key]]
		i += 1
	return array

def genActItemTFArray():
	item_dict = genActItemDict()
	# print item_dict
	x = len(available_list)
	n = len(item_dict)
	dims = (x,n)
	array = np.zeros(dims)
	i = 0 
	for subjectID in available_list:
		ItemIndex = buildItemIndex.build_single_activity_index(subjectID)
		# print ItemIndex
		for key in item_dict:
			if "'"+item_dict[key]+"'" in ItemIndex: 
				# print item_dict[key]
				array[i,key] = ItemIndex["'"+item_dict[key]+"'"]
		i += 1
	# print array
	return array

def genActTypeTFArray():
	item_dict = genActTypeDict()
	# print item_dict
	x = len(available_list)
	n = len(item_dict)
	dims = (x,n)
	array = np.zeros(dims)
	i = 0 
	for subjectID in available_list:
		ItemIndex = buildTypeIndex.build_single_activity_index(subjectID)
		for key in item_dict:
			if item_dict[key] in ItemIndex: 
				# print item_dict[key]
				array[i,key] = ItemIndex[item_dict[key]]
		i += 1
	return array

def DietItemTfidfArray():
	counts = genDietItemTFArray()
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(counts)
	aa = tfidf.toarray()
	return aa

def DietTypeTfidfArray():
	counts = genDietTypeTFArray()
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(counts)
	aa = tfidf.toarray()
	return aa

def ActItemTfidfArray():
	counts = genActItemTFArray()
	# print counts
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(counts)
	aa = tfidf.toarray()
	return aa

def ActTypeTfidfArray():
	counts = genActTypeTFArray()
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(counts)
	aa = tfidf.toarray()
	return aa

# to calculate the similarity of two user 
def numberOfSameWord(dict1,dict2):
	similarity = 0
	for key in dict1:
		if key in dict2:
			similarity += 1
	return similarity

# to calculate the similarity of two user 
def jaccard(dict1,dict2):
	similarity = 0
	listA = []
	listB = []
	for key in dict1:
		listA.append(key)
	for key in dict2:
		listB.append(key)
	setA = set(listA)
	setB = set(listB)
	similarity = float(len(setA.intersection(setB)))/len(setA.union(setB))
	return similarity

# this dict2list is to modify the diet/activity dict of each user for novel Jaccard computation 
def dict2list(dict):
	list = []
	for key in dict:
		for i in range(dict[key]):
			temp_string = key + str(i)
			list.append(temp_string)
	# print list
	return list

# to calculate the similarity of two user 
def novelJaccard(dict1,dict2):
	similarity = 0
	listA = dict2list(dict1)
	listB = dict2list(dict2)
	setA = set(listA)
	setB = set(listB)
	# distance = 1.0 - float(len(setA.intersection(setB)))/len(setA.union(setB))
	similarity = float(len(setA.intersection(setB)))/len(setA.union(setB))
	# print similarity
	return similarity

def distEclud(vecA, vecB): # real 0 -> 1
	return 1/(sqrt(sum(power(vecA - vecB, 2)))+1) #la.norm(vecA-vecB)
	
def distCosin(vecA,vecB): # -1 -> 1
	innerProduct = sum(vecA*vecB)
	# print "ineer product",innerProduct
	absA = np.sqrt(sum(np.power(vecA,2)))
	absB = np.sqrt(sum(np.power(vecB,2)))
	# print absA,absB
	return (innerProduct)/(absA*absB)

# to calculate the similarity of two user 
def TFIDF(domain):
	similarity_dict = {}
	similarity = 0
	if domain == 'actItem':
		tfidf = ActItemTfidfArray()
	elif domain == 'dietItem':
		tfidf = DietItemTfidfArray()
	elif domain == 'dietType':
		tfidf = DietTypeTfidfArray()
	elif domain == 'actType':
		tfidf = ActTypeTfidfArray()
	x = tfidf.shape[0]
	for i in range(x):
		similarity_dict[i] = {}
		for j in range(x):
			# print tfidf[i],tfidf[j]
			similarity = distCosin(tfidf[i],tfidf[j])
			# print similarity
			similarity_dict[i][j] = similarity
	# similarity = distCosin(tfidf[i],tfidf[j])
	# print similarity_dict
	return similarity_dict


	