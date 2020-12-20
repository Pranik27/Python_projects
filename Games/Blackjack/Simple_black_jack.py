# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:29:26 2020

@author: PRANIKP
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...


"""

import random

card_suits = ['Hearts','Diamonds','Club','Spade']
card_value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Cards():
    ## Card class to create each cards need in a deck
    
    def __init__(self,suit,card_num):
        self.suit = suit
        self.card_num = card_num
        self.value = card_value.get(card_num)
        
        
    def __str__(self):
        return ("{} of {}".format(self.card_num,self.suit))
    
    
class Deck():
    ## Deck class to create the card deck and shuffle 
    
    def __init__(self):
        
        self.all_cards = []
        
        for curr_suit in card_suits:
            for card in card_value:
                self.all_cards.append(Cards(curr_suit,card))
                
                
    def __len__(self):
        return (len(self.all_cards))
    
    def shuffle_deck(self):
        return(random.shuffle(self.all_cards))
                
    def deal(self):
        single_card = self.all_cards.pop()
        return(single_card)
        
        
class ChipsTrack():
    
    def __init__(self,chips):
        self.chips = chips
        
        
    def chips_won(self,num):
        self.chips+= num
        
    def chips_lost(self,num):
        self.chips -= num
        
    def bet(self,num):
        self.chips -= num
        

def valildate_bet(bet_amount):
    pass


        
print("Welcome to BLACK JACK GAME!!\n")


player_name = input("Please enter your name: \n")

while True:
    try:
        player_chips = int(input("please enter the chips amount you have: \n"))
    except:
        print("Please enter a numeric Value||\n")
    else:
        print("Thanks!! have a pleasant game..\n")
        break
    

print("{}, please place your bet".format(player_name))

new_deck = Deck()
new_deck.shuffle_deck()

player1_hand = []
dealer_hand = []


for num in range(2):
    player1_hand.append(new_deck.deal())
    dealer_hand.append(new_deck.deal())

    
print(*player1_hand,sep = ',')
print(*dealer_hand,sep= ',')








