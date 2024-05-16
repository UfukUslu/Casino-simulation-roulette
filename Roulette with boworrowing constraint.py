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

nb_game = int(input('Number of games : '))

for x in range(nb_game):
    number=randint(0,36)
    money_in_wallet_list.append(money)
    if money > 0:
        money=money-bet
        if number in my_number:
             money = money + bet*2
             bet=bet_min
             nb_win = nb_win+1
             nb_game_played=nb_game_played+1
        else:
            bet = bet*2
            nb_game_played = nb_game_played + 1
            if bet>money:
                bet=bet_min
    else:
        break


percentage_game_won=nb_win/nb_game_played

print(money_in_wallet_list)
print()
print()
print("Percentage of game won : ",percentage_game_won)
print()
print('Lowest amount in the available funds: ',min(money_in_wallet_list))
print('Highest amount in the available:' , max(money_in_wallet_list))

plt.plot(money_in_wallet_list)
plt.ylabel('Available funds')
plt.xlabel('Number of games')
plt.suptitle('Simulation of Classical Martingale')
plt.title("Access to LIMITED financial resources",fontstyle="italic" )
plt.show()
