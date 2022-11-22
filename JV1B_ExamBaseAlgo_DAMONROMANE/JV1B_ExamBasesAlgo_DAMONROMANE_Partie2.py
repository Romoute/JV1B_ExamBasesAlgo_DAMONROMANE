#Partie 2

print("PARTIE 2") 
#1
print("PREMIER EXERCICE")

grilles= ("_|_|_\n_|_|_\n | | ")

print(grilles)


#2
print("/////////////")
print("DEUXIEME EXERCICE")


while (grilles == "x" or grilles =="o"):
    print("quelle case voulez vous jouer ? ")



#3
print("/////////////")
print("TROISIEME EXERCICE")



for i in range(3):
        for j in range(3):
            if(grilles[3*i + j] == "x"):
                print("X", fin=" ")
            elif(grilles[3*i + j] == "o"):
                print("O", fin=" ")
            else:
                print(" ", fin=" ")



#4
'''
print("/////////////")
print("QUATRIEME EXERCICE")



while (turn != 9 and victory == False):
    
'''

#5
print("/////////////")
print("CINQUIEME EXERCICE")



grilles= ("_|_|_\n_|_|_\n | | ")
turn = 0
victory = False



while (turn != 9 and victory == False):


    play = int(input("Quelle case voulez-vous jouer ?"))
    while(grilles[play] == "o" or grilles[play] == "x"):
         play = int(input("Cette case  est déjà prise, choisissez en une autre ?"))


    if(turn%2 == 0):
        grilles[play] = "o"
    else:
        grilles[play] = "x"

    for i in range(3):
        for j in range(3):
            if(grilles[3*i + j] == "x"):
                print("X", end=" ")
            elif(grilles[3*i + j] == "o"):
                print("O", end=" ")
            else:
                print(" ", end=" ")
        print("")




    turn += 1








#6
#Pour faire un puissance 4 il faudraitaugmenter la taille de la grille, augmenter a 4 les lignes pour qu'un joueur gagne 
# et faire en sorte que quand un joueur choisit une colonne le "pion" aille en bas ou au dessus du dernier pion joué  

