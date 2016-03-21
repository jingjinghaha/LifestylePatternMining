# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 16:10:15 2015

@author: wu34
"""

'''
the 3rd version, sperate snacks into sweet food and nuts; and add eggP 
'''
#fruit products: 
Type1 = ['jam','raisin','currants','fruit','orange','apple','banana','kiwi','sultana','pineapple','smoothie','juice']
#dairy products:
Type2 = ['shake','milk','cheese','yoghurt']
#grain products:
Type3 = ['noodles','oatmeal','muesli','bread','macaroni''rice',]
#meat products:
Type4 = ['beef','bacon','meat','sausage','chicken','steak']
#sweet
Type5 = ['choco','pie','candy','iceCream','chocolate','cake','snack','cookie','sugar','waffle','pudding','kellogs'] 
#vegetables products: 
Type6 = ['salad','sauerkraut','cucumber','spinach','carrot','pumpkin','broccoli','tomato','vegetable','zucchini','bean']
#caffeine drink: 
Type7 = ['cola','tea','coffee','cappuccino']
#alcohol drink: 
Type8 = ['beer','wine','alcohol']
#Seafood
Type9 = ['fish','tuna','salmon','tilapia']
#Composite dishes
Type10 = ['doner','sandwich','pizza','soup','pasta','lasagna','hamburger']
#Potato products:
Type11 = ['potato','chip','fries']
#Nuts:
Type12 = ['nut']
#Egg:
Type13 = ['egg']

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
        diet_type = 'sweetF'
    if word in Type6:
        diet_type = 'vegetables'
    if word in Type7:
        diet_type = 'caffeineD'
    if word in Type8:
        diet_type = 'alcoholD'
    if word in Type9:
        diet_type = 'seafood'
    if word in Type10:
        diet_type = 'compositeP'
    if word in Type11:
        diet_type = 'starchyP'
    if word in Type12:
        diet_type = 'nutP'
    if word in Type13:
        diet_type = 'eggP'
    return diet_type 


'''
the foloowing types separation is the second version 
'''
# #fruit products: 
# Type1 = ['jam','raisin','currants','fruit','orange','apple','banana','kiwi','sultana','pineapple','smoothie','juice']
# #dairy products:
# Type2 = ['shake','milk','cheese','yoghurt']
# #grain products:
# Type3 = ['noodles','oatmeal','muesli','bread','macaroni''rice',]
# #meat products:
# Type4 = ['beef','bacon','meat','sausage','chicken','steak']
# #snacks
# Type5 = ['nut','choco','pie','candy','iceCream','chocolate','cake','snack','cookie','sugar','waffle','pudding','kellogs'] 
# #vegetables products: 
# Type6 = ['salad','sauerkraut','cucumber','spinach','carrot','pumpkin','broccoli','tomato','vegetable','zucchini','bean']
# #caffeine drink: 
# Type7 = ['cola','tea','coffee','cappuccino']
# #alcohol drink: 
# Type8 = ['beer','wine','alcohol']
# #Seafood
# Type9 = ['fish','tuna','salmon','tilapia']
# #Composite dishes
# Type10 = ['egg','doner','sandwich','pizza','soup','pasta','lasagna','hamburger']
# #Starchy products:
# Type11 = ['potato','chip','fries']
