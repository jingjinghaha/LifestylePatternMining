# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:18:54 2016

@author: jingjing
"""

import dataGen4SlpPrd 
import utilise 
import numpy as np
import pandas as pd 

label = dataGen4SlpPrd.getSlpTimeLabel()

labels = dataGen4SlpPrd.genActTypeLabel()
labels.append('Label')
dataset = dataGen4SlpPrd.genDailyActTypeFeatureTable4DC()
dataset_l1 = np.c_[dataset,label.ravel()]

df = pd.DataFrame(dataset_l1,columns=labels)

print df['Label']
