# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

#transportation1:
Type1 = ['walk']
#transportation2
Type2 = ['ov','car','bus','train','taxi','drive']
#transportaion3
Type3 = ['bike','cycle']
#work/study related
Type4 = ['craftwork','traineeship','exam','homework','read','work','lesson','sit','university','lecture','school','study','workout']
#entertainment:
Type5 = ['dog','shop','travel','watch','game','play','computer','tv','movie']
#social related
Type6 = ['activity','meet','friends','call','party','talk','phone']
#sport related
Type7 = ['run','sport','gym','hockey','swim','fitness','soccer']
#diet related
Type8 = ['food','drink','cheese','dish','eat','diner','breakfast','lunch','bread','cook']
#rest related
Type9 = ['rest','sleep','relax','bed']
#others
Type10 = ['wait','home','household','pack','shower','charge','recharge','clean','dress','toilet']

def actType(word):
    act_type = 'none'
    if word in Type1:
        act_type = 'transportation1'
    if word in Type2:
        act_type = 'transportation2'
    if word in Type3:
        act_type = 'transportation3'
    if word in Type4:
        act_type = 'work_study'
    if word in Type5:
        act_type = 'entertainment'
    if word in Type6:
        act_type = 'social'
    if word in Type7:
        act_type = 'sport'
    if word in Type8:
        act_type = 'diet'
    if word in Type9:
        act_type = 'rest'
    if word in Type10:
        act_type = 'others'
    return act_type 


