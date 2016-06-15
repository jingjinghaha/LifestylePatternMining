# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:38:43 2016

@author: wu34
"""

from scipy.stats import ttest_ind
import sleepAnalysis

#dd_low,dd_high,dd_diff = sleepAnalysis.supportDict()

a = [0.71,0.62,0.55,0.55,0.54,0.51,0.5,0.48,0.48,0.48,0.48,0.46,0.45,0.45,0.45,0.44,0.43,0.38,0.32]
b = [0.93,0.85,0.5,0.5,0.5,0.5,0.5,0.5,0.49,0.5,0.5,0.49,0.5,0.5,0.5,0.49,0.49,0.23,0.12]
c = [0.51,0.51,0.58,0.58,0.5,0.55,0.51,0.52,0.49,0.49,0.55,0.51,0.6,0.6,0.57,0.52,0.51,0.57,0.59]

#b = []
#for i in dd_low.keys():
##    a.append(dd_low[i][0])
#    b.append(dd_low[i][1])
##    c.append(dd_low[i][2])
#a = [0.84,0.73]
#b = [0.84,0.76]
#c = [0.84,0.74]

t_stat1, p_val1 = ttest_ind(a, b)
t_stat2, p_val2 = ttest_ind(a, c)
t_stat3, p_val3 = ttest_ind(b, c)

#d = [0.29,0.38,0.45,0.45,0.46,0.49,0.5,0.52,0.52,0.52,0.52,0.54,0.55,0.55,0.55,0.56,0.57,0.62,0.68]
#e = [0.07,0.15,0.5,0.5,0.5,0.5,0.5,0.5,0.51,0.5,0.5,0.51,0.5,0.5,0.5,0.51,0.51,0.77,0.88]
#f = [0.49,0.49,0.42,0.42,0.5,0.45,0.49,0.48,0.51,0.51,0.45,0.49,0.4,0.4,0.43,0.48,0.49,0.43,0.41]
#
##e = []
##for i in dd_high.keys():
###    d.append(dd_high[i][0])
##    e.append(dd_high[i][1])
###    f.append(dd_high[i][2])
#
#
#t_stat4, p_val4 = ttest_ind(d, e)
#t_stat5, p_val5 = ttest_ind(d, f)
#t_stat6, p_val6 = ttest_ind(e, f)



