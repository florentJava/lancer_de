import random


class Joueur:
    def __init__(self, prenom):
        self.prenom = prenom
        self.turn = None

    def lander_de(self):
        return random.random(6) + 1


class Jeux:
    def __init__(self):
        self.player_list = {}
    def add_player(self, p):
        self.player_list[f'player{len(self.player_list)}'] = p


    def display_players(self) -> list:
        return [self.player_list[player_id].prenom for player_id in self.player_list]



def create_player():
    player_name = input("Enter the player name   : ")
    return Joueur(player_name)


if __name__ == '__main__':

    game = Jeux()

    print(" ========== -- WELCOME TO OUR GAME -- ============================\n")
    play = True
    while play:

        for index in range(2):
             game.add_player(create_player())


        print(game.display_players())






