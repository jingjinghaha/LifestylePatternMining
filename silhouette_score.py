# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:00:43 2015

@author: wu34
"""

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import utilise
import dataGen4DietAct
import validation4DC
import artificialDataGenerator

Domain = ['ActType','DietType']
Metric = ['TF']

def sihouetteScore(metric):
    for domain in Domain:
        if metric == 'TF':
            if domain == 'DietType':
                X = dataGen4DietAct.genDietTypeTFArray()
            elif domain == 'ActType':
                X = dataGen4DietAct.genActTypeTFArray()
        elif metric == 'TFIDF':
            if domain == 'DietType':
                X = dataGen4DietAct.DietTypeTfidfArray()
            elif domain == 'ActType':
                X = dataGen4DietAct.ActTypeTfidfArray()
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
            print(metric, domain, 'For n_clusters =', n_clusters,
                  'The average silhouette_score is :', silhouette_avg)

def sihouetteScore4DC(metric):
    for domain in Domain:
        if domain == 'DietType':
            X = validation4DC.getDietTypeTFArray4DC()
        elif domain == 'ActType':
            X = validation4DC.getActTypeTFArray4DC()
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

def sihouetteScoreArtificialData(metric):
    df,cols = artificialDataGenerator.artificialData()
    for domain in Domain:
        print df.columns 
        if domain == 'DietType':
            df_temp = df[['alcoholD','caffeineD','compositeP','dairyP','eggP','fruitP','grainP','meatP','seafood','snack','starchyP','vegetables']]
        else:
            df_temp = df[['entertainmentRelax','others','social','sport','transportation1','transportation2','transportation3','workStudy']]
        X = df_temp.as_matrix()
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
        

for metric in Metric:
    sihouetteScoreArtificialData(metric)
