# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:29:13 2016

@author: wu34
"""

import utilise
import matplotlib.pyplot as plt

def visTFIDFMatrix():
	# tfidf = utilise.normArray(utilise.ActItemTfidfArray())
	tfidf1 = utilise.ActItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf1)
	plt.colorbar()
	plt.title('actTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFIDFMatrix')
	
	# tfidf = utilise.normArray(utilise.DietItemTfidfArray())
	tfidf2 = utilise.DietItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf2)
	plt.colorbar()
	plt.title('dietTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTFIDFMatrix')
	
	tfidf = utilise.genCombiArray(tfidf1,tfidf2)
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actDietTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTFIDFMatrix')
	
	# tfidf = utilise.normArray(utilise.DietTypeTfidfArray())
	tfidf2 = utilise.DietTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf2)
	plt.colorbar()
	plt.title('dietTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFIDFMatrix')
	
	# tfidf = utilise.normArray(utilise.ActTypeTfidfArray())
	tfidf1 = utilise.ActTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf1)
	plt.colorbar()
	plt.title('actTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTypeTFIDFMatrix')
	
	tfidf = utilise.genCombiArray(tfidf1,tfidf2)
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actDietTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTypeTFIDFMatrix')

visTFIDFMatrix()
