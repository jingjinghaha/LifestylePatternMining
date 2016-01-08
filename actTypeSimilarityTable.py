# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 16:26:06 2015

@author: wu34
"""

import buildTypeIndex
import xlwt
import utilise

# def actTypeSimilarityDict(dist = 'TFIDFCosin'):
	# actSimilarity_dict = {} 
	# available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	# if dist == 'TFIDFCosin':
		# actSimilarity_dict = utilise.TFIDFCosin('actType')
	# else: 
		# i = 0
		# for subjectID in available_list:
			# similarity = 0
			# actSimilarity_dict[i] = {}
			# ItemIndex = buildTypeIndex.build_single_activity_index(subjectID)
			# j = 0
			# for subjectid in available_list:
				# temp_ItemIndex = buildTypeIndex.build_single_activity_index(subjectid)
				# if dist == 'numberOfSameWord':
					# similarity = utilise.numberOfSameWord(ItemIndex,temp_ItemIndex)
				# elif dist == 'jaccard':
					# similarity = utilise.jaccard(ItemIndex,temp_ItemIndex)
				# elif dist == 'novelJaccard':
					# similarity = utilise.novelJaccard(ItemIndex,temp_ItemIndex)
				# actSimilarity_dict[i][j] = similarity
				# j += 1
			# i += 1
	## print actSimilarity_dict
	# return actSimilarity_dict


def excelTable(domain,dist = 'TFIDFCosin'):
	available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']
	workbook = xlwt.Workbook()
	ws = workbook.add_sheet('sheet1')
	row_index = 0
	for i in range(1,len(available_list)+1):
		ws.write(0,i,available_list[i-1])
	actSimilarity_dict = utilise.SimilarityDict(domain,dist)
	for subjectID in available_list:
		row_index += 1
		col_index = 0
		ws.write(row_index,0,subjectID)
		for subjectid in available_list:
			col_index += 1
			ws.write(row_index,col_index,actSimilarity_dict[row_index-1][col_index-1])
	workbook.save('SimilarityTableExcel/actTypeSimilarityTable_'+dist+'.xls')

def actTypeSimilarityTable(dist = 'TFIDFCosin'):
	print 'in actTypeSimilarityTable()'
	excelTable('ActType',dist)


# data visualization (table) for the activity type similarity between two users 
# actTypeSimilarityTable()


