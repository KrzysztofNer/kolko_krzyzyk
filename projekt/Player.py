class Player:
    def __init__(self, nick, figure=""):
        self.nick = nick
        self.figure = figure
        self.turns = []

    def choose_figure(self):
        """
        Returns figure's second player
         """
        figures = ["o", "x"]
        sign = input("Wybierz figure: (x) lub (o): ")
        while sign != "o" and sign != "x": # while sing not in ['o', 'x']
            sign = input("Wybrales zly znak, wybierz jeszcze raz: (x) lub (o)")

        self.figure = figures.pop(figures.index(sign))
        return figures[0]

    def __str__(self):
        """
        f"{obiekt1}_{obiekt}" ==> output: obiekt1_obiekt2
        str(obiekt1) + "_" + str(obiket2) ====> output: obiekt1_obiekt2
         """
        return f"{self.nick} {self.figure}"

