#Partie 1

print("PARTIE 1")

myTable=[3, 8, 7, 2, 6]
#1-

print("PREMIER EXERCICE")


print("Mon tableau de base est : ", myTable)

myTable.pop() #retire le dernier element du tableau
myTable.insert(2, 6) #(index, valeur)

print("Mon nouveau tableau est : ", myTable)

#2-
print("/////////////")
print("DEUXIEME EXERCICE")







#3-
print("/////////////")
print("Troisième exercice")


for i in range (0,len(myTable)): 
    indexPPValeur=i 
    pPValeur=myTable[i]
    for index in range(i,len(myTable)):
        if (myTable[index]< pPValeur):
            pPValeur=myTable[index]
            indexPPValeur=index

    myTable.pop(indexPPValeur) #(retire l'element choisi)
    myTable.insert(i,pPValeur) #(index, valeur)

print("Mon tableau trié est : ", myTable)

#c'est plutot un tri a insertion je crois :/


#4-
#Le tri  à bulles est tres lent car il doit comparer chaque elements du tableau aux autre elements(du meme tableau )
#Je pense que plus le tableau est grand plus le tri prend de temps 
