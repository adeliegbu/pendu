"""
objectifs : réaliser le TP3, réaliser un jeu du pendu.
date : 3 oct 2024
par : Adélie GIBOU
codé en python
programme des fonctions

reste à finir l'affichage (fct transforme_trait_en_mot) et faire tout tkinter
"""
import random

with open('dico.txt','r') as file:
    lignes = file.readlines()
    mot = random.choice(lignes)
    mot = mot.rstrip()
        
tentatives = 8
liste_lettres_trouvees = []

def proposition_correcte(proposition):
    return (len(proposition) == 1 and proposition.isalpha() and proposition not in liste_lettres_trouvees)

def reste_des_vies():
    return (tentatives > 0)

def lettre_dans_mot(proposition):
    global tentatives
    if proposition in mot:
        print ("La lettre", proposition, "est dans le mot")
        liste_lettres_trouvees.append(proposition)
        return True
    else:
        tentatives -= 1
        print ("La lettre", proposition, "n'est pas dans le mot")
        return False
    

def mot_trouve():
    return (all(caractere in liste_lettres_trouvees for caractere in mot))

def fin_du_jeu():
    return (not reste_des_vies() or mot_trouve())

def gagne():
    return (fin_du_jeu() and mot_trouve())



        

def pendu():
    while not fin_du_jeu():
        proposition = str (input("Saisissez une lettre à tester : "))
        while not proposition_correcte(proposition):
            proposition = str (input("Saisissez une nouvelle lettre à tester : "))
        proposition = proposition.lower()
        lettre_dans_mot(proposition)
    if gagne():
        print ("Bravo, vous avez trouvé le mot !")
    else :
        print ("Dommage, vous avez perdu. Le mot à deviner était", mot)   
   
def affichage_traits():
    affiche_mot = []
    for i in range(len(mot)):
        affiche_mot.append ("_")
    return affiche_mot


def transforme_trait_en_lettre(proposition):
    if lettre_dans_mot():
        


print (mot)
# print (pendu())
print (affichage())



# "j","o","u","r","n","a","l"