# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

#fruit
Type1 = ['fruit','orange','apple','banana','kiwi','sultana','pineapple']
#dairy:
Type2 = ['butter','milk','cheese','yoghurt']
#grain:
Type3 = ['sandwich','pizza','noodles','fries','chip','rice','nut','oatmeal','muesli','bread','macaroni','kellogs','pasta','lasagna']
#meat:
Type4 = ['doner','beef','bacon','meat','sausage','chicken','steak','hamburger']
#confections
Type5 = ['jam','raisin','pie','candy','iceCream','chocolate','cake','snack','cookie','sugar','waffle','pudding'] 
#vegetables
Type6 = ['salad','sauerkraut','cucumber','spinach','carrot','pumpkin','broccoli','tomato','vegetable','zucchini','bean','potato']
#drink
Type7 = ['soup','drink','water','juice']
#caffeine drink
Type8 = ['cola','tea','coffee','cappuccino','choco']
#alcohol
Type9 = ['beer','wine','alcohol']
#fish
Type10 = ['fish','tuna','salmon','tilapia']
#other animal products
Type11 = ['egg']

def dietType(word):
    diet_type = 'others'
    if word in Type1:
        diet_type = 'fruit'
    if word in Type2:
        diet_type = 'dairy'
    if word in Type3:
        diet_type = 'grain'
    if word in Type4:
        diet_type = 'meat'
    if word in Type5:
        diet_type = 'confections'
    if word in Type6:
        diet_type = 'vegetables'
    if word in Type7:
        diet_type = 'drink'
    if word in Type8:
        diet_type = 'caffeine'
    if word in Type9:
        diet_type = 'alcohol'
    if word in Type10:
        diet_type = 'fish'
    if word in Type11:
        diet_type = 'otherAnimalProducts'
    return diet_type 


