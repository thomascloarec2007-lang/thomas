
from random import randint 

# Déclaration des variables représentant des caractéristiques du joueur pour une utilisation future
pv = 20
épée = 2
stam = 100
insulte = 0



def mort(raison):
    print("Vous etes mort, GAME OVER ")
    tmp = input("affichez la cause de la mort? (oui/non)")
    if tmp != "oui" and tmp!= "non":
        mort(raison)
    else:
        if tmp == "oui":
            print("La cause de votre mort est: "+ raison)
            exit()
        else:
            exit()

# Introduction
def intro (nom):
    print("Bienvenue dans ce jeu !")
    print("Vous pouvez le quittter à tout moment en tapant une réponse non conforme.")


    print("\nVous vous réveillez amnésique et affaibli en dessous d'un grand arbre en ammont d'une colline arride ")
    print("Vous regardez vos effets personnels.")
    inventaire = ["épée", "étrange amullette"]
    print("vous avez sur vous une étrange amullette ansi qu'une épée.")
    print("\nLa nuit va bientôt tomber.")
    partie_1 (nom)
   

# Récupère dans une variable le nom pour une utilisation future
def psuedo (insulte):
    nom = input("Choisissez un speudonyme, il ne doit contenir que des lettres.\nIndiquer votre nom : ")
    nom_correct = False
    while nom_correct == False:
        for i in nom:
            if not i.isalpha():
                insulte = 1
                print("Gros apprend à lire des consignes, sinon ca va pas le faire. ")
                psuedo (insulte)
            else:
                nom_correct = True
            
    if insulte == 1:
        print("Bon toutou!")
    return nom

# Premier choix
def partie_1 (nom):
    print("Vous regardez autour de vous. ")
    print("A l'ouest: une intense source de lumière blanche.")
    print("Vous décidez:")
    print(" 1) De vous réfugier.\n 2) De retrouver d'où vous venez. ")
    reponse_1 = int(input("Que choisissez vous? (sélectionnez le numéro): "))
    if reponse_1 == 1:
        branche1 (nom)
    if reponse_1 == 2:
        branche2()

    


    # Branche 1 -> grotte 
def branche1 (nom): 
    print("\nVous trouvez une grotte sombre à l'abris pour la nuit.")
    print("Vous décidez de : ")
    print(" 1) Vous y réfugier pour la nuit.\n 2) De passer la nuit à l'exterieur malgré la pluie.")
    reponse_1_1 = int(input("Que choisissez-vous? (sélectionnez le numéro) : "))
    if int(reponse_1_1) == 1:
        branche1_1(nom)
    if int(reponse_1_1) == 2:
        raison = "mort de froid"
        mort(raison)

    # Branche 2 -> lumière          
def branche2 ():  
    print("\nVous marcher vers l'intense et ébloissante source lumineuse")
    print("Vous croisez le chemin d'un inconnu")
    print("Ce dernier et disgarcieux, avec une peau grasse et rugueuse, un visage boursoufflé, un nez imposant et large une pilosité hors de contrôle, la moitié de ses dents")
    print("Il inspirait du vice")
    print("Celui-ci vous demande si vous êtes perdu")
    print("Vous lui expliquer votre situation puis vous lui demandez s'il reconnaît le blason sur votre amullette.")
    print("Il vous répond qu'il s'agit du blason de l'intermonde, et vous conseille de vous rendre dans la ville la plus proche situé à l'est, à l'opposé de la source lumineuse.")
    print("\nVous décidez : ")
    print(" 1) De lui faire confiance et de suivre son indication \n 2) De ne pas lui faire confiance et de continuer votre chemin vers l'ouest")
    reponse_1_1 = int(input("Que choisissez-vous? (sélectionnez le numéro) : "))
    if reponse_1_1 == 1:
        branche2_1()
    if reponse_1_1 == 1:
        branche2_2()

# Branche 1-1
def branche1_1(nom):
    print("\nVous entrez dans la grotte")
    print("Après plusieurs minutes de vérifications, vous appercever une faible lueur dans la pénombre")
    print("Vous êtes appeuré et intrigué par cette dernière.")
    print("Une voix mystérieuse vous appelle: 'v..vv...viens par ici "+ str(nom) + "'")
    print (nom)
    partie_2()

    # Branche 2-1
