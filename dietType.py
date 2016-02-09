# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

#fruit products: 
Type1 = ['jam','raisin','currants','fruit','orange','apple','banana','kiwi','sultana','pineapple','smoothie','juice']
#dairy products:
Type2 = ['shake','milk','cheese','yoghurt']
#grain products:
Type3 = ['noodles','oatmeal','muesli','bread','macaroni']
#meat products:
Type4 = ['beef','bacon','meat','sausage','chicken','steak']
#confections
Type5 = ['choco','pie','candy','iceCream','chocolate','cake','snack','cookie','sugar','waffle','pudding','kellogs'] 
#vegetables products: 
Type6 = ['salad','sauerkraut','cucumber','spinach','carrot','pumpkin','broccoli','tomato','vegetable','zucchini','bean']
#caffeine drink: 
Type7 = ['cola','tea','coffee','cappuccino']
#alcohol drink: 
Type8 = ['beer','wine','alcohol']
#Seafood
Type9 = ['fish','tuna','salmon','tilapia']
#egg products:
Type10 = ['egg']
#animal fats:
Type11 = ['butter']
#nuts:
Type12 = ['nut']
#Composite dishes
Type13 = ['doner','sandwich','pizza','soup','snack','rice','pasta','lasagna','hamburger']
#Starchy products:
Type14 = ['potato','chip','fries']

def dietType(word):
    diet_type = 'others'
    if word in Type1:
        diet_type = 'fruitP'
    if word in Type2:
        diet_type = 'dairyP'
    if word in Type3:
        diet_type = 'grainP'
    if word in Type4:
        diet_type = 'meatP'
    if word in Type5:
        diet_type = 'confections'
    if word in Type6:
        diet_type = 'vegetables'
    if word in Type7:
        diet_type = 'caffeineD'
    if word in Type8:
        diet_type = 'alcoholD'
    if word in Type9:
        diet_type = 'seafood'
    if word in Type10:
        diet_type = 'eggP'
    if word in Type11:
        diet_type = 'animalFat'
    if word in Type12:
        diet_type = 'nuts'
    if word in Type13:
        diet_type = 'compositeP'
    if word in Type14:
        diet_type = 'starchyP'
    return diet_type 


