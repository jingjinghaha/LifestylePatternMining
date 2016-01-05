# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 16:26:06 2015

@author: wu34
"""

import buildTypeIndex
import xlwt
import utilise

def dietTypeSimilarityDict(dist = 'TFIDF'):
	dietSimilarity_dict = {} 
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	if dist == 'TFIDF':
		dietSimilarity_dict = utilise.TFIDF('dietType')
	else: 
		i = 0
		for subjectID in available_list:
			j = 0
			similarity = 0
			dietSimilarity_dict[i] = {}
			ItemIndex = buildTypeIndex.build_single_diet_index(subjectID)
			for subjectid in available_list:
				temp_ItemIndex = buildTypeIndex.build_single_diet_index(subjectid)
				if dist == 'numberOfSameWord':
					similarity = utilise.numberOfSameWord(ItemIndex,temp_ItemIndex)
				elif dist == 'jaccard':
					similarity = utilise.jaccard(ItemIndex,temp_ItemIndex)
				elif dist == 'novelJaccard':
					similarity = utilise.novelJaccard(ItemIndex,temp_ItemIndex)
				dietSimilarity_dict[i][j] = similarity
				j += 1
			i += 1
	# print dietSimilarity_dict
	return dietSimilarity_dict


def excelTable(dist = 'TFIDF'):
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	workbook = xlwt.Workbook()
	ws = workbook.add_sheet('sheet1')
	row_index = 0
	for i in range(1,len(available_list)+1):
		ws.write(0,i,available_list[i-1])
	dietSimilarity_dict = dietTypeSimilarityDict(dist)
	for subjectID in available_list:
		row_index += 1
		col_index = 0
		ws.write(row_index,0,subjectID)
		for subjectid in available_list:
			col_index += 1
			ws.write(row_index,col_index,dietSimilarity_dict[row_index-1][col_index-1])
	workbook.save('SimilarityTableExcel/dietTypeSimilarityTable_'+dist+'.xls')

def dietTypeSimilarityTable(dist = 'TFIDF'):
	print 'in dietTypeSimilarityTable()'
	excelTable(dist)


# data visualization (table) for the diet type similarity between two users 
# dietTypeSimilarityTable()


