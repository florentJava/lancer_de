import random


class Joueur:
    def __init__(self, prenom):
        self.prenom = prenom
        self.turn = None

    def lancer_de(self):
        return random.randrange(1,6)


class Jeux:
    def __init__(self,nbr_tour=2):
        self.player_list = []
        self.nbr_tour = nbr_tour

    def add_player(self, p):
        self.player_list.append(p)


    def display_players(self) -> list:
        return  self.player_list



def create_player(list):
    player_name = input("Enter the player name   : ")
    list.append(Joueur(player_name))



if __name__ == '__main__':

    game = Jeux()
    bool = True
    i = 1
    joueur = 0;
    liste_score = [];

    print(" ========== -- WELCOME TO OUR GAME -- ============================\n")
    play = True
    while play:

        for index in range(2):
            create_player(game.display_players())


        print("-------------------------- ORDRE DE JEUX ------------------------------------")
        [print("   ",(game.display_players().index(x)+1),"-", x.prenom) for x in game.display_players() ]



        print("-------------------------- DEBUT DU JEUX ------------------------------------")

        while bool :

            print("Tour Numero :",i)

            for player in  game.display_players():

                input("\t-"+player.prenom+" Lancer Le De :")

                liste_score.append(player.lancer_de())
                print("=",liste_score[(game.display_players().index(player))])

                i =+ 1


