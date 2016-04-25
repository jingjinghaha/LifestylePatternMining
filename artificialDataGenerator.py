# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 11:46:47 2016

@author: wu34
"""
import dataGen4SlpPrd
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#print np.random.rand(100) #random value in (0,1) fit average distribution 
#print np.random.normal(0.2,0.4,100) #normal distribution with mean and std 


def generateOneDay(df): 
    #independent variables generation: gender, walk, entertainment, alcohol 
    gender = np.random.normal(df['gender'].mean(),df['gender'].std())
    if gender>0.5:
        gender = 1
    else:
        gender = 0
    
    walk = np.random.normal(df['transportation1'].mean(),df['transportation1'].std())
    if walk>2.5:
        walk = 3
    elif walk>1.5:
        walk = 2
    elif walk>0.5:
        walk = 1
    else:
        walk = 0
    
    social = np.random.normal(df['social'].mean(),df['social'].std())
    if social>2.5:
        social = 3
    elif social>1.5:
        social = 2
    elif social>0.5:
        social = 1
    else:
        social = 0
    
    sport = np.random.normal(df['sport'].mean(),df['sport'].std())
    if sport>2.5:
        sport = 3
    elif sport>1.5:
        sport = 2
    elif sport>0.5:
        sport = 1
    else:
        sport = 0
    
    alcohol = np.random.normal(df['alcoholD'].mean(),df['alcoholD'].std())
    if alcohol>5.5:
        alcohol = 6
    elif alcohol>4.5:
        alcohol = 5
    elif alcohol>3.5:
        alcohol = 4
    elif alcohol>2.5:
        alcohol = 3
    elif alcohol>1.5:
        alcohol = 2
    elif alcohol>0.5:
        alcohol = 1
    else:
        alcohol = 0
    
    #dependent variables generation: bike, car 
    if gender == 0: 
        poss = np.random.rand() 
        if poss>0.3:
            temp_df = df[df['transportation3']>0]
            bike = np.random.normal(temp_df['transportation3'].mean(),temp_df['transportation3'].std())
            if bike>2.5:
                bike = 3
            elif bike>1.5:
                bike = 2
            else:
                bike = 1
        else:
            bike = 0 
    elif gender == 1:
        poss = np.random.rand()
        if poss>0.3:
            bike = 0 
        else:
            temp_df = df[df['transportation3']>0]
            bike = np.random.normal(temp_df['transportation3'].mean(),temp_df['transportation3'].std())
            if bike>2.5:
                bike = 3
            elif bike>1.5:
                bike = 2
            else:
                bike = 1
    
    #dependent variables generation: workStudy 
    if bike == 3: 
        poss = np.random.rand()
        if poss>0.1:
            temp_df = df[df['workStudy']>0]
            workStudy = np.random.normal(temp_df['workStudy'].mean(),temp_df['workStudy'].std())
            if workStudy>2.5:
                workStudy = 3
            elif workStudy>1.5:
                workStudy = 2
            else:
                workStudy = 1
        else:
            workStudy = 0
    elif bike == 2: 
        poss = np.random.rand()
        if poss>0.2:
            temp_df = df[df['workStudy']>0]
            workStudy = np.random.normal(temp_df['workStudy'].mean(),temp_df['workStudy'].std())
            if workStudy>2.5:
                workStudy = 3
            elif workStudy>1.5:
                workStudy = 2
            else:
                workStudy = 1
        else:
            workStudy = 0        
    elif bike == 1: 
        poss = np.random.rand()
        if poss>0.3:
            temp_df = df[df['workStudy']>0]
            workStudy = np.random.normal(temp_df['workStudy'].mean(),temp_df['workStudy'].std())
            if workStudy>2.5:
                workStudy = 3
            elif workStudy>1.5:
                workStudy = 2
            else:
                workStudy = 1
        else:
            workStudy = 0  
    elif bike == 0: 
        poss = np.random.rand()
        if poss>0.4:
            temp_df = df[df['workStudy']>0]
            workStudy = np.random.normal(temp_df['workStudy'].mean(),temp_df['workStudy'].std())
            if workStudy>2.5:
                workStudy = 3
            elif workStudy>1.5:
                workStudy = 2
            else:
                workStudy = 1
        else:
            workStudy = 0  
    
    #dependent variables generation: cafe and Snack
    if walk == 3: 
        poss = np.random.rand()
        if poss>0.4:
            temp_df = df[df['caffeineD']>0]
            cafe = np.random.normal(temp_df['caffeineD'].mean(),temp_df['caffeineD'].std())
            if cafe>5.5:
                cafe = 6
            elif cafe>4.5:
                cafe = 5
            elif cafe>3.5:
                cafe = 4
            elif cafe>2.5:
                cafe = 3
            elif cafe>1.5:
                cafe = 2
            else:
                cafe = 1
        else:
            cafe = 0
    elif walk == 2: 
        poss = np.random.rand()
        if poss>0.43:
            temp_df = df[df['caffeineD']>0]
            cafe = np.random.normal(temp_df['caffeineD'].mean(),temp_df['caffeineD'].std())
            if cafe>5.5:
                cafe = 6
            elif cafe>4.5:
                cafe = 5
            elif cafe>3.5:
                cafe = 4
            elif cafe>2.5:
                cafe = 3
            elif cafe>1.5:
                cafe = 2
            else:
                cafe = 1
        else:
            cafe = 0      
    elif walk == 1: 
        poss = np.random.rand()
        if poss>0.47:
            temp_df = df[df['caffeineD']>0]
            cafe = np.random.normal(temp_df['caffeineD'].mean(),temp_df['caffeineD'].std())
            if cafe>5.5:
                cafe = 6
            elif cafe>4.5:
                cafe = 5
            elif cafe>3.5:
                cafe = 4
            elif cafe>2.5:
                cafe = 3
            elif cafe>1.5:
                cafe = 2
            else:
                cafe = 1
        else:
            cafe = 0  
    elif walk == 0: 
        poss = np.random.rand()
        if poss>0.5:
            temp_df = df[df['caffeineD']>0]
            cafe = np.random.normal(temp_df['caffeineD'].mean(),temp_df['caffeineD'].std())
            if cafe>5.5:
                cafe = 6
            elif cafe>4.5:
                cafe = 5
            elif cafe>3.5:
                cafe = 4
            elif cafe>2.5:
                cafe = 3
            elif cafe>1.5:
                cafe = 2
            else:
                cafe = 1
        else:
            cafe = 0 

    if walk == 3: 
        poss = np.random.rand()
        if poss>0.2:
            temp_df = df[df['snack']>0]
            snack = np.random.normal(temp_df['snack'].mean(),temp_df['snack'].std())
            if snack>5.5:
                snack = 6
            elif snack>4.5:
                snack = 5
            elif snack>3.5:
                snack = 4
            elif snack>2.5:
                snack = 3
            elif snack>1.5:
                snack = 2
            else:
                snack = 1
        else:
            snack = 0
    elif walk == 2: 
        poss = np.random.rand()
        if poss>0.3:
            temp_df = df[df['snack']>0]
            snack = np.random.normal(temp_df['snack'].mean(),temp_df['snack'].std())
            if snack>5.5:
                snack = 6
            elif snack>4.5:
                snack = 5
            elif snack>3.5:
                snack = 4
            elif snack>2.5:
                snack = 3
            elif snack>1.5:
                snack = 2
            else:
                snack = 1
        else:
            snack = 0      
    elif walk == 1: 
        poss = np.random.rand()
        if poss>0.4:
            temp_df = df[df['snack']>0]
            snack = np.random.normal(temp_df['snack'].mean(),temp_df['snack'].std())
            if snack>5.5:
                snack = 6
            elif snack>4.5:
                snack = 5
            elif snack>3.5:
                snack = 4
            elif snack>2.5:
                snack = 3
            elif snack>1.5:
                snack = 2
            else:
                snack = 1
        else:
            snack = 0  
    elif walk == 0: 
        poss = np.random.rand()
        if poss>0.5:
            temp_df = df[df['snack']>0]
            snack = np.random.normal(temp_df['snack'].mean(),temp_df['snack'].std())
            if snack>5.5:
                snack = 6
            elif snack>4.5:
                snack = 5
            elif snack>3.5:
                snack = 4
            elif snack>2.5:
                snack = 3
            elif snack>1.5:
                snack = 2
            else:
                snack = 1
        else:
            snack = 0
 
    #generate variables that are not in the dependency graph 
    dairy = np.random.normal(df['dairyP'].mean(),df['dairyP'].std())
    if dairy>5.5:
        dairy = 6
    elif dairy>4.5:
        dairy = 5
    elif dairy>3.5:
        dairy = 4
    elif dairy>2.5:
        dairy = 3
    elif dairy>1.5:
        dairy = 2
    elif dairy>0.5:
        dairy = 1
    else:
        dairy = 0
    
    grain = np.random.normal(df['grainP'].mean(),df['grainP'].std())
    if grain>5.5:
        grain = 6
    elif grain>4.5:
        grain = 5
    elif grain>3.5:
        grain = 4
    elif grain>2.5:
        grain = 3
    elif grain>1.5:
        grain = 2
    elif grain>0.5:
        grain = 1
    else:
        grain = 0
    
    egg = np.random.normal(df['eggP'].mean(),df['eggP'].std())
    if egg>5.5:
        egg = 6
    elif egg>4.5:
        egg = 5
    elif egg>3.5:
        egg = 4
    elif egg>2.5:
        egg = 3
    elif egg>1.5:
        egg = 2
    elif egg>0.5:
        egg = 1
    else:
        egg = 0
    
    seafood = np.random.normal(df['seafood'].mean(),df['seafood'].std())
    if seafood>5.5:
        seafood = 6
    elif seafood>4.5:
        seafood = 5
    elif seafood>3.5:
        seafood = 4
    elif seafood>2.5:
        seafood = 3
    elif seafood>1.5:
        seafood = 2
    elif seafood>0.5:
        seafood = 1
    else:
        seafood = 0
    
    fruit = np.random.normal(df['fruitP'].mean(),df['fruitP'].std())
    if fruit>5.5:
        fruit = 6
    elif fruit>4.5:
        fruit = 5
    elif fruit>3.5:
        fruit = 4
    elif fruit>2.5:
        fruit = 3
    elif fruit>1.5:
        fruit = 2
    elif fruit>0.5:
        fruit = 1
    else:
        fruit = 0
    
    meat = np.random.normal(df['meatP'].mean(),df['meatP'].std())
    if meat>5.5:
        meat = 6
    elif meat>4.5:
        meat = 5
    elif meat>3.5:
        meat = 4
    elif meat>2.5:
        meat = 3
    elif meat>1.5:
        meat = 2
    elif meat>0.5:
        meat = 1
    else:
        meat = 0
    
    composite = np.random.normal(df['compositeP'].mean(),df['compositeP'].std())
    if composite>5.5:
        composite = 6
    elif composite>4.5:
        composite = 5
    elif composite>3.5:
        composite = 4
    elif composite>2.5:
        composite = 3
    elif composite>1.5:
        composite = 2
    elif composite>0.5:
        composite = 1
    else:
        composite = 0
    
    vegetables = np.random.normal(df['vegetables'].mean(),df['vegetables'].std())
    if vegetables>5.5:
        vegetables = 6
    elif vegetables>4.5:
        vegetables = 5
    elif vegetables>3.5:
        vegetables = 4
    elif vegetables>2.5:
        vegetables = 3
    elif vegetables>1.5:
        vegetables = 2
    elif vegetables>0.5:
        vegetables = 1
    else:
        vegetables = 0
    
    starchy = np.random.normal(df['starchyP'].mean(),df['starchyP'].std())
    if starchy>5.5:
        starchy = 6
    elif starchy>4.5:
        starchy = 5
    elif starchy>3.5:
        starchy = 4
    elif starchy>2.5:
        starchy = 3
    elif starchy>1.5:
        starchy = 2
    elif starchy>0.5:
        starchy = 1
    else:
        starchy = 0

    
    entertainment = np.random.normal(df['entertainmentRelax'].mean(),df['entertainmentRelax'].std())
    if entertainment>2.5:
        entertainment = 3
    elif entertainment>1.5:
        entertainment = 2
    elif entertainment>0.5:
        entertainment = 1
    else:
        entertainment = 0

    car = np.random.normal(df['transportation2'].mean(),df['transportation2'].std())
    if car>2.5:
        car = 3
    elif car>1.5:
        car = 2
    elif car>0.5:
        car = 1
    else:
        car = 0
        
    others = np.random.normal(df['others'].mean(),df['others'].std())
    if others>2.5:
        others = 3
    elif others>1.5:
        others = 2
    elif others>0.5:
        others = 1
    else:
        others = 0
    
    return gender,walk,entertainment,alcohol,car,bike,workStudy,cafe,snack,dairy,grain,egg,seafood,fruit,meat,composite,vegetables,starchy,social,sport,others 


def originalData():
    col1 = dataGen4SlpPrd.genDietTypeLabel()
    col2 = dataGen4SlpPrd.genActTypeLabel()
    cols = col1+col2
    cols.append('gender')
    cols.append('sleepTime')
    cols.append('label')
    
    dataset = dataGen4SlpPrd.genDailyDietActTypeFeaT4DC()
    gender = dataGen4SlpPrd.getGender()
    dataset = np.c_[dataset,gender.ravel()]
    
    time = dataGen4SlpPrd.getSlpTime() 
    dataset = np.c_[dataset,time.ravel()]
    
    label1 = dataGen4SlpPrd.getSlpTimeLabel()
    dataset_l1 = np.c_[dataset,label1.ravel()]
    df = pd.DataFrame(dataset_l1,columns=cols)
    
    return df,cols  

def artificialData():

    df,cols = originalData()
    dd = {}
    for i in range(len(cols)):
        dd[cols[i]] = []
    labels = []
    
    for i in range(10000):
        gender,walk,entertainment,alcohol,car,bike,workStudy,cafe,snack,dairy,grain,egg,seafood,fruit,meat,composite,vegetables,starchy,social,sport,others = generateOneDay(df)
        time = -0.16*gender + 0.056*walk - 0.198*alcohol - 0.11*workStudy +0.074*cafe - 0.01*sport - 0.056*social - 0.015*bike 
        time = ((time + 1.846)/(0.687 + 1.846)*(12 - 5)) + 5 
        if time >= 9.8:
            label = 2
        elif time >= 9.4:
            label = 1
        else:
            label = 0
        dd['gender'].append(gender)
        dd['transportation1'].append(walk)
        dd['entertainmentRelax'].append(entertainment)
        dd['alcoholD'].append(alcohol)
        dd['transportation2'].append(car)
        dd['transportation3'].append(bike)
        dd['workStudy'].append(workStudy)
        dd['snack'].append(snack) 
        dd['caffeineD'].append(cafe)
        dd['dairyP'].append(dairy)
        dd['grainP'].append(grain)
        dd['eggP'].append(egg)
        dd['seafood'].append(seafood)
        dd['fruitP'].append(fruit)
        dd['meatP'].append(meat)
        dd['compositeP'].append(composite)
        dd['vegetables'].append(vegetables)
        dd['starchyP'].append(starchy)
        dd['social'].append(social)
        dd['sport'].append(sport)
        dd['others'].append(others)
        dd['sleepTime'].append(time) 
        dd['label'].append(label)
        labels.append(label)
    
    newDF = pd.DataFrame(dd)
    print newDF['sleepTime'].mean()
    return newDF,labels  

def visdiff():
    newDF,labels = artificialData()
    df,cols = originalData() 
    for i in newDF.columns:
        plt.figure()
        df[i].plot.kde(label='old')
        newDF[i].plot.kde(label='new')
        #newDF[i].hist()
        if i == 'transportation1':
            i = 'walk'
        if i == 'transportation2':
            i = 'car'
        if i == 'transportation3':
            i = 'bike' 
        plt.legend()
        plt.title(i)
        plt.savefig('distribution/'+i+'_new')

#visdiff()
