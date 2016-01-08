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

Domain = ['DietItem','ActItem','DietType','ActType']
# metric: TF, TFIDF
metric = 'TFIDF'
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

	# af = KMeans().fit(X)
	# cluster_centers = af.cluster_centers_
	# print cluster_centers
	# labels = af.labels_
	# print labels
	# n_clusters_ = len(cluster_centers)
	# print('Estimated number of clusters: %d' % n_clusters_)

	range_n_clusters = [2, 3, 4, 5, 6]

	for n_clusters in range_n_clusters:
		reduced_data = PCA(n_components=2).fit_transform(X)
		kmeans = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
		kmeans.fit(reduced_data)

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
		# Plot the centroids as a white X
		centroids = kmeans.cluster_centers_
		plt.scatter(centroids[:, 0], centroids[:, 1],
					marker='x', s=169, linewidths=3,
					color='w', zorder=10)
		plt.title('K-means clustering (PCA-reduced data)\n'
				  'Centroids are marked with white cross')
		plt.xlim(x_min, x_max)
		plt.ylim(y_min, y_max)
		plt.xticks(())
		plt.yticks(())
		plt.savefig('VisClustering'+domain+'Pattern/KMeans_'+metric+'_'+str(n_clusters))
		# plt.show()
		