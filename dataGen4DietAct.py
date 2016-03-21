# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:13:17 2016

@author: jingjing
"""

import xlrd
import dietActInfoRetrv
import numpy as np
import utilise 

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
sleep_list = ['044','045','048','050','051','052','053','056','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']


def genDietTypeTFArrayWithSlp():
    TF = utilise.genDietTypeTFArray()
    
    x = len(sleep_list)
    n = TF.shape[1]
    array = np.zeros((x,n))
    
    cunt = 0
    for i in range(len(available_list)):
        if available_list[i] in sleep_list:
            array[cunt] = TF[i]
            cunt += 1 
    
    return array 
    

def genActTypeTFArrayWithSlp():
    TF = utilise.genActTypeTFArray()
    
    x = len(sleep_list)
    n = TF.shape[1]
    array = np.zeros((x,n))
    
    cunt = 0
    for i in range(len(available_list)):
        if available_list[i] in sleep_list:
            array[cunt] = TF[i]
            cunt += 1 
    
    return array 


