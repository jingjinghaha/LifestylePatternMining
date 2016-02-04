# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

from nltk import wordpunct_tokenize
import matplotlib.pyplot as plt

def plot_overall_diet():
	sizes = []
	labels = []
	for line in open('diet/dietOverallTypeFreq/all_dietType_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words
		#print words[0], type(words[1])
		#words[0]: diet type
		#words[1]: type frequency
		sizes.append(int(words[1]))
		#print sizes
		labels.append(words[0])
		#print labels
	labels = tuple(labels)
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['overall_dietType'])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('visOverallPattPie/visOverallDietTypePie/overall_dietType')
	return sizes, labels

def plot_overall_activity():
	sizes = []
	labels = []
	for line in open('activity/activityOverallTypeFreq/all_activityType_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: act type
		#words[1]: type frequency
		sizes.append(int(words[1]))
		#print sizes
		labels.append(words[0])
		#print labels
	labels = tuple(labels)
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['overall_activityType'])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('visOverallPattPie/visOverallActivityTypePie/overall_activityType')
	return sizes, labels

def plotOverallDietActTypeFreq():
	print 'in plotOverallDietActTypeFreq()'
	plot_overall_diet()
	plot_overall_activity()

# plotOverallDietActTypeFreq()