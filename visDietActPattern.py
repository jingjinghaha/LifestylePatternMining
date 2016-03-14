# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 16:25:53 2016

@author: wu34
"""

import plotDietActItemFreq
import plotOverallDietActItemFreq
import plotDietActTypeFreq
import plotOverallDietActTypeFreq

# data visualization (pie chart) for diet/activity pattern
def visDietActPattern():
	# data visualization (pie chart) for diet/activity Item pattern of each people 
	# the parameter is to set the minimal Item frequency 
	plotDietActItemFreq.plotDietActItemFreq(3)
	# data visualization (pie chart) for overall diet/activity Item pattern
	# the parameter is to set the minimal Item frequency 
	plotOverallDietActItemFreq.plotOverallDietActItemFreq(10)
	# data visualization (pie chart) for diet/activity type pattern of each people 
	plotDietActTypeFreq.plotDietActTypeFreq()
	# data visualization (pie chart) for overall diet/activity type pattern 
	plotOverallDietActTypeFreq.plotOverallDietActTypeFreq()
	
# visDietActPattern()
