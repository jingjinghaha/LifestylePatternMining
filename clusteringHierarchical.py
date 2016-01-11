# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 17:34:11 2016

@author: wu34
"""

import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
import utilise
import pydendroheatmap as pdh

Domain = ['DietItem','ActItem','DietType','ActType']
Metric = ['TF','TFIDF']
Sim = ['jaccard','novelJaccard','TFCosin','TFEclud','TFIDFCosin','TFIDFEclud']
for domain in Domain:
	for metric in Metric:
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
	# for sim in Sim:
		# dietSimilarity_dict = {}
		# if domain == 'DietItem':
			# Similarity_dict = utilise.SimilarityDict(domain,sim)
		# elif domain == 'ActItem':
			# Similarity_dict = utilise.SimilarityDict(domain,sim)
		# elif domain == 'DietType':
			# Similarity_dict = utilise.SimilarityDict(domain,sim)
		# elif domain == 'ActType':
			# Similarity_dict = utilise.SimilarityDict(domain,sim)
		# X = visSimilarityMat.similarityDict2array(Similarity_dict,0)
		
		# method can be ward, complete, average
		method = 'ward'
		row_method = method
		row_metric = 'euclidean'
		column_method = method
		column_metric = 'euclidean'

		# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.pdist.html
		# d1 = ssd.pdist(X,'cosine')
		d1 = ssd.pdist(X)
		# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform
		D1 = ssd.squareform(d1)  # full matrix
		# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
		Y1 = sch.linkage(D1, method=row_method, metric=row_metric) 
		row_idxing = sch.leaves_list(Y1)

		# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.pdist.html
		d2 = ssd.pdist(X.T)
		# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform
		D2 = ssd.squareform(d2)
		# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
		Y2 = sch.linkage(D2, method=column_method, metric=column_metric) 
		col_idxing = sch.leaves_list(Y2)

		heatmap_array = X[:,col_idxing][row_idxing,:] #a numpy.ndarray or numpy.matrix, for this example, let's say mxn array
		top_dendrogram = Y2 #a (n-1) x 4 array
		side_dendrogram = Y1 #a (m-1) x 4 array

		row_labels = range(X.shape[0])
		# col_labels = range(X.shape[1])
		if domain == 'DietItem':
			col_labels = utilise.itemDict2list(utilise.genDietItemDict())
		elif domain == 'ActItem':
			col_labels = utilise.itemDict2list(utilise.genActItemDict())
		elif domain == 'DietType':
			col_labels = utilise.itemDict2list(utilise.genDietTypeDict())
		elif domain == 'ActType':
			col_labels = utilise.itemDict2list(utilise.genActTypeDict())
		col_idxing = list(col_idxing)
		row_idxing = list(row_idxing)

		new_row_labels = []
		new_col_labels = []
		for i in range(len(row_idxing)):
			new_row_labels.append(str(row_labels[row_idxing[i]]))
		for j in range(len(col_idxing)):
			new_col_labels.append(str(col_labels[col_idxing[j]]))

		heatmap = pdh.DendroHeatMap(heat_map_data=heatmap_array, left_dendrogram=side_dendrogram, top_dendrogram=top_dendrogram)
		heatmap.title = 'HC_'+domain+'_'+metric+'_'+method
		# heatmap.title = 'HC_'+domain+'_'+sim+'_'+method
		heatmap.row_labels = new_row_labels
		heatmap.col_labels = new_col_labels

		# heatmap.show()
		heatmap.export('VisClustering'+domain+'Pattern/Hierarchy_'+metric+'_'+method+'.png')
		# heatmap.export('VisClustering'+domain+'Pattern/Hierarchy_'+sim+'_'+method+'.png')
