# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:58:11 2019

@author: Bryan
"""
#Define some basic percentages and values for Texas Hold em

#Define Lists for both the cards and suits
suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9" , "10", "Jack", "Queen", "King", "Ace"]
deck = []
#fun fact: because python uses lists instead of arrays, these are dynamic. You can add or remove values to the list
#thats why we declared this empty deck[] list

#len() gets the length of an object 
#print() prints out the value to the console
print(len(cards)) 
print(len(suits))
print(len(cards)*len(suits))

#store this values for later use
card_count = 13
suit_count = 4
deck_count = card_count * suit_count
#also define some more counted variables while we're at it
pocket_count = 2
flop_count = 3
turn_count = 4
river_count = 5

#function to create a list with all cards in deck
def createDeckList():
    for w in suits:
        for x in cards:
           deck.append(x + " of " + w) 

# call the createDeckList() function          
createDeckList()

#printing empty line to clear up some space on the console log
print()

def every_card_in_deck():
    for card in deck:
        print(card)

#call the every_card_in_deck() function        
every_card_in_deck()
print()
#if we tried to run..
# print("a full deck has " + len(deck) + " cards")
#..we would get this error:
# "TypeError: can only concatenate str (not "int") to str"
#because the length of the deck is an integer. not a string of text characters. Hence we must convert it to a string

print("a full deck has " + str(len(deck)) + " cards")
print()

#print an equivalency test to compare deck[] size and deck_count
print("Is it true that deck[] size equals deck_count?")
print(len(deck) == deck_count)

#Next up..           
#attempt a crazy loop to iterate through the possible number of different shuffle deck possibilities
