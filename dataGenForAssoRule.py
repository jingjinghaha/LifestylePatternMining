# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:26:06 2015

@author: wu34
"""

import buildItemIndex
import buildTypeIndex
from pymining import itemmining, assocrules, perftesting
	 
def genDietItemDataSet():
	dataset = []
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectid in available_list:
		indexDict = buildItemIndex.build_single_diet_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)
	dataset = tuple(dataset)
	# print dataset
	return dataset

def genActItemDataSet():
	dataset = []
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectid in available_list:
		indexDict = buildItemIndex.build_single_activity_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)
	dataset = tuple(dataset)
	# print dataset
	return dataset

def genDietTypeDataSet():
	dataset = []
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectid in available_list:
		indexDict = buildTypeIndex.build_single_diet_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)
	dataset = tuple(dataset)
	# print dataset
	return dataset

def genActTypeDataSet():
	dataset = []
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	for subjectid in available_list:
		indexDict = buildTypeIndex.build_single_activity_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)
	dataset = tuple(dataset)
	# print dataset
	return dataset


transactions = genDietItemDataSet()
# transactions = genActItemDataSet()
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=25)
# print item_sets
rules = assocrules.mine_assoc_rules(item_sets, min_support=23, min_confidence=0.95)
print rules 


# transactions = perftesting.get_default_transactions()
# relim_input = itemmining.get_relim_input(transactions)
# item_sets = itemmining.relim(relim_input, min_support=5)
# print item_sets
# rules = assocrules.mine_assoc_rules(item_sets, min_support=3, min_confidence=0.5)
# print rules 
