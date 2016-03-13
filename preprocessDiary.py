# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:24:53 2015

@author: wu34
"""

import string
import re
import nltk
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
#from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.stem.lancaster import LancasterStemmer
# from nltk.stem.porter import PorterStemmer
import spellChecking 
import dietActInfoRetrv 

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#preprocess single file
def preprocessing(in_file, out_file):
	fw = open(out_file,'w')
	for line in open(in_file):
		temp_string = ''.join(str(element) for element in line if element not in string.punctuation)
		temp_string = temp_string.lower()
		#tokenization 
		words = wordpunct_tokenize(temp_string)
		new_tokens = []
		for token in words:
			flag = 0 
			token = re.sub(r'[a-zA-Z]*[0-9]+[a-zA-Z]*', r' ', token)
			# token = re.sub(r'[^\w]', r'', token)
			token = token.encode('utf-8')
			#remove stop words, which are meaningless
			for stopword in stopwords.words('english'):
				if token==str(stopword) or token=='one' or token=='go' or token=='take' or token=='three' or \
				token=='two' or token=='four' or token=='kg' or token=='baked' or token=='hawaii' or \
				token=='brueno' or token=='french' or token=='american' or token=='turkish' or \
				token=='chinese' or token=='indische' or token=='cole' or token=='alla':
					flag = 1
					break
			if flag == 0:
				if token != '':
					if token != ' ':
						#lemmatization 
						token = nltk.stem.WordNetLemmatizer().lemmatize(token,'v')
						#spell checking 
						token = spellChecking.correct(token)
						token = token.encode('utf-8')
						if token!='peer' and token!='quark' and token!='flat' and token!='go' and token!='take' and \
						token!='get' and token!='forget' and token!='stuff' and token!='brown' and token!='bad' and \
						token!='child' and token!='bring' and token!='cream' and token!='mm' and token!='sensor' and \
						token!='stuf' and token!='groceries' and token!='back' and token!='home' and token!='behind' and \
						token!='city' and token!='dog' and token!='red' and token!='healthy':
							new_tokens.append(token)
		if new_tokens:
			print >> fw, new_tokens
	fw.close() 

# preprocess all files
def preprocessDiary():
	print 'in preprocessDiary()'
	singlerun = 0 
	if singlerun: 
		subjectID = '039'
		preprocessing('activity/activityFromExcel/activity_'+subjectID+'.txt','activity/activityProcessed/processed_activity_'+subjectID+'.txt')
		preprocessing('diet/dietFromExcel/diet_'+subjectID+'.txt','diet/dietProcessed/processed_diet_'+subjectID+'.txt')
	else:
		for subjectID in available_list:
			print subjectID
			preprocessing('activity/activityFromExcel/activity_'+subjectID+'.txt','activity/activityProcessed/processed_activity_'+subjectID+'.txt')
			preprocessing('diet/dietFromExcel/diet_'+subjectID+'.txt','diet/dietProcessed/processed_diet_'+subjectID+'.txt')

def preprocessDailyDiary():
	print 'in preprocessDailyDiary()'
	for subjectID in available_list:
		print subjectID
		duration = dietActInfoRetrv.getDuration(subjectID)
		for n in range(1,duration+1):
			preprocessing('activity/activityFromExcel/activity_'+subjectID+'_'+str(n)+'.txt','activity/activityProcessed/processed_activity_'+subjectID+'_'+str(n)+'.txt')
			preprocessing('diet/dietFromExcel/diet_'+subjectID+'_'+str(n)+'.txt','diet/dietProcessed/processed_diet_'+subjectID+'_'+str(n)+'.txt')
			
# preprocessDiary()
# preprocessDailyDiary()
