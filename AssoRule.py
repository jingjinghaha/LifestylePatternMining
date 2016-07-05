# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:26:06 2015

@author: wu34
"""

import buildItemIndex
import buildTypeIndex
import dietActInfoRetrv
import artificialDataGenerator
import newDataProcess
from pymining import itemmining, assocrules 
#from pymining import seqmining
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
			if 'compositeP' in indexDict: del indexDict['compositeP']
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
            if 'others' in indexDict1: del indexDict1['others']
            temp1 = tuple(indexDict1)
            indexDict2 = buildTypeIndex.build_daily_single_diet_index(subjectid,i+1)
            if 'compositeP' in indexDict2: del indexDict2['compositeP']
            temp2 = tuple(indexDict2)
            temp = temp1+temp2
            dataset.append(temp)

    dataset = tuple(dataset)
    print len(dataset)
    return dataset
#genDailyActDietTypeDataSet()

def genOriginalActDietTypeDataSet():
    dataset = []     
    
    df = artificialDataGenerator.originalData()
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'compositeP' and j != 'label' and j!='sleepTime' and j!='gender' and j!='ID' and j!='others':
                if df[j][i] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)        
        
    dataset = tuple(dataset)
    print len(dataset)
    return dataset

def genOriginalActDietTypeDataSetForLessSleep():
    dataset = []     
    
    df = artificialDataGenerator.originalData()
    df = df[df['label']==0]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'compositeP' and j != 'label' and j!='sleepTime' and j!='gender' and j!='ID' and j!='others':
                if df[j][i] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)        
        
    dataset = tuple(dataset)
    print len(dataset)
    return dataset 
 
def genOriginalActDietTypeDataSetForMoreSleep():
    dataset = []     
    
    df = artificialDataGenerator.originalData()
    df = df[df['label']==1]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'compositeP' and j != 'label' and j!='sleepTime' and j!='gender' and j!='ID' and j!='others':
                if df[j][i] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)        
        
    dataset = tuple(dataset)
    print len(dataset)
    return dataset
    
def genArtificialActDietTypeDataSet():
    dataset = []

    newDF = artificialDataGenerator.artificialData()
    for i in range(newDF.shape[0]):
        temp = []
        for j in newDF.columns:
            if j != 'compositeP' and j != 'sleepTime' and j != 'label' and j!='gender' and j!='others': 
                if newDF.ix[i,j] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)
    
    dataset = tuple(dataset)
    print len(dataset)
    return dataset

def genArtificialActDietTypeDataSetForLessSleep():
    dataset = []

    df = artificialDataGenerator.artificialData()
    df = df[df['label']==0]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'compositeP' and j != 'sleepTime' and j != 'label' and j!='gender' and j!='others': 
                if df.ix[i,j] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)
    
    dataset = tuple(dataset)
    print len(dataset)
    return dataset

def genArtificialActDietTypeDataSetForMoreSleep():
    dataset = []

    df = artificialDataGenerator.artificialData()
    df = df[df['label']==1]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'compositeP' and j != 'sleepTime' and j != 'label' and j!='gender' and j!='others': 
                if df.ix[i,j] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)
    
    dataset = tuple(dataset)
    print len(dataset)
    return dataset

def genNewActDietTypeDataSet():
    dataset = []

    newDF = newDataProcess.newFeatureFrame() 
    for i in range(newDF.shape[0]):
        temp = []
        for j in newDF.columns:
            if j != 'grainP' and j!='ID' and j!='gender' and j!='age' and j != 'label' and j != 'vegetables' and j != 'meatP' and j != 'dairyP' and j!='caffeineD' and j!='snack': 
                if newDF.ix[i,j] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)
    
    dataset = tuple(dataset)
    print len(dataset)
    return dataset
    
def genNewActDietTypeDataSetForLessSleep():
    dataset = []     
    
    df = newDataProcess.newFeatureFrame()
    df = df[df['label']==0]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'grainP' and j!='ID' and j!='gender' and j!='age' and j != 'label' and j != 'vegetables' and j != 'meatP' and j != 'dairyP' and j!='caffeineD' and j!='snack':
                if df[j][i] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)        
        
    dataset = tuple(dataset)
    print len(dataset)
    return dataset 
 
def genNewActDietTypeDataSetForMoreSleep():
    dataset = []     
    
    df = newDataProcess.newFeatureFrame()
    df = df[df['label']==1]
    df.index = range(df.shape[0])
    
    for i in range(df.shape[0]):
        temp = []
        for j in df.columns:
            if j != 'grainP' and j!='ID' and j!='gender' and j!='age' and j != 'label' and j != 'vegetables' and j != 'meatP' and j != 'dairyP' and j!='caffeineD' and j!='snack':
                if df[j][i] > 0:
                    temp.append(j)
        temp = tuple(temp)
        dataset.append(temp)        
        
    dataset = tuple(dataset)
    print len(dataset)
    return dataset

#for i in range(1,10):
#    # transactions = genDietItemDataSet()
#    # transactions = genActItemDataSet()
#    # transactions = genDailyDietDataSet()
#    # transactions = genDailyActDataSet()
#    #transactions = genDailyDietTypeDataSet()
#    #transactions = genDailyActTypeDataSet()
#    #transactions = genDailyActDietTypeDataSet()
#    #transactions = genOriginalActDietTypeDataSet()
##    transactions = genOriginalActDietTypeDataSetForLessSleep()
##    transactions = genOriginalActDietTypeDataSetForMoreSleep()
#    #transactions = genArtificialActDietTypeDataSet()
#    transactions = genArtificialActDietTypeDataSetForLessSleep()
#    #transactions = genArtificialActDietTypeDataSetForMoreSleep()
#    #transactions = genNewActDietTypeDataSet()
#    #transactions = genNewActDietTypeDataSetForLessSleep()
#    #transactions = genNewActDietTypeDataSetForMoreSleep()
#    
#    # print transactions
#    
#    relim_input = itemmining.get_relim_input(transactions)
#
#    print 0.1*i
#    item_sets = itemmining.relim(relim_input, min_support=int(len(transactions)*0.1*3))
##    print len(item_sets)
#    rules = assocrules.mine_assoc_rules(item_sets, min_support=int(len(transactions)*0.1*3), min_confidence=0.1*i)
#    print len(rules)

transactions = genOriginalActDietTypeDataSetForMoreSleep()
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=int(len(transactions)*0.1*3))
#print item_sets  
rules = assocrules.mine_assoc_rules(item_sets, min_support=len(transactions)*0.3, min_confidence=0.70)
print rules 


#df = newDataProcess.newFeatureFrame()
#df = df[df['label']==1]
#print df.shape[0]
#for factor in ['bike','leisure','starchyP','fruitP']:
#    df_temp1 = df[df[factor]>0]
#    #print df_temp1.shape[0]
#    df_temp2 = df[df['workStudy']>0]
#    #print df_temp2.shape[0]
#    df_temp3 = df_temp1[df_temp1['workStudy']>0]
#    #print df_temp3.shape[0]
#    print (float(df_temp3.shape[0])/(df_temp1.shape[0]*df_temp2.shape[0]))*df.shape[0]

df = artificialDataGenerator.originalData()
df = df[df['label']==1]
print df.shape[0]
df_temp1 = df[df['transportation1']>0]
#print df_temp1.shape[0]
df_temp2 = df[df['transportation2']>0]
#print df_temp2.shape[0]
df_temp3 = df_temp1[df_temp1['transportation2']>0]
#print df_temp3.shape[0]
print (float(df_temp3.shape[0])/(df_temp1.shape[0]*df_temp2.shape[0]))*df.shape[0]

#df = newDataProcess.newFeatureFrame()
#for factor in df.columns:
#    print factor
#    df_temp1 = df[df[factor]>0]
##    print df_temp1.shape[0]
#    df_temp2 = df[df['label']==1]
##    print df_temp2.shape[0]
#    df_temp3 = df_temp1[df_temp1['label']==1]
##    print df_temp3.shape[0]
#    print (float(df_temp3.shape[0])/(df_temp1.shape[0]*df_temp2.shape[0]))*df.shape[0]

#freq_seqs = seqmining.freq_seq_enum(transactions, 100)
#print sorted(freq_seqs)

# transactions = perftesting.get_default_transactions()
# relim_input = itemmining.get_relim_input(transactions)
# item_sets = itemmining.relim(relim_input, min_support=5)
# print item_sets
# rules = assocrules.mine_assoc_rules(item_sets, min_support=3, min_confidence=0.5)
# print rules 
