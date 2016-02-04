# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 10:51:27 2015

@author: wu34
"""

from nltk import wordpunct_tokenize
import matplotlib.pyplot as plt

def plot_overall_diet(f):
	sizes = []
	labels = []
	temp = 0
	for line in open('diet/dietOverallItemFreq/all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: Item
		#words[1]: Item frequency
		if int(words[1]) > f:
			sizes.append(int(words[1]))
			#print sizes
			labels.append(words[0])
			#print labels
		else:
			temp += int(words[1])
	# sizes.append(temp)
	# labels.append('others')
	labels = tuple(labels)
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['overall_diet_minF_'+str(f)])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('visOverallPattPie/visOverallDietItemPie/overall_diet_minF_'+str(f))
	return sizes, labels

def plot_overall_activity(f):
	sizes = []
	labels = []
	temp = 0
	for line in open('activity/activityOverallItemFreq/all_activity_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: Item
		#words[1]: Item frequency
		if int(words[1]) > f:
			sizes.append(int(words[1]))
			#print sizes
			labels.append(words[0])
			#print labels
		else:
			temp += int(words[1])
	# sizes.append(temp)
	# labels.append('others')
	labels = tuple(labels)
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['overall_activity_minF_'+str(f)])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('visOverallPattPie/visOverallActivityItemPie/overall_activity_minF_'+str(f))
	return sizes, labels

def plotOverallDietActItemFreq(f):
	print 'in plotOverallDietActItemFreq()'
	plot_overall_diet(f)
	plot_overall_activity(f)

# plotOverallDietActItemFreq(10)

