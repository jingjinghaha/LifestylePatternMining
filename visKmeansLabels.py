# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:10:18 2016

@author: wu34
"""
from sklearn.cluster import KMeans
import xlwt
import matplotlib.pyplot as plt
import numpy as np
import utilise
import dataGen4DietAct
import validation4DC
import artificialDataGenerator 
import newDataProcess

# Domain = ['ActItem','DietItem','DietType','ActType','ActDietItem','ActDietType']
Domain = ['DietType','ActType']

def bestLabel(labelsDietType,labelsActType):

    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0

    for domain in Domain:
        if domain == 'DietType':
            labels = utilise.string2array(labelsDietType) 
            row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
            X = dataGen4DietAct.genDietTypeTFArray()
        elif domain == 'ActType':
            labels = utilise.string2array(labelsActType)
            row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
            X = dataGen4DietAct.genActTypeTFArray()
        X = utilise.normArray(X)
        
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1 
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            # we don't have to do normalization here, as the input X has already been normalized 
            # totalSum = np.sum(meanVec[0])
            # print totalSum
            # meanVec = meanVec/totalSum
            
            # # normalize the meanVec 
            # firstMax = np.max(meanVec)
            # meanVec = meanVec/firstMax
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMax

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                    plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

def bestLabel4DC(labelsDietType,labelsActType):

    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0

    for domain in Domain:
        if domain == 'DietType':
            labels = utilise.string2array(labelsDietType)
            X = validation4DC.getDietTypeTFArray4DC()
            row_labels = utilise.itemDict2list(dataGen4DietAct.genDietTypeDict())
        elif domain == 'ActType':
            labels = utilise.string2array(labelsActType)
            X = validation4DC.getActTypeTFArray4DC()
            row_labels = utilise.itemDict2list(dataGen4DietAct.genActTypeDict())
        print X 
        X = utilise.normArray(X)
        print X
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            # print stdVec
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            # we don't have to do normalization here, as the input X has already been normalized 
            # totalSum = np.sum(meanVec[0])
            # print totalSum
            # meanVec = meanVec/totalSum
            
            # # normalize the meanVec 
            # firstMax = np.max(meanVec)
            # meanVec = meanVec/firstMax
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMax

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
#            plt.errorbar(x,meanVec,yerr=stdVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    # print k,domain,n_clusters,meanVec[j],row_labels[j]
                if row_labels[j] == 'transportation1':
                    plt.text(x[j],meanVec[j],'walk')
                elif row_labels[j] == 'transportation2':
                    plt.text(x[j],meanVec[j],'car')
                elif row_labels[j] == 'transportation3':
                    plt.text(x[j],meanVec[j],'bike')
                else:
                    plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_OriginalSubs_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

# def clusteringKmeansLabels():
    # for domain in Domain:
        # for n_clusters in range(4,5):
            # for metric in Metric:
                # bestLabel(domain,metric,n_clusters)

#def clusteringKmeansLabels():
#   for n_clusters in range(2,3):
#       bestLabel('TF',n_clusters)

def clusteringKmeansLabelsOriginal():
    labelsDietType = '1 1 0 1 1 1 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 1 1 1'
    labelsActType = '1 0 1 1 0 0 2 2 2 1 2 0 1 2 1 2 0 1 1 2 0 1 1 2 1 1 0 2 1'
    # remove compositeP from diet + remove others from activity 
#    labelsDietType = '1 0 0 1 0 1 0 0 1 0 1 1 1 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 0'
#    labelsActType = '0 2 0 0 2 2 1 1 1 0 1 2 0 1 0 1 2 0 0 1 2 0 0 1 0 0 2 1 0'
    bestLabel4DC(labelsDietType,labelsActType)
    
def clusteringKmeansLabelsOriginalDays():
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0
    
    df,cols = artificialDataGenerator.originalData()
    for domain in Domain:
        print df.columns 
        if domain == 'DietType':
            df_temp = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables']]
            row_labels = df_temp.columns 
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=2, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        else:
            df_temp = df[['entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy']]
            row_labels = df_temp.columns             
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=3, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            print stdVec
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMaxO

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
#            plt.errorbar(x,meanVec,yerr=stdVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                if row_labels[j] == 'transportation1':
                    plt.text(x[j],meanVec[j],'walk')
                elif row_labels[j] == 'transportation2':
                    plt.text(x[j],meanVec[j],'car')
                elif row_labels[j] == 'transportation3':
                    plt.text(x[j],meanVec[j],'bike')
                else:
                    plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_OriginalDays_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')
    
def clusteringKmeansLabelsArtificialDays():
    
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0
    
    df = artificialDataGenerator.artificialData()
    for domain in Domain:
        print df.columns 
        if domain == 'DietType':
            df_temp = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables']]
            row_labels = df_temp.columns 
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=2, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        else:
            df_temp = df[['entertainmentRelax','social','sport','transportation1','transportation2','transportation3','workStudy']]
            row_labels = df_temp.columns             
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=3, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            print stdVec
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMaxO

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
#            plt.errorbar(x,meanVec,yerr=stdVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                if row_labels[j] == 'transportation1':
                    plt.text(x[j],meanVec[j],'walk')
                elif row_labels[j] == 'transportation2':
                    plt.text(x[j],meanVec[j],'car')
                elif row_labels[j] == 'transportation3':
                    plt.text(x[j],meanVec[j],'bike')
                else:
                    plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_ArtificialDays_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

def clusteringKmeansLabelsNewDays():
    
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0
    
    df = newDataProcess.newFeatureFrame() 
    for domain in Domain:
        print df.columns 
        if domain == 'DietType':
            df_temp = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables']]
            row_labels = df_temp.columns 
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=2, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        else:
            df_temp = df[['leisure','social','sport','walk','car','bike','workStudy']]
            row_labels = df_temp.columns             
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=3, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            print stdVec
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMaxO

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
#            plt.errorbar(x,meanVec,yerr=stdVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_NewDataDays_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')
    
def clusteringKmeansLabelsNewSubs():
    
    workbookW = xlwt.Workbook()
    ws = workbookW.add_sheet('sheet1')
    rowW = 0
    
    df = newDataProcess.newSubInfo() 
    for domain in Domain:
        print df.columns 
        if domain == 'DietType':
            df_temp = df[['alcoholD','caffeineD','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables']]
            row_labels = df_temp.columns 
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=2, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        else:
            df_temp = df[['leisure','social','sport','walk','car','bike','workStudy']]
            row_labels = df_temp.columns             
            X = df_temp.as_matrix()
            X = utilise.normArray(X)
            kmeans = KMeans(n_clusters=3, n_init = 3000)
            kmeans.fit(X)
            labels = kmeans.labels_ 
        
        # write the lables to excel file  
        col = 0
        for label in row_labels:
            ws.write(rowW,col,label)
            col += 1 
        rowW += 1 
        
        # print type(labels)
        plt.figure()
        
        n_clusters = np.max(labels) + 1
        
        for k in range(n_clusters):
            class_members = labels == k
            group = [] 
            for x in X[class_members]:
                group.append(x)
            group = np.array(group)
            
            meanVec = np.mean(group,axis=0)
            meanVec.tolist()
            stdVec = np.std(group,axis=0)
            stdVec.tolist() 
            print stdVec
            
            # write the mean vector of each group to excel file 
            col = 0
            for value in meanVec:
                ws.write(rowW,col,value)
                col += 1 
            rowW += 1 
            # print meanVec 
            
            firstMax = np.max(meanVec)
            # print firstMax
            tempVec = np.copy(meanVec)
            for j in range(X.shape[1]):
                if tempVec[j] == firstMax:
                    tempVec[j] = 0
            secondMax = np.max(tempVec)
            # print secondMax
            tempVec2 = np.copy(tempVec)
            for j in range(X.shape[1]):
                if tempVec2[j]==secondMax:
                    tempVec2[j] = 0
            thirdMax = np.max(tempVec2)
            # print thirdMaxO

            
            x = range(X.shape[1])
            plt.plot(x,meanVec)
#            plt.errorbar(x,meanVec,yerr=stdVec)
            # print meanVec
            for j in range(X.shape[1]):
                # if meanVec[j] == firstMax:
                # if meanVec[j] == firstMax or meanVec[j] == secondMax:
                if meanVec[j] == firstMax or meanVec[j] == secondMax or meanVec[j] == thirdMax:
                    ws.write(rowW,0,k)
                    ws.write(rowW,1,domain)
                    ws.write(rowW,2,row_labels[j])
                    ws.write(rowW,3,meanVec[j])
                    rowW += 1 
                    print k,domain,n_clusters,meanVec[j],row_labels[j]
                plt.text(x[j],meanVec[j],row_labels[j])

        # print row_labels
        # plt.xlabel(row_labels)
        plt.title(domain+'_TF_KMeans_'+str(n_clusters))
        plt.savefig('visClustering'+domain+'Pattern/KMeans__TF_NewDataSubs_'+str(n_clusters)+'_groupFreq')
    
    workbookW.save('tempLabels.xls')

clusteringKmeansLabelsNewSubs() 
