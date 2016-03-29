# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 15:19:56 2016

@author: wu34
"""

import utilise
import dataGen4DietAct
import matplotlib.pyplot as plt
import numpy as np

def visTFMatrix():
	tf_ActItem = utilise.normArray(dataGen4DietAct.genActItemTFArray())
	# tf_ActItem = dataGen4DietAct.genActItemTFArray()
	plt.figure()
	plt.matshow(tf_ActItem)
	plt.colorbar()
	plt.title('actTFMatrix')
	plt.savefig('visTForTFIDFMatrix/actTFMatrix')
	
	tf_DietItem = utilise.normArray(dataGen4DietAct.genDietItemTFArray())
	# tf_DietItem = dataGen4DietAct.genDietItemTFArray()
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
	
	tf_DietType = utilise.normArray(dataGen4DietAct.genDietTypeTFArray())
	# tf_DietType = dataGen4DietAct.genDietTypeTFArray()
	plt.figure()
	plt.matshow(tf_DietType)
	plt.colorbar()
	plt.title('dietTypeTFMatrix')
	plt.savefig('visTForTFIDFMatrix/dietTypeTFMatrix')
	
	tf_ActType = utilise.normArray(dataGen4DietAct.genActTypeTFArray())
	# tf_ActType = dataGen4DietAct.genActTypeTFArray()
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
