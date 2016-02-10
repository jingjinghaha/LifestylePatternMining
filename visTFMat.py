# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:19:56 2016

@author: wu34
"""

import utilise
import matplotlib.pyplot as plt
import numpy as np

def visTFMatrix():
	# tf_ActItem = utilise.normArray(utilise.genActItemTFArray())
	tf_ActItem = utilise.genActItemTFArray()
	plt.figure()
	plt.matshow(tf_ActItem)
	plt.colorbar()
	plt.title('actTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFMatrix')
	
	# tf_DietItem = utilise.normArray(utilise.genDietItemTFArray())
	tf_DietItem = utilise.genDietItemTFArray()
	plt.figure()
	plt.matshow(tf_DietItem)
	plt.colorbar()
	plt.title('dietTFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTFMatrix')
	
	tf = utilise.genCombiArray(tf_ActItem,tf_DietItem)
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('actDietTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTFMatrix')
	
	# tf_DietType = utilise.normArray(utilise.genDietTypeTFArray())
	tf_DietType = utilise.genDietTypeTFArray()
	plt.figure()
	plt.matshow(tf_DietType)
	plt.colorbar()
	plt.title('dietTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFMatrix')
	
	# tf_ActType = utilise.normArray(utilise.genActTypeTFArray())
	tf_ActType = utilise.genActTypeTFArray()
	plt.figure()
	plt.matshow(tf_ActType)
	plt.colorbar()
	plt.title('actTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTypeTFMatrix')
	
	tf = utilise.genCombiArray(tf_ActType,tf_DietType)
	plt.figure()
	plt.matshow(tf)
	plt.colorbar()
	plt.title('actDietTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actDietTypeTFMatrix')

visTFMatrix()