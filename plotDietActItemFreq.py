# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""

from nltk import wordpunct_tokenize
import matplotlib.pyplot as plt

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#plot diet pie chart for single user
def plot_single_diet(subjectID,f):
	sizes = []
	labels = []
	temp = 0
	for line in open('diet_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: Item
		#words[3]: Item frequency
		if int(words[3]) > f:
			sizes.append(int(words[3]))
			#print sizes
			labels.append(words[1])
			#print labels
		else:
			temp += int(words[3])
	# sizes.append(temp)
	# labels.append('others')
	labels = tuple(labels)
	# plt.figure()
	# plt.pie(sizes, labels=labels,autopct='%1.1f%%')
	# plt.xlabel('subject'+subjectID)
	# plt.axis('equal')
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['diet_subject'+subjectID+'_minF_'+str(f)])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('diet_subject'+subjectID+'_minF_'+str(f))
	return sizes, labels

#plot activity pie chart for single user
def plot_single_activity(subjectID,f):
	sizes = []
	labels = []
	temp = 0
	for line in open('activity_frequency_'+subjectID+'.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[1], type(words[3])
		#words[1]: Item
		#words[3]: Item frequency
		if int(words[3]) > f:
			sizes.append(int(words[3]))
			#print sizes
			labels.append(words[1])
			#print labels
		else:
			temp += int(words[3])
	# sizes.append(temp)
	# labels.append('others')
	labels = tuple(labels)
	# plt.figure()
	# plt.pie(sizes, labels=labels,autopct='%1.1f%%')
	# plt.xlabel('subject'+subjectID)
	# plt.axis('equal')
	fig = plt.figure()
	ax = fig.gca()
	ax.pie(sizes, labels=labels,autopct='%1.1f%%')
	ax.set_xticks([0])
	ax.set_yticks([0])
	ax.set_xticklabels(['activity_subject'+subjectID+'_minF_'+str(f)])
	ax.set_yticklabels([" "])
	ax.set_aspect('equal')
	plt.savefig('activity_subject'+subjectID+'_minF_'+str(f))
	return sizes, labels


# plot_single_diet('039')
# plot_single_activity('039')
# for n in range(0,30):
	# subjectID = available_list[n]
	# i = n%6
	# j = n/6
	# sizes,labels = plot_single_diet(subjectID)
	# fig = plt.figure()
	# ax = fig.gca()
	# ax.pie(sizes,labels=labels,autopct='%1.1f%%',radius=0.25, center=(i,j), frame=True)
# ax.set_aspect('equal')
# plt.show()

def plotDietActItemFreq(f):
	print 'in plotDietActItemFreq()'
	for subjectID in available_list:
		plot_single_diet(subjectID,f)
		plot_single_activity(subjectID,f)
	
# plotDietActItemFreq()
