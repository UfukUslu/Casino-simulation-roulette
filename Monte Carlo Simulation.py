#Libraries used
import statistics
import pandas as pd
import matplotlib.pyplot as plt
from random import *

#two input for the simulation
money=1000
bet_min=1 #this is the minimal bet

my_number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
money_in_wallet_list=[]
nb_win=0
nb_game_played=0
bet=bet_min

nb_sim =10000

nb_bankruptcy=0
z=30000 #nb of games to start with (the highest one )
proba_list=[]

while z>10000: #lower limit to reach (to not wait too much before the computer finish its calcualtion
    nb_bankruptcy=0
    for i in range(nb_sim):
        money_in_wallet_list=[]
        money=1000
        bet=bet_min
        for x in range(z):
            number=randint(0,36)
            money_in_wallet_list.append(money)
            if money > 0:
                money=money-bet
                if number in my_number:
                     money = money + bet*2
                     bet=bet_min
                     nb_win = nb_win+1
                     nb_game_played = nb_game_played+1
                else:
                    bet = bet*2
                    nb_game_played=nb_game_played+1
                    if bet>money:
                        bet=bet_min
        if min(money_in_wallet_list)==0:
            nb_bankruptcy=nb_bankruptcy+1
    proba=nb_bankruptcy/nb_sim
    print(z,":  ",proba)
    proba_list.append(proba)
    z=z-100   #diminish z which is the nb of games at each loop "while"


percentage_game_won=nb_win/nb_game_played

print("Percentage of game won : ",percentage_game_won)
print()
