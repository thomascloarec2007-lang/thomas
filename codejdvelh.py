import random
import os
# Déclaration des variables représentant des caractéristiques du joueur pour une utilisation future
pv = 20
pm = 0
from random import randit 

# Introduction
print("Vous vous réveillez amnésique et affaibli en dessous d'un grand arbre en ammont d'une colline arride ")
print("Vous regardez vos effets personnels")
print("Inventaire: épée, étrange amullette")
inventaire = ["épée", "étrange", "amullette"]

# Récupère dans une variable le nom pour une utilisation future
nom = input("Indiquer votre nom : ")

# Premier choix
print("La nuit va bientôt tomber.")
print(" Vous regardez autour de vous. ")
print("A l'ouest: une intense source de lumière blanche.")
print("Vous décidez:")
print(" 1) De vous réfugier\n 2) De retrouver d'où vous venez\n ")
reponse_1 = input("Que choisissez vous? (sélectionnez le numéro) ")

# Branche 1
if int(reponse_1) == 1:
    print("Vous trouvez une grotte sombre à l'abris pour la nuit")
    print("Vous décidez de : ")
    print(" 1) Vous y réfugier pour la nuit\n 2) De passer la nuit à l'exterieur malgré la pluie")
    reponse_1_1 = input("Que choisissez-vous? (sélectionnez le numéro) : ")

    # Branche 1-1
    if int(reponse_1_1) == 1:
        print("Vous entrez dans la grotte")
        print("Après plusieurs minutes de vérifications, vous appercever une faible lueur dans la pénombre")
        print("Vous êtes légeremment appeuré et intrigué par cette dernière.")
        print("Une voix mystérieuse vous appelle: 'v..vv...viens par ici "+ str(nom) + "'")
   
    # Branche 1-2
    if int(reponse_1_1) == 2:
        print("Vous restez dehors sous la pluie.")
        print("Après plusieurs minutes vous vous endormez.")
        print("Vous voyez une lumière au fond du tunnel... GAME OVER!!!")
        print("Vous vous êtes fait tuer par un animal sauvage pendant votre sommeil")
           

            
if int(reponse_1) == 2:
    print("Vous marcher vers l'intense et ébloissante source lumineuse")
    print("Vous croisez le chemin d'un inconnu")
    print("Ce dernier et disgarcieux, avec une peau grasse et rugueuse, un visage boursoufflé, un nez imposant et large une pilosité hors de contrôle, la moitié de ses dents")
    print("Il inspirait du vice")
    print("Vous décidez de : ")
    print("Celui-ci vous demande si vous êtes perdu")
    print("Vous lui expliquer votre situation puis vous lui demandez s'il reconnaît le blason sur votre amullette.")
    print("Il vous répond qu'il s'agit du blason de l'intermonde, et vous conseille de vous rendre dans la ville la plus proche situé à l'est, à l'opposé de la source lumineuse.")
    print(" 1) De lui faire confiance et de suivre son indication \n 2) De ne pas lui faire confiance et de continuer votre chemin vers l'ouest")
    reponse_1_1 = input("Que choisissez-vous? (sélectionnez le numéro) : ")

    # Branche 2-1
    if int(reponse_1_1) == 1:
        print("Vous rentrer dans une forêt")
        print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
        print("Il séagissait d'un piège... Il ne faut jamais faire confiance aux personnes moches...")
        


    # Branche 2-2
    if int(reponse_1_1) == 2:
        print("Vous partez dans la direction opposée")
        print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
        print("Il séagissait d'un piège... Les moches sont toujours vicieux...")
        print("L'homme s'élance ver vous, armé d'une dague !!!")
        print("Vous décidez de: ")
        print("1)Se diriger vers la voie \n 2)")
        reponse_1_1_2 = input("Que choisissez-vous ? (sélectionnez le numéro) : ")

    print("L'homme s'élance ver vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    stam = 100
    while pv > 0 or pv_du_moche > 0:
        #defense:
        if stam <= 0:
            print ("vous n'avez pas la force d'esquiver...")
            pv -= 5
        else:
            
            attaque = randit(1,2)
            print("vous esquivez: 1)vers la droite 2)vers la gauche")
            reponse_1_1 = input("Que choisissez-vous? (sélectionnez le numéro) : ")
            if reponse_1_1 == attaque:
                chance = randit(1, 100)
                if chance > 90:
                    pv -= 2 
                    print(" Bonne esquive !!! Mais vous êtes tout de même touché !!!")
                else:
                    print ("Bien joué !!")
            if reponse_1_1 != attaque:
                pv -= 5
                print(" Mauvais coté...Vous subissez d'imortant dommage... ")
    
        #attaque
        if stam <= 0:
            print("vous êtes à cours d'endurance..")
            stam += 20 
        else:
            print("A votre tour, choisissez votre attque")
            print("1)attaque vive, 2)attaque basique, 3)attaque lourde, 4)se reposer ")
            attaque = intput("choisissez une action")
            if attaque == 1:
                stam -= 10
                chance = randit (1,100)
                if chance > 90:
                    print ("votre attaque échoue...")
                else:
                    print("Bravo vous infligez des dégâts!!! ")
                    pv_du_moche -= 2
                
            if attaque == 2:
                stam -= 20
                chance = randit (1,100)
                if chance > 80:
                    print ("votre attaque échoue...") 
                else:
                    print("Bravo vous infligez des dégâts!!! ")
                    pv_du_moche -= 5
            if attaque == 3:
                stam -= 30
                chance = randit (1,100)
                if chance > 25:
                    print ("votre attaque échoue...") 
                else:
                    print("Bravo vous infligez des dégâts!!! ")
                    pv_du_moche -= 8
            else:
                stam += 20
                print("Vous vous sentez remplit d'énergie !")

            
            
            
        
    

