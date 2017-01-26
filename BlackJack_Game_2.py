import m_classes
import random
nums = 'AKQJT98765432'
pict = 'DHCS'
m = m_classes.All_cards(nums,pict)
all_cards = m.making()
random.shuffle(all_cards)
def player_game():
    player_score = 0
    while True:
        player_card = input("Would you like to take a card? Y or N?\n")
        if player_card == "Y" or player_card == "y":
            card = all_cards.pop()
            c = m_classes.Count_points(card)
            print(c)
            player_points = c.points()
            player_score += player_points
            print("PLAYER points are: %d"%player_points)
            print("PLAYER score is: %d" %player_score)
            if player_score < 21:
                continue
            else:
                break  
        elif player_card == "N" or player_card == "n":
            break
    return player_score
def comp_game():
    computer_score = 0
    while True:
        card = all_cards.pop()
        c = m_classes.Count_points(card)
        computer_points = c.points()
        computer_score += computer_points
        if computer_score < 18:
            continue
        else:
            break
    return computer_score
print(str.center("",50,"-"))
print(str.center("BLACKJACK GAME",50,"*"))
print(str.center("",50,"-"))
while True:
    i = input("PLAY GAME\n Y or N?\n")
    if i == "Y" or i == "y":
        p = player_game()
        c = comp_game()
        if p > c and p <= 21 or p <= 21 and c > 21:
            print("PLAYER SCORE: {}".format(p))
            print("COMPUTER SCORE: {}".format(c))
            print("PLAYER WIN")
        elif p == c and p <= 21:
            print("PLAYER SCORE: {}".format(p))
            print("COMPUTER SCORE: {}".format(c))
            print("Dead heat!")
        elif c > p and c <= 21 or c <= 21 and p > 21:
            print("PLAYER SCORE: {}".format(p))
            print("COMPUTER SCORE: {}".format(c))
            print("COMPUTER WIN")
        else:
            print("PLAYER SCORE: {}".format(p))
            print("COMPUTER SCORE: {}".format(c))
            print("PLAYER LOSE\nCOMPUTER LOSE")
    elif i == "N" or i == "n":
        exit()
    else:
        i = input("PLAY GAME\n Y or N?\n")