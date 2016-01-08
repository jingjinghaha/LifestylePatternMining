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
	for line in open('dietOverallItemFreq/all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[1]
		n += 1
	# print item_dict
	return item_dict

def genDietTypeDict():
	item_dict = {}
	n = 0
	for line in open('dietOverallTypeFreq/all_dietType_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[0]
		n += 1
	# print item_dict
	return item_dict

def genActItemDict():
	item_dict = {}
	n = 0
	for line in open('activityOverallItemFreq/all_activity_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		item_dict[n] = words[1]
		n += 1
	# print item_dict
	return item_dict

def genActTypeDict():
	item_dict = {}
	n = 0
	for line in open('activityOverallTypeFreq/all_activityType_frequency.txt','r'):
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
	# distance = (np.sqrt(sum(np.power(vecA - vecB, 2)))+1)
	similarity = 1/(np.sqrt(sum(np.power(vecA - vecB, 2)))+1)
	return similarity #la.norm(vecA-vecB)
	
def distCosin(vecA,vecB): # -1 -> 1
	innerProduct = sum(vecA*vecB)
	# print "ineer product",innerProduct
	absA = np.sqrt(sum(np.power(vecA,2)))
	absB = np.sqrt(sum(np.power(vecB,2)))
	# print absA,absB
	# distance = 1.0-(innerProduct)/(absA*absB)
	similarity = (innerProduct)/(absA*absB)
	return similarity

# to calculate the similarity of two user 
def TFIDFCosin(domain):
	similarity_dict = {}
	similarity = 0
	if domain == 'ActItem':
		tfidf = ActItemTfidfArray()
	elif domain == 'DietItem':
		tfidf = DietItemTfidfArray()
	elif domain == 'DietType':
		tfidf = DietTypeTfidfArray()
	elif domain == 'ActType':
		tfidf = ActTypeTfidfArray()
	x = tfidf.shape[0]
	for i in range(x):
		similarity_dict[i] = {}
		for j in range(x):
			# print tfidf[i],tfidf[j]
			similarity = distCosin(tfidf[i],tfidf[j])
			# print similarity
			similarity_dict[i][j] = similarity
	# print similarity_dict
	return similarity_dict

def TFIDFEclud(domain):
	similarity_dict = {}
	similarity = 0
	if domain == 'ActItem':
		tfidf = ActItemTfidfArray()
	elif domain == 'DietItem':
		tfidf = DietItemTfidfArray()
	elif domain == 'DietType':
		tfidf = DietTypeTfidfArray()
	elif domain == 'ActType':
		tfidf = ActTypeTfidfArray()
	x = tfidf.shape[0]
	for i in range(x):
		similarity_dict[i] = {}
		for j in range(x):
			# print tfidf[i],tfidf[j]
			similarity = distEclud(tfidf[i],tfidf[j])
			# print similarity
			similarity_dict[i][j] = similarity
	# print similarity_dict
	return similarity_dict

def TFCosin(domain):
	similarity_dict = {}
	similarity = 0
	if domain == 'ActItem':
		tf = genActItemTFArray()
	elif domain == 'DietItem':
		tf = genDietItemTFArray()
	elif domain == 'DietType':
		tf = genDietTypeTFArray()
	elif domain == 'ActType':
		tf = genActTypeTFArray()
	x = tf.shape[0]
	for i in range(x):
		similarity_dict[i] = {}
		for j in range(x):
			# print tf[i],tf[j]
			similarity = distCosin(tf[i],tf[j])
			# print similarity
			similarity_dict[i][j] = similarity
	# print similarity_dict
	return similarity_dict

def TFEclud(domain):
	similarity_dict = {}
	similarity = 0
	if domain == 'ActItem':
		tf = genActItemTFArray()
	elif domain == 'DietItem':
		tf = genDietItemTFArray()
	elif domain == 'DietType':
		tf = genDietTypeTFArray()
	elif domain == 'ActType':
		tf = genActTypeTFArray()
	x = tf.shape[0]
	for i in range(x):
		similarity_dict[i] = {}
		for j in range(x):
			# print tf[i],tf[j]
			similarity = distEclud(tf[i],tf[j])
			# print similarity
			similarity_dict[i][j] = similarity
	# print similarity_dict
	return similarity_dict

def SimilarityDict(domain,dist = 'TFIDFCosin'):
	Similarity_dict = {} 
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	if dist == 'TFIDFCosin':
		Similarity_dict = TFIDFCosin(domain)
	elif dist == 'TFIDFEclud':
		Similarity_dict = TFIDFEclud(domain)
	elif dist == 'TFCosin':
		Similarity_dict = TFCosin(domain)
	elif dist == 'TFEclud':
		Similarity_dict = TFEclud(domain)
	else: 
		i = 0
		for subjectID in available_list:
			j = 0
			similarity = 0
			Similarity_dict[i] = {}
			if domain == 'ActItem':
				ItemIndex = buildItemIndex.build_single_activity_index(subjectID)
			elif domain == 'DietItem':
				ItemIndex = buildItemIndex.build_single_diet_index(subjectID)
			elif domain == 'DietType':
				ItemIndex = buildTypeIndex.build_single_diet_index(subjectID)
			elif domain == 'ActType':
				ItemIndex = buildTypeIndex.build_single_activity_index(subjectID)
			for subjectid in available_list:
				if domain == 'ActItem':
					temp_ItemIndex = buildItemIndex.build_single_activity_index(subjectid)
				elif domain == 'DietItem':
					temp_ItemIndex = buildItemIndex.build_single_diet_index(subjectid)
				elif domain == 'DietType':
					temp_ItemIndex = buildTypeIndex.build_single_diet_index(subjectid)
				elif domain == 'ActType':
					temp_ItemIndex = buildTypeIndex.build_single_activity_index(subjectid)
				if dist == 'numberOfSameWord':
					similarity = numberOfSameWord(ItemIndex,temp_ItemIndex)
				elif dist == 'jaccard':
					similarity = jaccard(ItemIndex,temp_ItemIndex)
				elif dist == 'novelJaccard':
					similarity = novelJaccard(ItemIndex,temp_ItemIndex)
				Similarity_dict[i][j] = similarity
				j += 1
			i += 1
	# print Similarity_dict
	return Similarity_dict
