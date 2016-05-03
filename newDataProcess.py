# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:51:17 2016

@author: jingjing
"""
import numpy as np 
import pandas as pd
import artificialDataGenerator
import matplotlib.pyplot as plt

#df = pd.read_csv('newData.csv')
#
##tempDF = df[df['Duration']>10]
#
#print df.shape
#print df.columns
#print type(df['Duration'][1]) 
#print type(df['Breakfast'][1])
#print int(df['Duration'][1].split(':')[0])
#
#for i in range(df.shape[0]):
#    df.set_value(i,'Duration',int(df['Duration'][i].split(':')[0]))
#    if df['Duration'][i] > 15:
#        print i 
#    
#temp_df = df[df['Duration']>=9]
#print temp_df.shape
#temp_df = df[df['Duration']>=8]
#print temp_df.shape
#temp_df = df[df['Duration']<8]
#print temp_df.shape
#
#print df['Breakfast'][1]
#if 'Grain' in df['Breakfast'][1]:
#    print 'haha'
#
#if type(df['Breakfast'][0]) is str:
#    print 'haha'

def newFeatureFrame():
    df = pd.read_csv('newData.csv')
    
    columns = ['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables','leisure','social','sport','walk','car','bike','workStudy','label']
    x = df.shape[0]
    n = len(columns)
    array = np.zeros((x,n))
    feature_df = pd.DataFrame(array,columns = columns) 
    
    for i in range(df.shape[0]):
        
        df.set_value(i,'Duration',int(df['Duration'][i].split(':')[0]))
        
        if df['Duration'][i] >= 9:
            feature_df['label'][i] = 2
        elif df['Duration'][i] >= 8:
            feature_df['label'][i] = 1
        else:
            feature_df['label'][i] = 0            
            
        if type(df['Breakfast'][i]) is str:
            if 'Alcohol' in df['Breakfast'][i]:
                feature_df['alcoholD'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Alcohol' in df['MorningSnack'][i]:
                feature_df['alcoholD'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Alcohol' in df['Lunch'][i]:
                feature_df['alcoholD'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Alcohol' in df['AfternoonSnack'][i]:
                feature_df['alcoholD'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Alcohol' in df['Dinner'][i]:
                feature_df['alcoholD'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Alcohol' in df['EveningSnack'][i]:
                feature_df['alcoholD'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Caffeine' in df['Breakfast'][i]:
                feature_df['caffeineD'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Caffeine' in df['MorningSnack'][i]:
                feature_df['caffeineD'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Caffeine' in df['Lunch'][i]:
                feature_df['caffeineD'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Caffeine' in df['AfternoonSnack'][i]:
                feature_df['caffeineD'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Caffeine' in df['Dinner'][i]:
                feature_df['caffeineD'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Caffeine' in df['EveningSnack'][i]:
                feature_df['caffeineD'][i] += 1
            
        if type(df['Breakfast'][i]) is str:
            if 'Dairy' in df['Breakfast'][i]:
                feature_df['dairyP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Dairy' in df['MorningSnack'][i]:
                feature_df['dairyP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Dairy' in df['Lunch'][i]:
                feature_df['dairyP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Dairy' in df['AfternoonSnack'][i]:
                feature_df['dairyP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Dairy' in df['Dinner'][i]:
                feature_df['dairyP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Dairy' in df['EveningSnack'][i]:
                feature_df['dairyP'][i] += 1
    
        if type(df['Breakfast'][i]) is str:
            if 'Egg' in df['Breakfast'][i]:
                feature_df['eggP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Egg' in df['MorningSnack'][i]:
                feature_df['eggP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Egg' in df['Lunch'][i]:
                feature_df['eggP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Egg' in df['AfternoonSnack'][i]:
                feature_df['eggP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Egg' in df['Dinner'][i]:
                feature_df['eggP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Egg' in df['EveningSnack'][i]:
                feature_df['eggP'][i] += 1
            
        if type(df['Breakfast'][i]) is str:
            if 'Fruit' in df['Breakfast'][i]:
                feature_df['fruitP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Fruit' in df['MorningSnack'][i]:
                feature_df['fruitP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Fruit' in df['Lunch'][i]:
                feature_df['fruitP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Fruit' in df['AfternoonSnack'][i]:
                feature_df['fruitP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Fruit' in df['Dinner'][i]:
                feature_df['fruitP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Fruit' in df['EveningSnack'][i]:
                feature_df['fruitP'][i] += 1
            
        if type(df['Breakfast'][i]) is str:
            if 'Grain' in df['Breakfast'][i]:
                feature_df['grainP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Grain' in df['MorningSnack'][i]:
                feature_df['grainP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Grain' in df['Lunch'][i]:
                feature_df['grainP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Grain' in df['AfternoonSnack'][i]:
                feature_df['grainP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Grain' in df['Dinner'][i]:
                feature_df['grainP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Grain' in df['EveningSnack'][i]:
                feature_df['grainP'][i] += 1
            
        if type(df['Breakfast'][i]) is str:
            if 'Meat' in df['Breakfast'][i]:
                feature_df['meatP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Meat' in df['MorningSnack'][i]:
                feature_df['meatP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Meat' in df['Lunch'][i]:
                feature_df['meatP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Meat' in df['AfternoonSnack'][i]:
                feature_df['meatP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Meat' in df['Dinner'][i]:
                feature_df['meatP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Meat' in df['EveningSnack'][i]:
                feature_df['meatP'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Seafood' in df['Breakfast'][i]:
                feature_df['seafood'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Seafood' in df['MorningSnack'][i]:
                feature_df['seafood'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Seafood' in df['Lunch'][i]:
                feature_df['seafood'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Seafood' in df['AfternoonSnack'][i]:
                feature_df['seafood'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Seafood' in df['Dinner'][i]:
                feature_df['seafood'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Seafood' in df['EveningSnack'][i]:
                feature_df['seafood'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Sweet' in df['Breakfast'][i]:
                feature_df['snack'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Sweet' in df['MorningSnack'][i]:
                feature_df['snack'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Sweet' in df['Lunch'][i]:
                feature_df['snack'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Sweet' in df['AfternoonSnack'][i]:
                feature_df['snack'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Sweet' in df['Dinner'][i]:
                feature_df['snack'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Sweet' in df['EveningSnack'][i]:
                feature_df['snack'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Nuts' in df['Breakfast'][i]:
                feature_df['snack'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Nuts' in df['MorningSnack'][i]:
                feature_df['snack'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Nuts' in df['Lunch'][i]:
                feature_df['snack'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Nuts' in df['AfternoonSnack'][i]:
                feature_df['snack'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Nuts' in df['Dinner'][i]:
                feature_df['snack'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Nuts' in df['EveningSnack'][i]:
                feature_df['snack'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Potato' in df['Breakfast'][i]:
                feature_df['starchyP'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Potato' in df['MorningSnack'][i]:
                feature_df['starchyP'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Potato' in df['Lunch'][i]:
                feature_df['starchyP'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Potato' in df['AfternoonSnack'][i]:
                feature_df['starchyP'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Potato' in df['Dinner'][i]:
                feature_df['starchyP'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Potato' in df['EveningSnack'][i]:
                feature_df['starchyP'][i] += 1
        
        if type(df['Breakfast'][i]) is str:
            if 'Vegetables' in df['Breakfast'][i]:
                feature_df['vegetables'][i] += 1 
        if type(df['MorningSnack'][i]) is str:
            if 'Vegetables' in df['MorningSnack'][i]:
                feature_df['vegetables'][i] += 1
        if type(df['Lunch'][i]) is str:
            if 'Vegetables' in df['Lunch'][i]:
                feature_df['vegetables'][i] += 1
        if type(df['AfternoonSnack'][i]) is str:
            if 'Vegetables' in df['AfternoonSnack'][i]:
                feature_df['vegetables'][i] += 1
        if type(df['Dinner'][i]) is str:
            if 'Vegetables' in df['Dinner'][i]:
                feature_df['vegetables'][i] += 1
        if type(df['EveningSnack'][i]) is str:
            if 'Vegetables' in df['EveningSnack'][i]:
                feature_df['vegetables'][i] += 1
        
        if type(df['MorningAct'][i]) is str:
            if 'Entertainment' in df['MorningAct'][i]:
                feature_df['leisure'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Entertainment' in df['AfternoonAct'][i]:
                feature_df['leisure'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Entertainment' in df['EveningAct'][i]:
                feature_df['leisure'][i] += 1
        
        if type(df['MorningAct'][i]) is str:
            if 'Social' in df['MorningAct'][i]:
                feature_df['social'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Social' in df['AfternoonAct'][i]:
                feature_df['social'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Social' in df['EveningAct'][i]:
                feature_df['social'][i] += 1
        
        if type(df['MorningAct'][i]) is str:
            if 'Sport' in df['MorningAct'][i]:
                feature_df['sport'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Sport' in df['AfternoonAct'][i]:
                feature_df['sport'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Sport' in df['EveningAct'][i]:
                feature_df['sport'][i] += 1
            
        if type(df['MorningAct'][i]) is str:
            if 'Walk' in df['MorningAct'][i]:
                feature_df['walk'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Walk' in df['AfternoonAct'][i]:
                feature_df['walk'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Walk' in df['EveningAct'][i]:
                feature_df['walk'][i] += 1     
        
        if type(df['MorningAct'][i]) is str:
            if 'Drive' in df['MorningAct'][i]:
                feature_df['car'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Drive' in df['AfternoonAct'][i]:
                feature_df['car'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Drive' in df['EveningAct'][i]:
                feature_df['car'][i] += 1
        
        if type(df['MorningAct'][i]) is str:
            if 'Bike' in df['MorningAct'][i]:
                feature_df['bike'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Bike' in df['AfternoonAct'][i]:
                feature_df['bike'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Bike' in df['EveningAct'][i]:
                feature_df['bike'][i] += 1
        
        if type(df['MorningAct'][i]) is str:
            if 'Work' in df['MorningAct'][i]:
                feature_df['workStudy'][i] += 1
        if type(df['AfternoonAct'][i]) is str:
            if 'Work' in df['AfternoonAct'][i]:
                feature_df['workStudy'][i] += 1
        if type(df['EveningAct'][i]) is str:
            if 'Work' in df['EveningAct'][i]:
                feature_df['workStudy'][i] += 1
    
    return feature_df
    
#feature = newFeatureFrame(df)

def visdiff():
    surrogateDF,labels = artificialDataGenerator.artificialData()
    df,cols = artificialDataGenerator.originalData() 
    newDF = newFeatureFrame()
    for i in newDF.columns:
        plt.figure()
        newDF[i].plot.kde(label='new')
        
        if i == 'walk':
            i = 'transportation1'
        if i == 'car':
            i = 'transportation2'
        if i == 'bike':
            i = 'transportation3'
        if i == 'leisure':
            i = 'entertainmentRelax'
        
        df[i].plot.kde(label='original')
        surrogateDF[i].plot.kde(label='surrogate')
        
        plt.legend()
        plt.title(i)
        plt.savefig('distribution/'+i+'_diff')
  
visdiff()
  