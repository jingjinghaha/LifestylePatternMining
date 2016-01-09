# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:29:13 2016

@author: wu34
"""

import utilise
import matplotlib.pyplot as plt

def visTFIDFMatrix():
	tfidf = utilise.ActItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFIDFMatrix')
	
	tfidf = utilise.DietItemTfidfArray()
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('dietTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTFIDFMatrix')
	
	tfidf = utilise.DietTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('dietTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFIDFMatrix')
	
	tfidf = utilise.ActTypeTfidfArray()
	plt.figure()
	plt.matshow(tfidf)
	plt.colorbar()
	plt.title('actTypeTFIDFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTypeTFIDFMatrix')

visTFIDFMatrix()
