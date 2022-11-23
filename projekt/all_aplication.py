from plansza import plansza
from Player import Player
from zasady import is_win

players = [
    Player(input("Wprowadz nazwe dla gracza: ")),
    Player(input("Wprowadz nazwe dla gracza: "))
]

#Zaczyna losowy gracz:
import random
# first_person = random.choice([0, 1])
# queue = [players[first_person], players[(first_person+1) % 2]]

choice_first_person = random.choice(range(len(players)))
first_person = players.pop(choice_first_person)
choice_second_person = random.choice(range(len(players)))
second_person = players.pop(choice_second_person)

#Kto zaczyna i wybor figury
queue = [first_person, second_person]
print(str(first_person) + " starts the game! Choose your figure and let's do your turn")
second_person.figure = first_person.choose_figure()

#Plansza:
board = plansza()
print(board)

#Przebieg rozgrywki:
ilosc_ruchow = 0
while ilosc_ruchow < 9:
    current_player = queue[ilosc_ruchow % 2]
    ilosc_ruchow += 1

    turn = int(input("Twoja tura: " + str(current_player.nick) + " Wprowadz wartosc pola, ktore zaznaczasz: "))
    current_player.turns.append(turn)
    board = board.replace(str(turn), current_player.figure)

    print(board)

#Wygrany:
    if is_win(current_player.turns):    #is_win() == True
        print("Gratulacje graczu: " + current_player.nick + " wygrałes !!!")
        break
    #
    # if ilosc_ruchow % 2 == 0:
    #     turn = int(input("Twoja tura: " + str(first_person.nick) + " Wprowadz wartosc pola, ktore zaznaczasz: "))
    #     first_person.turns.append(turn)
    #     board = board.replace(str(turn), first_person.figure)
    #     if is_win(first_person.turns):    #is_win() == True
    #         print("Gratulacje graczu: " + first_person.nick + " wygrałes !!!")
    #         break
    #
    # else:
    #     turn = int(input("Twoja tura: " + str(second_person.nick) + " Wprowadz wartosc pola, ktore zaznaczasz: "))
    #     second_person.turns.append(turn)
    #     board = board.replace(str(turn), second_person.figure)
    #     if is_win(second_person.turns):    #is_win() == True
    #         print("Gratulacje graczu: " + second_person.nick + " wygrałes !!!")
    #         break



