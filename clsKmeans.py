# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 14:45:39 2016

@author: wu34
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import utilise
import dataGen4DietAct
from kmeans import * 

# Domain = ['DietItem','ActItem','DietType','ActType','ActDietItem','ActDietType']
Domain = ['DietType','ActType']

def KM(domain, n_clusters):
    if domain == 'DietType':
        X = dataGen4DietAct.genDietTypeTFArray()
    elif domain == 'ActType':
        X = dataGen4DietAct.genActTypeTFArray()

    X = utilise.normArray(X)
    # print X
    # print X.shape
    
    Inertia = []
    Labels = []
    # range_n_clusters = [2, 3, 4, 5, 6]
    # range_n_clusters = [4]
    
    # for n_clusters in range_n_clusters:
    for j in range(300):

        kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
  
        # kmeans.fit(reduced_data)
        kmeans.fit(X)
        inertia = kmeans.inertia_
        Inertia.append(inertia)
        # print domain,inertia
        labels = kmeans.labels_
        Labels.append(labels)
        # print labels

    min = np.min(Inertia)
    for i in range(len(Inertia)):
        if Inertia[i] == min:
            inertia = Inertia[i] 
            labels = Labels[i]
    
#    a,b = kMeans(X,2)
#    print b[:,0].shape
#    print a,b[:,0].ravel()
#    print sum(b[:,1].ravel())
    
    print domain, n_clusters,inertia, labels

def plotPCA(reduced_data,):
    kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
    
    # plot based on PCA 
    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    for i in range(reduced_data.shape[0]):
        plt.text(reduced_data[i, 0], reduced_data[i, 1],i)

    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=100, linewidths=2,
                color='w', zorder=10)
    plt.title('K-means clustering (PCA-reduced data)\n'
              'Centroids are marked with white cross')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    #plt.savefig('visClustering'+domain+'Pattern/KMeans_'+metric+'_'+str(n_clusters)+'_'+str(j))
    # plt.show()


def KM_nonslp(domain,n_clusters):
    if domain == 'DietType':
        X = dataGen4DietAct.genDietTypeTFArrayWithSlp()
    else:
        X = dataGen4DietAct.genActTypeTFArrayWithSlp()
    
    X = utilise.normArray(X)

    Inertia = []
    Labels = []

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
    
    print domain,n_clusters,inertia, labels
    

for n_clusters in range(2,5):
    for domain in Domain:
        KM_nonslp(domain,n_clusters)

# KM('ActItem', 'TFIDF')
# KM_slp(4)