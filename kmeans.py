from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from nltk.cluster import KMeansClusterer, euclidean_distance
#from vectorization import *
# def demo():
    # # example from figure 14.9, page 517, Manning and Schutze

    # from nltk.cluster import KMeansClusterer, euclidean_distance
    # import numpy
    # vectors = [numpy.array(f) for f in [[2, 1], [1, 3], [4, 7], [6, 7]]]
    # means = [[4, 3], [5, 5]]

    # clusterer = KMeansClusterer(2, euclidean_distance, initial_means=means)
    # clusters = clusterer.cluster(vectors, True, trace=True)

    # print('Clustered:', vectors)
    # print('As:', clusters)
    # print('Means:', clusterer.means())
    # print()

    # vectors = [numpy.array(f) for f in [[3, 3], [1, 2], [4, 2], [4, 0], [2, 3], [3, 1]]]

    # # test k-means using the euclidean distance metric, 2 means and repeat
    # # clustering 10 times with random seeds

    # clusterer = KMeansClusterer(2, euclidean_distance, repeats=10)
    # clusters = clusterer.cluster(vectors, True)
    # print('Clustered:', vectors)
    # print('As:', clusters)
    # print('Means:', clusterer.means())
    # print()

    # classify a new vector
    # vector = numpy.array([3, 3])
    # print('classify(%s):' % vector, end=' ')
    # print(clusterer.classify(vector))
    # print()

    
# if __name__ == '__main__':
      # demo()
     
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)
    
def distCosin(vecA,vecB):
    innerProduct = sum(vecA*vecB)
    print "ineer product",innerProduct
    absA = sqrt(sum(power(vecA,2)))
    absB = sqrt(sum(power(vecB,2)))
    print absA,absB
    return 1 - (innerProduct)/(absA*absB)
    
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids
    
def kMeans(dataSet, k = 4, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points                                   #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        # print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment
    
def mean_Sparse(dataset,position):
    len = dataset['len']
    m = shape(position)[0]
    #print m
    origin = []
    dic = {}
    for i in range(0,m):
        tmp = dataset[position[i]]
        origin.extend(tmp)
        for item in tmp:
            c=dic.setdefault(item,0)
            dic[item] = c+1
    #print "origin:",origin
    originList = list(set(origin))
    #print "originList:",originList
    means = reverse_sparse(len,originList)
    #print dic
    #print "means",means
    #print type(means)
    for item in originList:
        means[item] = float(dic[item])/float(m) 
    return means
        
def reverse_sparse(termNumber,position):
    pos = array([0.0]*termNumber)
    pos[position] = 1.0
    return pos
        
def kMeans_Sparse(dataSet, k, distMeas=distEclud):
    termNum = dataSet['len']
    m = len(dataSet)-1
    clusterAssment = mat(zeros((m,2)))
    centroids = []
    old = []
    b=dataSet.keys()
    del(b[b.index('len')])
    b.sort()
    print b
    for i in range(k):
        tmp = random.randint(0,len(b)-1)
        while tmp in old:
            tmp = random.randint(0,len(b)-1)
        old.append(tmp)
        centroids.append(reverse_sparse(termNum,dataSet[b[tmp]]))
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in b:#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(reverse_sparse(termNum,dataSet[i]),centroids[j])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[b.index(i),0] != minIndex: clusterChanged = True
            clusterAssment[b.index(i),:] = minIndex,minDist**2
        #print centroids
        for cent in range(k):#recalculate centroids
            position = nonzero(clusterAssment[:,0].A==cent)[0]
            #ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent] = mean_Sparse(dataSet, array(b)[position]) #assign centroid to mean 
    return centroids, clusterAssment
    
def miniBatch_KMeans_Sparse(dataSet,k,batchSize,iterations,distMeas=distEclud,L1 = False):  
    termNum = dataSet['len']
    m = len(dataSet)-1
    clusterAssment = mat(zeros((m,2)))
    centroids = []
    old = []
    b=dataSet.keys()
    del(b[b.index('len')])
    b.sort()
    print b
    for i in range(k):
        tmp = random.randint(0,len(b)-1)
        while tmp in old:
            tmp = random.randint(0,len(b)-1)
        old.append(tmp)
        centroids.append(reverse_sparse(termNum,dataSet[b[tmp]]))
    v={}
    for i in range(k):
        v.setdefault(i,0)
    for i in range(iterations):
        old = []
        batchM = []
        for i in range(batchSize):
            tmp = random.randint(0,len(b)-1)
            while tmp in old:
                tmp = random.randint(0,len(b)-1)
            old.append(tmp)
            batchM.append(dataSet[b[tmp]])
        cacheCenter = {}
        for m in range(len(batchM)):
            cacheCenter.setdefault(m,None)
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(reverse_sparse(termNum,batchM[m]),centroids[j])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            cacheCenter[m] = minIndex
        for m in range(len(batchM)):
            c = cacheCenter[m]
            v[c] = v[c] + 1
            theta = 1.0/float(v[c])
            centroids[c] = (1.0-theta)*centroids[c] + theta*reverse_sparse(termNum,batchM[m])
        if L1:
            # do projection here#
            pass
    for i in b:#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(reverse_sparse(termNum,dataSet[i]),centroids[j])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            clusterAssment[b.index(i),:] = minIndex,minDist**2 
    fw = open ('Mini_Batch_cluster.txt','w')
    for cent in range(k):#recalculate centroids
            position = nonzero(clusterAssment[:,0].A==cent)[0]
            #ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            #centroids[cent] = mean_Sparse(dataSet, array(b)[position]) #assign centroid to mean 
            fw.write("%-30s"%('Cluster '+str(cent)+':',))
            for i in range(shape(array(b)[position])[0]):
                fw.write ("%-10s"%((array(b)[position])[i]))
            fw.write('\n')
    return centroids, clusterAssment

    
# def NTLK_kMeansdef(dataSet, k, distMeas=euclidean_distance, createCent=randCent):
    # means=[]
    # initilalcentroids = createCent(mat(dataSet),k)
    # for i in range(k):
        # tmp=[]
        # for j in range(shape(initilalcentroids)[1]):
            # tmp.append(initilalcentroids[i,j])
        # means.append(tmp) 
    # clusterer = KMeansClusterer(k, distMeas, initial_means=means)
    # vectors = [array(f) for f in dataSet]
    # clusters = clusterer.cluster(vectors, True, trace=True)
    # return clusterer.means(),clusters
    

# dat = loadDataSet('testSet.txt')
# datmat = mat(dat)
# myCentroids, clustAssing = kMeans(datmat,4,distMeas=distEclud,createCent=randCent)
# Cen, Ass = NTLK_kMeansdef(dat,4,distMeas=euclidean_distance,createCent=randCent)
# print myCentroids, clustAssing 
# print Cen, Ass
# fig  = plt.figure()
# ax = fig.add_subplot(121)
# ax.scatter(array(dat)[:,0],array(dat)[:,1],c=array(clustAssing)[:,0])
# ax1 = fig.add_subplot(122)
# ax1.scatter(array(dat)[:,0],array(dat)[:,1],c=array(Ass))
# plt.show()
# dataSet = {1:[1,2],2:[3,4],3:[5,6],'len' :7}
# b=array([1, 3])
# mean_Sparse(dataSet,b)