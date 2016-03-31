# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:26:06 2015

@author: wu34
"""

import buildItemIndex
import buildTypeIndex
import dietActInfoRetrv
from pymining import itemmining, assocrules 
available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
 
def genDietItemDataSet():
	dataset = []
	
	for subjectid in available_list:
		indexDict = buildItemIndex.build_single_diet_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)

	dataset = tuple(dataset)
	# print dataset
	return dataset

def genActItemDataSet():
	dataset = []

	for subjectid in available_list:
		indexDict = buildItemIndex.build_single_activity_index(subjectid)
		temp = tuple(indexDict)
		dataset.append(temp)

	dataset = tuple(dataset)
	# print dataset
	return dataset

def genDailyDietDataSet():
	dataset = [] 

	for subjectid in available_list:
		duration = dietActInfoRetrv.getDuration(subjectid)
		for i in range(duration):
			indexDict = buildItemIndex.build_daily_single_diet_index(subjectid,i+1)
			temp = tuple(indexDict)
			dataset.append(temp)

	dataset = tuple(dataset)
	print len(dataset)
	return dataset

def genDailyActDataSet():
	dataset = [] 

	for subjectid in available_list:
		duration = dietActInfoRetrv.getDuration(subjectid)
		for i in range(duration):
			indexDict = buildItemIndex.build_daily_single_activity_index(subjectid,i+1)
			temp = tuple(indexDict)
			dataset.append(temp)

	dataset = tuple(dataset)
	print len(dataset)
	return dataset

def genDailyDietTypeDataSet():
	dataset = [] 

	for subjectid in available_list:
		duration = dietActInfoRetrv.getDuration(subjectid)
		for i in range(duration):
			indexDict = buildTypeIndex.build_daily_single_diet_index(subjectid,i+1)
			temp = tuple(indexDict)
			dataset.append(temp)

	dataset = tuple(dataset)
	print len(dataset)
	return dataset

def genDailyActTypeDataSet():
	dataset = [] 

	for subjectid in available_list:
		duration = dietActInfoRetrv.getDuration(subjectid)
		for i in range(duration):
			indexDict = buildTypeIndex.build_daily_single_activity_index(subjectid,i+1)
			temp = tuple(indexDict)
			dataset.append(temp)

	dataset = tuple(dataset)
	print len(dataset)
	return dataset

def genDailyActDietTypeDataSet():
    dataset = [] 

    for subjectid in available_list:
        duration = dietActInfoRetrv.getDuration(subjectid)
        for i in range(duration):
            indexDict1 = buildTypeIndex.build_daily_single_activity_index(subjectid,i+1)
            temp1 = tuple(indexDict1)
            indexDict2 = buildTypeIndex.build_daily_single_diet_index(subjectid,i+1)
            temp2 = tuple(indexDict2)
            temp = temp1+temp2
            dataset.append(temp)

    dataset = tuple(dataset)
    print len(dataset)
    return dataset

# transactions = genDietItemDataSet()
# transactions = genActItemDataSet()
# transactions = genDailyDietDataSet()
# transactions = genDailyActDataSet()
#transactions = genDailyDietTypeDataSet()
#transactions = genDailyActTypeDataSet()
transactions = genDailyActDietTypeDataSet()

# print transactions

relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=100)
# print item_sets
rules = assocrules.mine_assoc_rules(item_sets, min_support=100, min_confidence=0.70)
print rules 


# transactions = perftesting.get_default_transactions()
# relim_input = itemmining.get_relim_input(transactions)
# item_sets = itemmining.relim(relim_input, min_support=5)
# print item_sets
# rules = assocrules.mine_assoc_rules(item_sets, min_support=3, min_confidence=0.5)
# print rules 
