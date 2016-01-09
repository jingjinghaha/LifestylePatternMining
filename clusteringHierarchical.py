# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 17:34:11 2016

@author: wu34
"""

import matplotlib.pyplot as pylab
import matplotlib as mpl
import scipy
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as dist
import numpy
import utilise
import pydendroheatmap as pdh

Domain = ['DietItem','ActItem','DietType','ActType']
# metric: TF, TFIDF
metric = 'TF'
for domain in Domain:
	if metric == 'TF':
		if domain == 'DietItem':
			X = utilise.genDietItemTFArray()
		elif domain == 'ActItem':
			X = utilise.genActItemTFArray()
		elif domain == 'DietType':
			X = utilise.genDietTypeTFArray()
		elif domain == 'ActType':
			X = utilise.genActTypeTFArray()
	elif metric == 'TFIDF':
		if domain == 'DietItem':
			X = utilise.DietItemTfidfArray()
		elif domain == 'ActItem':
			X = utilise.ActItemTfidfArray()
		elif domain == 'DietType':
			X = utilise.DietTypeTfidfArray()
		elif domain == 'ActType':
			X = utilise.ActTypeTfidfArray()
	
	row_method = 'single'
	row_metric = 'euclidean'
	column_method = 'single'
	column_metric = 'euclidean'

	# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.pdist.html
	d1 = dist.pdist(X,'cosine')
	# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform
	D1 = dist.squareform(d1)  # full matrix
	# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
	Y1 = sch.linkage(D1, method=row_method, metric=row_metric) 
	row_idxing = sch.leaves_list(Y1)

	# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.pdist.html
	d2 = dist.pdist(X.T,'cosine')
	# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform
	D2 = dist.squareform(d2)
	# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
	Y2 = sch.linkage(D2, method=column_method, metric=column_metric) 
	col_idxing = sch.leaves_list(Y2)

	heatmap_array = X[:,col_idxing][row_idxing,:] #a numpy.ndarray or numpy.matrix, for this example, let's say mxn array
	top_dendrogram = Y2 #a (n-1) x 4 array
	side_dendrogram = Y1 #a (m-1) x 4 array

	row_labels = range(X.shape[0])
	col_labels = range(X.shape[1])
	col_idxing = list(col_idxing)
	row_idxing = list(row_idxing)
	# print col_idxing
	# print row_idxing
	new_row_labels = []
	new_col_labels = []
	for i in range(len(row_idxing)):
		new_row_labels.append(str(row_labels[row_idxing[i]]))
	for j in range(len(col_idxing)):
		new_col_labels.append(str(col_labels[col_idxing[j]]))

	heatmap = pdh.DendroHeatMap(heat_map_data=heatmap_array, left_dendrogram=side_dendrogram, top_dendrogram=top_dendrogram)
	heatmap.title = 'Hierarchical Clustering ('+domain+'_'+metric+')'
	heatmap.row_labels = new_row_labels
	heatmap.col_labels = new_col_labels

	# heatmap.show()
	heatmap.export('VisClustering'+domain+'Pattern/Hierarchy_'+metric+'.png')
