# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:43:57 2016

@author: wu34
"""

import numpy as np
import buildTypeIndex 
import dietActInfoRetrv
import utilise 
import dataGen4DietAct
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
Domain = ['DietType','ActType']

def getActTypeTFArray4DC():
    type_dict = dataGen4DietAct.genActTypeDict()
#    print type_dict
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
    type_dict = dataGen4DietAct.genDietTypeDict()
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
a = dataGen4DietAct.genDietTypeTFArray()


def sihouetteScore(domain):
    if domain == 'DietType':
        X = getDietTypeTFArray4DC()
    elif domain == 'ActType':
        X = getActTypeTFArray4DC() 
    X = utilise.normArray(X)
    reduced_data = PCA(n_components=2).fit_transform(X)
    
    range_n_clusters = [2, 3, 4, 5, 6] 

    for n_clusters in range_n_clusters:
        clusterer = KMeans(n_clusters=n_clusters, n_init = 300)
        clusterer.fit(reduced_data)
        cluster_labels = clusterer.labels_
        
        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print(domain, 'For n_clusters =', n_clusters,
              'The average silhouette_score is :', silhouette_avg)


def KM(domain, n_clusters):
    if domain == 'DietType':
        X = getDietTypeTFArray4DC()
    elif domain == 'ActType':
        X = getActTypeTFArray4DC()
    X = utilise.normArray(X)
    reduced_data = PCA(n_components=2).fit_transform(X)

    Inertia = []
    Labels = []
    
    # for n_clusters in range_n_clusters:
    for j in range(300):

        kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)

        kmeans.fit(reduced_data)
        inertia = kmeans.inertia_
        Inertia.append(inertia)

        labels = kmeans.labels_
        Labels.append(labels)

    min = np.min(Inertia)
    for i in range(len(Inertia)):
        if Inertia[i] == min:
            inertia = Inertia[i] 
            labels = Labels[i] 
    print domain,n_clusters,inertia, labels
    
#for n_clusters in range(2,5):
#    for domain in Domain:
#        KM(domain,n_clusters)

#
#for domain in Domain:
#    sihouetteScore(domain)

