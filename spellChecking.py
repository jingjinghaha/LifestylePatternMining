# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:24:53 2015

@author: wu34
"""

import re, collections
import enchant
from nltk import wordpunct_tokenize
import string

def words(text):
	return re.findall('[a-z]+', text.lower())

def train(features):
	model = collections.defaultdict(lambda: 1)
	for f in features:
		model[f] += 1
	return model

NWORDS = train(words(file('big.txt').read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
	s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	deletes	 = [a + b[1:] for a, b in s if b]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
	replaces	 = [a + c + b[1:] for a, b in s for c in alphabet if b]
	inserts	 = [a + c + b	  for a, b in s for c in alphabet]
	return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(wordss):
	return set(w for w in wordss if w in NWORDS)

def correct_temp(word):
	# print word
	candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
	# print max(candidates, key=NWORDS.get)
	return max(candidates, key=NWORDS.get)

def correct(word):
	#diet word
	if word == 'patatoe' or word=='potatoe' or word=='patato' or word=='patatoes' or word=='potatoes' or word=='patatoeegg':
		word = 'potato'
	if word == 'twix' or word == 'bonbonbloc' or word == 'chocopeanuts' or word == 'chocolade' or word == 'chocolat' or word=='chocoalde':
		word = 'chocolate'
	if word == 'crackers' or word == 'nutcracker' or word == 'sultana' or word == 'cracker' or word == 'stultana' or word == 'honeyloops' or word == 'coockie' or word == 'kruidnoten' or word=='coockies':
		word = 'cookie'
	if word == 'tosti' or word=='sanwich' or word=='sandwcihes' or word=='sandwcihe' or word=='sadnwich' or word=='sandwitch' or word=='sandwiche' or word=='lasagne' or word=='cheesesandwichsperad' or word=='sandwichspread':
		word = 'sandwich'
	if word == 'couscous' or word == 'risotto' or word == 'rissoto' or word == 'nasi' or word=='prices' or word=='sushi':
		word = 'rice'
	if word == 'spaghetti' or word == 'fooyonghai' or word == 'carbonara' or word == 'spaghette' or word == 'canneloni' or word == 'bolognese':
		word = 'pasta'
	if word == 'yoghurtdrink' or word == 'yoghert' or word =='vanilleyoghurt' or word=='yohurt' or word=='yoghury' or word=='yoghurtdrink':
		word = 'yoghurt'
	if word == 'tomatosoup' or word=='spinachsoup':
		word = 'soup'
	if word == 'salaede' or word=='salad7up':
		word = 'salad'
	if word == 'chocolademousse' or word == 'chocomel' or word=='chocopops' or word=='chocomouse':
		word = 'choco'
	if word == 'carpacio' or word == 'carpaccio' or word=='cappucino' or word=='cappuccino':
		word = 'cappuccino'
	if word == 'cofee':
		word = 'coffee'
	if word == 'champginon':
		word = 'champignon'
	if word == 'cumcumber':
		word = 'cucumber'
	if word == 'vegetables' or word == 'vegetarian' or word == 'vegies' or word =='vegetrable' or word=='vegetables80g':
		word = 'vegetable'
	if word == 'tandori' or word=='pastabroccolichicken':
		word = 'chicken'
	if word == 'noodle' or word == 'noedleswoksauce' or word == 'noudles' or word == 'noedles' or word=='noedleswoksauce' or word == 'bami' or word=='nodules':
		word = 'noodles'
	if word == 'schrimp':
		word = 'shrimp'
	if word == 'zuchini':
		word = 'zucchini'
	if word == 'gingerbread' or word == 'croissant' or word == 'toast' or word == 'nonnevot' or word == 'waldkorn' or word=='sugarbread' or word=='cinnastix':
		word = 'bread'
	if word == 'canneloni':
		word = 'cannelloni'
	if word == 'aplle':
		word = 'apple'
	if word == 'aspargus':
		word = 'asparagus'
	if word == 'crusli' or word=='cruesli' or word=='cruslie':
		word = 'muesli'
	if word == 'musli' or word=='muslie' or word=='cheesecruesli':
		word = 'muesli'
	if word == 'gnochhi':
		word = 'gnocchi'
	if word == 'juce' or word=='jus':
		word = 'juice'
	if word == 'carrots' or word == 'carrotstamp' or word=='carot':
		word = 'carrot'
	if word == 'pizzam' or word=='moussaka' or word=='flammkuchen':
		word = 'pizza'
	if word == 'omelet' or word == 'wggs':
		word = 'egg'
	if word == 'snacken' or word=='tapas':
		word = 'snack'
	if word == 'pancakes' or word == 'pancake' or word == 'cale' or word == 'cubcake' or word=='milefeuille':
		word = 'cake'
	if word == 'prosecco' or word=='gluhwine' or word=='gluh':
		word = 'wine'
	if word == 'cokenuts':
		word = 'coconut'
	if word == 'cheesepeanut' or word == 'goatcheese' or word =='camembert' or word=='olivesfeta' or word=='chinees':
		word = 'cheese'
	if word == 'kaletuna':
		word = 'tuna'
	if word == 'crocquette' or word == 'croquette' or word == 'antipasto' or word == 'meatball' or word == 'gourmetten' or word == 'zuurvlees' or word == 'goatcheesebacon' or word == 'crocquette' or word == 'ragou' or word == 'filet' or word == 'bitterballs' or word == 'frikandel' or word=='carne' or word=='antipasta':
		word = 'meat'
	if word == 'stew' or word == 'bf' or word =='steak':
		word = 'beef'
	if word == 'fruitbars' or word=='fruitbf':
		word = 'fruit'
	if word == 'peanutbutter' or word == 'herbbutter':
		word = 'butter'
	if word == 'tangerine' or word == 'dorange':
		word = 'orange'
	if word == 'ranja':
		word = 'water'
	if word == 'glass' or word == 'redbull' or word=='fanta' or word=='glas':
		word = 'drink'
	if word == 'pannacotta':
		word = 'pudding'
	if word == 'nutmilk' or word == 'chocolademilk':
		word = 'milk'
	if word == 'coke' or word == 'rucola':
		word = 'cola'
	if word == 'peanut' or word == 'peanuts' or word == 'cashewnuts' or word == 'peanutpesto':
		word = 'nut'
	if word == 'chorizo':
		word = 'sausage'
	if word == 'wrap' or word == 'burritowrap':
		word = 'doner'
	if word == 'zuchini':
		word = 'oatmeal'
	if word == 'proteinshake':
		word = 'protein'
	if word == 'dessert' or word == 'sprinkle' or word == 'honey':
		word = 'sugar'
	if word == 'hamburgers' or word == 'ham':
		word = 'hamburger'
	if word == 'ice':
		word = 'iceCream'
	if word == 'fry':
		word = 'fries'
	#activity word
	if word == 'coocking' or word == 'cooking':
		word = 'cook'
	if word == 'relaxen':
		word = 'relax'
	if word == 'uni':
		word = 'university'
	if word == 'pc':
		word = 'computer'
	if word == 'lessons':
		word = 'lesson'
	if word == 'computertv':
		word = 'computer'
	if word == 'phonecall':
		word = 'phone'
	if word == 'cars':
		word = 'car'
	if word == 'bicycle':
		word = 'bike'
	if word == 'course':
		word = 'lesson'
	if word == 'activities':
		word = 'activity'
	if word == 'recharge':
		word = 'charge'
	if word == 'watchting':
		word = 'watch'
	if word == 'swimmingpool':
		word = 'swim'
	return word 

#usage: 
#a = correct('speling')
#print 'Did you mean ' + a +'?'

def check_spelling_single_diet_file(subjectID):
	f_with_precheck = open('SC_diet'+subjectID+'_with_precheck.txt','w')
	# f_no_precheck = open('temp_no_precheck.txt','w')
	for line in open('diet_'+subjectID+'.txt','r'):
		temp_string = ''.join(str(element) for element in line if element not in string.punctuation)
		temp_string = temp_string.lower()
		#tokenization 
		tokens = wordpunct_tokenize(temp_string)
		for word in tokens:
			# # correct(word)
			# ## use pyenchant 
			d = enchant.Dict("en_US")
			# print word 
			# print d.check(word)
			if not d.check(word):
				word_after_check = correct_temp(word)
				f_with_precheck.write("%-10s%-10s"%(word,word_after_check))
				f_with_precheck.write('\n')
			# ## use popular method
			# word_after_check = correct_temp(word)
			# f_no_precheck.write("%-10s%-10s"%(word,word_after_check))
			# f_no_precheck.write('\n')
	f_with_precheck.close()
	# f_no_precheck.close()

def check_spelling_single_activity_file(subjectID):
	f_with_precheck = open('SC_activity'+subjectID+'_with_precheck.txt','w')
	# f_no_precheck = open('temp_no_precheck.txt','w')
	for line in open('activity_'+subjectID+'.txt','r'):
		temp_string = ''.join(str(element) for element in line if element not in string.punctuation)
		temp_string = temp_string.lower()
		#tokenization 
		tokens = wordpunct_tokenize(temp_string)
		for word in tokens:
			# # correct(word)
			# ## use pyenchant 
			d = enchant.Dict("en_US")
			# print word 
			# print d.check(word)
			if not d.check(word):
				word_after_check = correct_temp(word)
				f_with_precheck.write("%-10s%-10s"%(word,word_after_check))
				f_with_precheck.write('\n')
			# ## use popular method
			# word_after_check = correct_temp(word)
			# f_no_precheck.write("%-10s%-10s"%(word,word_after_check))
			# f_no_precheck.write('\n')
	f_with_precheck.close()
	# f_no_precheck.close()

# available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
# for subjectID in available_list:
	# check_spelling_single_diet_file(subjectID)
	# check_spelling_single_activity_file(subjectID)



