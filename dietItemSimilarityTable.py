# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 16:26:06 2015

@author: wu34
"""

import buildItemIndex
import xlwt
import utilise

def excelTable(domain,sim = 'TFIDFCosin'):
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	workbook = xlwt.Workbook()
	ws = workbook.add_sheet('sheet1')
	row_index = 0
	for i in range(1,len(available_list)+1):
		ws.write(0,i,available_list[i-1])
	dietSimilarity_dict = utilise.SimilarityDict(domain,sim)
	for subjectID in available_list:
		row_index += 1
		col_index = 0
		ws.write(row_index,0,subjectID)
		for subjectid in available_list:
			col_index += 1
			ws.write(row_index,col_index,dietSimilarity_dict[row_index-1][col_index-1])
	workbook.save('SimilarityTableExcel/dietItemSimilarityTable_'+sim+'.xls')

def dietItemSimilarityTable(sim):
	# print 'in dietItemSimilarityTable()'
	excelTable('DietItem',sim)


# data visualization (table) for the diet Item similarity between two users 
# dietItemSimilarityTable(sim = 'jaccard')


