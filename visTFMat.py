# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:19:56 2016

@author: wu34
"""

import utilise
import matplotlib.pyplot as plt

def visTFMatrix():
	tf = utilise.genActItemTFArray()
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('actTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFMatrix')
	
	tf = utilise.genDietItemTFArray()
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('dietTFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTFMatrix')
	
	tf = utilise.genDietTypeTFArray()
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('dietTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFMatrix')
	
	tf = utilise.genActTypeTFArray()
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('actTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTypeTFMatrix')

visTFMatrix()