def branche2_1():
    print("\nVous rentrer dans une forêt")
    print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
    print("Il séagissait d'un piège... Il ne faut jamais faire confiance aux personnes moches...")
    print("\nL'homme s'élance ver vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    combat()
    

    # Branche 2-2
def branche2_2():
    print("\nVous partez dans la direction opposée")
    print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
    print("Il séagissait d'un piège... Les moches sont toujours vicieux...")
    print("\nL'homme s'élance ver vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    combat(stam, épée, pv, pv_du_moche)
    
   
   


    #combat 1
    #print("\nL'homme s'élance ver vous, armé d'une dague !!!")
    #print("Vous devez vous battre !!!")
    #pv_du_moche = 10
    #stam = 100
    #pv = 20
    #épée = 2
    #while pv_du_moche >= 0:


def deffense (stam, épee, pv): 
    if stam <= 0:
        print ("\nvous n'avez pas la force d'esquiver...")
        pv -= 5
    
    else:    
        attaque = randint(1,2)
        print("\nAttention, escquivez!!!")
        print("vous esquivez: \n1)vers la droite \n2)vers la gauche")
        reponse_1_1 = int(input("Que choisissez-vous? (sélectionnez le numéro) : "))
        if reponse_1_1 == attaque:
            chance = randint(1, 100)
            
            if chance > 90:
                pv -=  2 
                print("\nBonne esquive !!! Mais vous êtes tout de même touché !!!")
                print("Il vous reste: " + str(pv) + " pv.")
            else:
                print ("\nBien esquivé!!! Vous ne subissez aucun dommage!!!")
        if reponse_1_1 != attaque:
            pv -= 5
            print("\nMauvais coté...Vous subissez d'imortant dommage... ")
            print("Il vous reste: " + str(pv) + " pv.")
        
        elif int(reponse_1_1) != 1 and int(reponse_1_1) != 2:
            print("Choix invalide!")
            exit()
        
    if pv <= 0:
        print("\nVous êtes mort... GAME OVER!!!")
        exit()
    return pv, stam
    
def attaque (stam, pv_du_moche, épée):
    if stam <= 0:
        print("\nA votre tour, choisissez votre attaque, mais vous n'avez plus d'endurance... Vous devez vous reposer")
        stam += 20 
    else:
        print("\nA votre tour, choisissez votre attaque")
        print("1)attaque vive\n2)attaque basique\n3)attaque lourde\n4)se reposer ")
        attaque = int((input("choisissez une action: ")))
        if attaque == "1":
            stam -= 10
            chance = randint (1,100)
            if chance > 90:
                print ("\nvotre attaque échoue...")
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= épée   
            
        if attaque == "2":
            stam -= 20
            chance = randint (1,100)
            if chance > 70:
                print ("\nvotre attaque échoue...")  
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= épée + 3

        if attaque == "3":
            stam -= 30
            chance = randint (1,100)
            if chance > 25:
                print ("\nvotre attaque échoue...") 
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= épée + 6

        if attaque == "4":
            print("\nVous vous reposez et regagnez de l'endurance")
            stam += 30  

        elif int(attaque) != 1 and int(attaque) != 2 and int(attaque) != 3 and int(attaque) != 4:
            print("Choix invalide!")
            exit()  

        return pv, stam, pv_du_moche

def combat(stam, épée, pv, pv_du_moche):    
    while pv_du_moche >= 0:
        deffense(stam, épée, pv)
        attaque (stam, pv_du_moche)
        
        

def fin_combat_1 (nom):
    print("\nFélicitation, vous avez vaincu l'ennemi !!!")
    print("Vous fouillez le corps de l'ennemi...")
    print("Vous récupérez sa dague ainsi que de la nourriture")
    épée += 20
    print("Vous décidez de : ")
    print(" 1) Mangez pour vous restorez.\n 2) Laissez pour le prochain.")   
    reponse_1_1 = int(input("Que choisissez-vous? (sélectionnez le numéro) : "))
    if int(reponse_1_1) == 1:
            pv += 10
            print("\nVous mangez et vous vous restaurez.")
            pv += 10
    if int(reponse_1_1) == 2:
            print("\nVous laissez la nourriture pour le prochain.")
    

def fin_1er_combat ():
    print("\nVous êtes encore completement perdu mais au moins vous êtes en vie...")   
    print("La nuit commence à tomber, vous décidez de chercher un abris pour la nuit...")  
    branche1 ()


      
   
       


def partie_2(): 
    print("\nLa chose semble vous connaître...")
    print("En sait t-elle davantage sur vous et sur ce monde?")
    print("Vous descidez de vous avancer vers le voie...")
    print("Vous harpentez de long corridors humides et sombres...\nSoudain, vous arrivez dans une vaste salle éclairée par des torches.")    
    print("Au centre de cette pièce se tient une silhouette encapuchonnée...")
    print("Elle ne semble pas hostile...\nElle vous fait signe de vous approcher... \nVous vous avancez prudemment...")
    print("\n'Cela fait bien longtemps que je n'ai pas vu un mortel...' dit la créature d'une voix rauque." )
    print("'Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde.'" )

    print("Vous demandez:")
    print(" 1) Pouvez vous me parlez plus de ce qu'est cet intermonde?.\n 2) Mais qui êtes vous au juste? ")
    reponse_1 = int(input("Que choisissez vous? (sélectionnez le numéro): "))
    if int(reponse_1) == 1:
        branche2_1()
    if int(reponse_1) == 2:
        branche2_2()

#brance 2-1

def branche2_1_1():
    print("\n'L'intermonde est un lieu entre les mondes, un carrefour pour les âmes perdues' répond l'Archivister" )
    print("'Certaines personnes y sont envoyées pour expier leurs fautes, d'autres errent ici après la mort, incapables de trouver la paix.'" )
#branche 2-2 
def branche2_1_2 ():
    print("\n'Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde.' répond la créature" )
    print("'Mon rôle est de préserver les connaissances anciennes et d'aider ceux qui cherchent des réponses.'" )
    print("ainsi que de guider les âmes égarées comme la vôtre, à retrouvez la voie de la paix éternelle'" )


#revelation
def branche2_2_1():
    print("\nAvec ces simples mots, vous comprenez que vous êtes mort...")
    print("Mais vous ne vous rappelez toujours pas qui vous étiez de votre vivant...")
    print("Vous hésitez à lui montrer votre amulette..., qui semble avoir une signification particulière ici...")
    print("Vous choisissez:")
    print(" 1) De lui montrer.\n 2) De guarder le secret. ")
    reponse_1 = int(input("Que choisissez vous? (sélectionnez le numéro): "))
    if int(reponse_1) == 1:
        branche2_3_1()
    if int(reponse_1) == 2:
        branche2_3_2()
#suicide 
def branche2_3_2():
    print("\nVous n'avez plus rien à faire ici et descidez de partir" )
    print("Vous quittez la grotte et marchez dans la nuit sombre...")
    print("Tourmentez par cette révélation, vous errez sans but à travers les paysages de l'intermonde...")
    print("Vous vous sentez vide, perdu et désespéré...")
    print("Finalement, vous vous effondrez, submergé par la tristesse et la solitude...")
    print("Vous sortez votre épée et vous vous suicidez...")
    raison = "Vous vous êtes scuicidé de tristessse #BAAAKKKKAAAA"
    mort(raison)

#fin du jeu
def branche2_3_1(): 
    print("\nL'Archiviste regarde l'amulette avec une expression de surprise." )
    print("Seulement, cette expression de surprise se transforme vite en un regard farouche.." )
    print("La chose vous vixe dans les yeux avec un regard noir... Vous vouillez maintenant son visage, qui n'a rien d'humain..." )
    print("'Cette amulette est une relique perdue... ou plustôt volée...' dit la créature" )
    print("'Volé il y a des milier d'années, au prit de la vie de nombreux des miens...Tu payerais pour les crîmes de tes ancêtres!!!!'" )
    print("La créature se jette sur vous, furieuse de votre possession de l'amulette...")
    print("Vous devez vous battre pour votre survie!!!")
    print("\nLe monstre s'élance ver vous!!!")
    
    pv_du_moche = 100
    stam = 100
    combat(stam, épée, pv, pv_du_moche)
    

    print("\nFélicitation, vous avez vaincu l'ennemi !!!")
    print("En mourrant, la créature murmure: 'Peut être qu'un jour tu comprendras le fardeau que tu portes...'")
    print("Vous sentez une étrange paix vous envahir...")
    print("Vous contnuez votre chemin, l'amulette brillant faiblement autour de votre cou...")
    print("Alors vous tombez nez à nez avec une structure qui s'apparante à une porte...")
    print("En vous approchant, vous dicernez des inscriptions anciennes gravées sur le cadre de la porte...")
    print("Vous repérez une encoche en forme de serrure au centre de la porte...")
    print("Vous décidez de : ")
    print("1) Incerez l'amulette.\n 2) Incerez votre sexe.")   
    reponse_1 = int(input("Que choisissez vous? (sélectionnez le numéro): "))
    
    if int(reponse_1) == 1:
        print("\nVous insérez l'amulette dans l'encoche...")
        print("Un éclat de lumière aveuglante emplit la pièce...")
        print("Lorsque la lumière se dissipe, vous vous retrouvez dans un endroit familier...")
        print("Vous êtes de retour dans le monde des vivants, avec des souvenirs retrouvés et une nouvelle appréciation pour la vie.")
        print("Félicitations, vous avez trouvé la paix et la rédemption!")
        print("FIN DU JEU !!!")
        print("Ecrit et réalisé par Thomas et Adam.")
        exit()
    
    if int(reponse_1) == 2:
        print("\nVous insérez votre sexe dans l'encoche...")
        print("Vous sentez une douleur intense...")
        print("Puis une lumière aveuglante emplit la pièce...")
        raison = ("Votre se")
        exit()

        
def jeu (): 
    nom = psuedo (insulte)
    intro (nom)
    
    

jeu()

















































































































































































































































# tu fais quoi ici mdrrrr


            
            
        
    
