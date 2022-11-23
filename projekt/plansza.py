
def plansza():
    plansza = [" --- ", "| a |"]
    pola = ""
    for i in range(3):
        for index in plansza:
            pola += 3 * index + "\n"
        if i == 2:
            plansza = (pola + " ---  ---  ---")

    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    board = ""
    for litera in range(len(plansza)):
        if plansza[litera] == "a":
            board += str(liczby.pop(0))
        else:
            board += plansza[litera]

    return board


