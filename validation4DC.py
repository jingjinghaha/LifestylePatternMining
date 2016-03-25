# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:43:57 2016

@author: wu34
"""

import numpy as np
import buildTypeIndex 
import dietActInfoRetrv
import utilise 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
Domain = ['DietType','ActType']

def getActTypeTFArray4DC():
    type_dict = utilise.genActTypeDict()
    x = len(available_list)
    n = len(type_dict)
    array = np.zeros((x,n))

    i = 0
    for subjectID in available_list:
        duration = dietActInfoRetrv.getDuration(subjectID)
        
        for n in range(1,duration+1):
            dictWithTime = buildTypeIndex.build_daily_single_activity_index_with_time4DC(subjectID,n)
            for time in dictWithTime:
                for key in type_dict:
                    if type_dict[key] in dictWithTime[time]:
                        array[i,key] += dictWithTime[time][type_dict[key]] 
        i += 1 
    return array 
            
def getDietTypeTFArray4DC():
    type_dict = utilise.genDietTypeDict()
    x = len(available_list)
    n = len(type_dict)
    array = np.zeros((x,n))

    i = 0
    for subjectID in available_list:
        duration = dietActInfoRetrv.getDuration(subjectID)
        
        for n in range(1,duration+1):
            dictWithTime = buildTypeIndex.build_daily_single_diet_index_with_time4DC(subjectID,n)
            for time in dictWithTime:
                for key in type_dict:
                    if type_dict[key] in dictWithTime[time]:
                        array[i,key] += dictWithTime[time][type_dict[key]] 
        i += 1 
    return array 

aa = getDietTypeTFArray4DC()
a = utilise.genDietTypeTFArray()

def KM(domain, metric, n_clusters):
    if metric == 'TF':
        if domain == 'DietType':
            X = getDietTypeTFArray4DC()
        elif domain == 'ActType':
            X = getActTypeTFArray4DC()
    X = utilise.normArray(X)

    Inertia = []
    Labels = []
    
    # for n_clusters in range_n_clusters:
    for j in range(300):

        kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)

        kmeans.fit(X)
        inertia = kmeans.inertia_
        Inertia.append(inertia)

        labels = kmeans.labels_
        Labels.append(labels)

    min = np.min(Inertia)
    for i in range(len(Inertia)):
        if Inertia[i] == min:
            inertia = Inertia[i] 
            labels = Labels[i] 
    print domain,metric,n_clusters,inertia, labels
    
#for n_clusters in range(2,5):
#    for domain in Domain:
#        KM(domain, 'TF',n_clusters)
        
        
        
#str1 = '1 2 1 1 0 0 0 0 2 1 0 0 1 0 2 0 0 1 1 0 2 1 1 0 1 1 0 2 2'
#str2 = '1 2 1 1 2 2 0 0 0 1 0 2 1 0 1 0 2 1 1 0 2 1 1 0 1 1 2 0 1'
#l1 = str1.split(' ')
#l2 = str2.split(' ')
#
#for i in range(len(l1)):
#    if l1[i] != l2[i]:
#        print i,l1[i],l2[i] 



def sihouetteScore(domain,metric):
    if metric == 'TF':
        if domain == 'DietType':
            X = getDietTypeTFArray4DC()
        elif domain == 'ActType':
            X = getActTypeTFArray4DC() 
    X = utilise.normArray(X)
    
    range_n_clusters = [2, 3, 4, 5, 6] 

    for n_clusters in range_n_clusters:
        clusterer = KMeans(n_clusters=n_clusters, n_init = 300)
        clusterer.fit(X)
        cluster_labels = clusterer.labels_
        
        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print(metric, domain, 'For n_clusters =', n_clusters,
              'The average silhouette_score is :', silhouette_avg)


for domain in Domain:
    sihouetteScore(domain,'TF')
