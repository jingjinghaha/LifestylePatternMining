# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""

from nltk import wordpunct_tokenize
import matplotlib.pyplot as plt

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#plot diet type pie chart for single user
def plot_single_diet(subjectID):
	sizes = []
	labels = []
	temp = 0
	for line in open('dietTypeFreq/dietType_frequency_'+subjectID+'.txt','r'):
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
	ax.set_xticklabels(['dietType_subject'+subjectID])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('VisDietTypePattPie/dietType_subject'+subjectID)
	return sizes, labels

#plot activity type pie chart for single user
def plot_single_activity(subjectID):
	sizes = []
	labels = []
	temp = 0
	for line in open('activityTypeFreq/activityType_frequency_'+subjectID+'.txt','r'):
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
	ax.set_xticklabels(['activityType_subject'+subjectID])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('VisActivityTypePattPie/activityType_subject'+subjectID)
	return sizes, labels

def plotDietActTypeFreq():
	print 'in plotDietActTypeFreq()'
	for subjectID in available_list:
		plot_single_diet(subjectID)
		plot_single_activity(subjectID)
	
# plotDietActTypeFreq()
