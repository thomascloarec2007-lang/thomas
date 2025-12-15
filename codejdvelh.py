
from random import randint 

# Déclaration des variables représentant des caractéristiques du joueur pour une utilisation future
pv = 20
épée = 2
stam = 100
inventaire = ["amullette"]

info_joueur = {"pv":pv, "épée": épée, "stam": stam, "inventaire":inventaire}


def reponse (diff_choix):
    valeur_accepter = ['exit', "restart"]
    for i in range (len(diff_choix)):
        tmp = i + 1
        print (str(tmp) + ")" + diff_choix[i])
        valeur_accepter.append(str(tmp))

    rep_user = input("Entrez votre choix: ")
    if rep_user == "exit":
        print("Aurevoir!")
        exit()
    elif rep_user ==  "restart":
        pv = 20
        épée = 2
        stam = 100
        inventaire = ["amullette"]
        info_joueur = {"pv":pv, "épée": épée, "stam": stam, "inventaire":inventaire}
        jeu(info_joueur)
        exit()
    elif rep_user not in valeur_accepter:
        print("Veuillez choisir une repponse correcte ou entrer 'exit' pour quitter le programme.")
        return reponse(diff_choix)
    else:
        print("Vous choississez "+ str(diff_choix[int(rep_user)-1])+".")
        return rep_user

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


# Récupère dans une variable le nom pour une utilisation future
def pseudo (insulte, info_joueur):

    nom = input("Choisissez un speudonyme, il ne doit contenir que des lettres.\nIndiquer votre nom : ")
    cara = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNéàèûù"
    for i in nom:
        if i not in cara:
            insulte = True
            print("Gros apprend à lire des consignes, sinon ca va pas le faire. ")
            pseudo (insulte, info_joueur)
     
                      
    if insulte == True:
        print("Bon toutou!")
        
    info_joueur["nom"] = nom
    return info_joueur

# Introduction
def intro (info_joueur):
    print("Bienvenue dans ce jeu !")
    print("Vous pouvez le quittter à tout moment en tapant 'exit'.")


    print("\nVous vous réveillez amnésique et affaibli en dessous d'un grand arbre en ammont d'une colline arride ")
    print("Vous regardez vos effets personnels.")
    print("vous avez sur vous une étrange amullette ansi qu'une épée.")
    print("\nLa nuit va bientôt tomber.")
    partie_1 (info_joueur)

# Premier choix
def partie_1 (info_joueur):
    print("Vous regardez autour de vous. ")
    print("A l'ouest: une intense source de lumière blanche.")
    print("Vous décidez:")
    diff_choix = ["de vous réfugier", "de retrouver d'où vous venez"]
   
    reponse_1 = reponse (diff_choix)
    if reponse_1 == "1":
        branche1 (info_joueur)
    if reponse_1 == "2":
        pont(info_joueur)



    # Branche 1 -> grotte 
def branche1 (info_joueur): 
    print("\nVous trouvez une grotte sombre à l'abris pour la nuit.")
    print("Vous décidez de: ")
    diff_choix = ["Vous y réfugier pour la nuit", "De passer la nuit à l'exterieur malgré la pluie"]
    reponse_1_1 = reponse (diff_choix)
    if reponse_1_1 == "1":
        branche1_1(info_joueur)
    if reponse_1_1 == "2":
        raison = "mort de froid"
        mort(raison)

def pont (info_joueur):
    print("Vous vous retrouvé bloqué par une rivière. Il vous faut la traverser.")
    print("Vous pouvez: ")
    diff_choix = []


    branche2 (info_joueur)



    # Branche 2 -> lumière          
def branche2 (info_joueur):  
    print("\nVous marcher vers l'intense et ébloissante source lumineuse")
    print("Vous croisez le chemin d'un inconnu")
    print("Ce dernier et disgarcieux, avec une peau grasse et rugueuse, un visage boursoufflé, un nez imposant et large une pilosité hors de contrôle, la moitié de ses dents")
    print("Il inspirait du vice")
    print("Celui-ci vous demande si vous êtes perdu")
    print("Vous lui expliquer votre situation puis vous lui demandez s'il reconnaît le blason sur votre amullette.")
    print("Il vous répond qu'il s'agit du blason de l'intermonde, et vous conseille de vous rendre dans la ville la plus proche situé à l'est, à l'opposé de la source lumineuse.")
    print("\nVous décidez : ")
    diff_choix = ["De lui faire confiance et de suivre son indication", "De ne pas lui faire confiance et de continuer votre chemin vers l'ouest"]
    reponse_1_1 = reponse (diff_choix)
    if reponse_1_1 == "1":
        branche2_1(info_joueur)
    if reponse_1_1 == "2":
        branche2_2(info_joueur)
   


# Branche 1-1
def branche1_1(info_joueur):
    print("\nVous entrez dans la grotte")
    print("Après plusieurs minutes de vérifications, vous appercever une faible lueur dans la pénombre")
    print("Vous êtes appeuré et intrigué par cette dernière.")
    print("Une voix mystérieuse vous appelle: 'v..vv...viens par ici "+ str(info_joueur["nom"]) + "'")
    
    partie_2(info_joueur)

    # Branche 2-1
def branche2_1(info_joueur):
    print("\nVous rentrer dans une forêt")
    print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
    print("Il séagissait d'un piège... Il ne faut jamais faire confiance aux personnes moches...")
    print("\nL'homme s'élance ver vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    raison = "Le sale moche vous a tué..."
    num_combat = 1
    combat(info_joueur, pv_du_moche, raison, num_combat)
    

    # Branche 2-2
def branche2_2(info_joueur):
    print("\nVous partez dans la direction opposée")
    print("Vous recroisez l'étrangé à un tournant, qui vous regarde d'un air menaçant...")
    print("Il séagissait d'un piège... Les moches sont toujours vicieux...")
    print("\nL'homme s'élance ver vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    raison = "Le sale moche vous a tué..."
    num_combat = 1
   
    combat(info_joueur, pv_du_moche, raison, num_combat)
    


def deffense (info_joueur, raison ): 
    if info_joueur["stam"] <= 0:
        print ("\nvous n'avez pas la force d'esquiver...")
        info_joueur["pv"] -= 5
    
    else:    
        attaque = randint(1,2) #coté du quel vient l'ennemi
        print("\nAttention, escquivez!!!")
        diff_choix = ["vers la droite ", "vers la gauche"]
        reponse_1_1 = reponse(diff_choix)
        if int(reponse_1_1) == attaque:
            chance = randint(1, 100) #taux de réussite de l'attaque
            
            if chance > 90:  
                info_joueur["pv"] -=  2 
                print("\nBonne esquive !!! Mais vous êtes tout de même touché !!!")
                print("Il vous reste: " + str(info_joueur["pv"]) + " pv.")
            else:
                print ("\nBien esquivé!!! Vous ne subissez aucun dommage!!!")
        if int(reponse_1_1) != attaque:
            info_joueur["pv"] -= 5
            print("\nMauvais coté...Vous subissez d'imortant dommage... ")
            print("Il vous reste: " + str(info_joueur["pv"]) + " pv.")


    if info_joueur["pv"] <= 0:
        mort(raison)
    return info_joueur
    
def attaque (info_joueur, pv_du_moche):
    if info_joueur["stam"] <= 0:
        print("\nA votre tour, choisissez votre attaque, mais vous n'avez plus d'endurance... Vous devez vous reposer")
        info_joueur["stam"] += 20 
    else:
        print("\nA votre tour, choisissez votre attaque")
        diff_choix =  ["attaque vive", "attaque basique", "attaque lourde", "se reposer" ]
        attaque = reponse(diff_choix)
        if attaque == "1":
            info_joueur["stam"] -= 8
            chance = randint (1,100) #taux de réussite de l'attaque
            if chance > 90:
                print ("\nvotre attaque échoue...")
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= info_joueur["épée"]
            
        if attaque == "2":
            info_joueur["stam"] -= 15
            chance = randint (1,100)
            if chance > 80:
                print ("\nvotre attaque échoue...")  
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= info_joueur["épée"] + 3

        if attaque == "3":
            info_joueur["stam"] -= 20
            chance = randint (1,100)
            if chance > 70:
                print ("\nvotre attaque échoue...") 
            else:
                print("\nBravo vous infligez des dégâts!!! ")
                pv_du_moche -= info_joueur["épée"] + 6

        if attaque == "4":
            print("\nVous vous reposez et regagnez de l'endurance")
            info_joueur["stam"] += 30 
            if info_joueur["stam"] > 200:
                info_joueur["stam"] = 200
                

        if pv_du_moche > 0:
            print ("Il lui reste: "+ str(pv_du_moche)+ "pv")
        else:
            print("Votre énemie sembre mal en point... Il titube puis s'effondre!")

        if info_joueur["stam"] < 15:
            print("Vous vous sentez fatigué...")

        return info_joueur, pv_du_moche
        
def combat(info_joueur, pv_du_moche, raison, num_combat):  
    
    while pv_du_moche > 0:
        deffense(info_joueur, raison)
        pv_du_moche_tmp = attaque (info_joueur, pv_du_moche)
        pv_du_moche = pv_du_moche_tmp[1]
    if num_combat == 1:
        fin_combat_1 (info_joueur)
    if num_combat== 2:
        fin_combat_2 ()


        
        

def fin_combat_1 (info_joueur):
    print("\nFélicitation, vous avez vaincu l'ennemi !!!")
    print("Vous fouillez le corps de l'ennemi...")
    print("Vous récupérez sa dague ainsi que de la nourriture")
    info_joueur["épée"] += 20
    print("Vous décidez de : ")

    diff_choix = ["mangez pour vous restorez","laissez pour le prochain" ]
    reponse_1_1 = reponse(diff_choix)
    if reponse_1_1 == "1":
            info_joueur["pv"] += 20
            print("\nVous mangez et vous vous restaurez.")
    if reponse_1_1 == "2":
            print("\nVous laissez la nourriture pour le prochain.")
  
    print("\nVous êtes encore completement perdu mais au moins vous êtes en vie...")   
    print("La nuit commence à tomber, vous décidez de chercher un abris pour la nuit...")  
    
    branche1 (info_joueur)


      
   
       


def partie_2(info_joueur): 
    print("\nLa chose semble vous connaître...")
    print("En sait t-elle davantage sur vous et sur ce monde?")
    print("Vous descidez de vous avancer vers le voie...")
    print("Vous harpentez de long corridors humides et sombres...\nSoudain, vous arrivez dans une vaste salle éclairée par des torches.")    
    print("Au centre de cette pièce se tient une silhouette encapuchonnée...")
    print("Elle ne semble pas hostile...\nElle vous fait signe de vous approcher... \nVous vous avancez prudemment...")
    print("\n'Cela fait bien longtemps que je n'ai pas vu un mortel...' dit la créature d'une voix rauque." )
    print("'Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde.'" )
    print("Vous demandez:")

    diff_choix = ["pouvez vous me parlez plus de ce qu'est cet intermonde?", "Mais qui êtes vous au juste?"]
    reponse_1 = reponse(diff_choix)
    if reponse_1 == "1":
        branche2_1_1(info_joueur)
    if reponse_1 == "2":
        branche2_1_2(info_joueur)
   

#brance 2-1

def branche2_1_1(info_joueur):
    print("\n'L'intermonde est un lieu entre les mondes, un carrefour pour les âmes perdues' répond l'Archivister" )
    print("'Certaines personnes y sont envoyées pour expier leurs fautes, d'autres errent ici après la mort, incapables de trouver la paix.'" )
    branche2_2_1(info_joueur)

#branche 2-2 
def branche2_1_2 (info_joueur):
    print("\n'Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde.' répond la créature" )
    print("'Mon rôle est de préserver les connaissances anciennes et d'aider ceux qui cherchent des réponses.'" )
    print("ainsi que de guider les âmes égarées comme la vôtre, à retrouvez la voie de la paix éternelle'" )
    branche2_2_1(info_joueur)

#revelation
def branche2_2_1(info_joueur):
    print("\nAvec ces simples mots, vous comprenez que vous êtes mort...")
    print("Mais vous ne vous rappelez toujours pas qui vous étiez de votre vivant...")
    print("Vous hésitez à lui montrer votre amulette..., qui semble avoir une signification particulière ici...")
    print("Vous choisissez:")

    diff_choix =  ["de lui montrer", "de guarder le secret"]
    reponse_1 = reponse(diff_choix)
    if reponse_1 == "1":
        branche2_3_1(info_joueur)
    if reponse_1 == "2":
        branche2_3_2(info_joueur)
  
#suicide 
def branche2_3_2(info_joueur):
    print("\nVous n'avez plus rien à faire ici et descidez de partir" )
    print("Vous quittez la grotte et marchez dans la nuit sombre...")
    print("Tourmentez par cette révélation, vous errez sans but à travers les paysages de l'intermonde...")
    print("Vous vous sentez vide, perdu et désespéré...")
    print("Finalement, vous vous effondrez, submergé par la tristesse et la solitude...")
    print("Vous sortez votre épée et vous vous suicidez...")
    raison = "Vous vous êtes scuicidé de tristessse #BAAAKKKKAAAA"
    mort(raison)

#fin du jeu
def branche2_3_1(info_joueur): 
    print("\nL'Archiviste regarde l'amulette avec une expression de surprise." )
    print("Seulement, cette expression de surprise se transforme vite en un regard farouche.." )
    print("La chose vous vixe dans les yeux avec un regard noir... Vous vouillez maintenant son visage, qui n'a rien d'humain..." )
    print("'Cette amulette est une relique perdue... ou plustôt volée...' dit la créature" )
    print("'Volé il y a des milier d'années, au prit de la vie de nombreux des miens...Tu payerais pour les crîmes de tes ancêtres!!!!'" )
    print("La créature se jette sur vous, furieuse de votre possession de l'amulette...")
    print("Vous devez vous battre pour votre survie!!!")
    print("\nLe monstre s'élance ver vous!!!")
    num_combat = 2
    pv_du_moche = 100
    raison = "Le monstre vous a tué... Il semble bien trop fort, ou bien VOUS êtes bien trop faible."

    combat(info_joueur,pv_du_moche, raison, num_combat)
    
def fin_combat_2():
    print("\nFélicitation, vous avez vaincu l'ennemi !!!")
    print("En mourrant, la créature murmure: 'Peut être qu'un jour tu comprendras le fardeau que tu portes...'")
    print("Vous sentez une étrange paix vous envahir...")
    print("Vous contnuez votre chemin, l'amulette brillant faiblement autour de votre cou...")
    print("Alors vous tombez nez à nez avec une structure qui s'apparante à une porte...")
    print("En vous approchant, vous dicernez des inscriptions anciennes gravées sur le cadre de la porte...")
    print("Vous repérez une encoche en forme de serrure au centre de la porte...")
    print("Vous décidez de : ")

    diff_choix = ["incerez l'amulette", "incerez votre 'avant bras'."]
    reponse_1 = reponse(diff_choix)
    
    if reponse_1 == "1":

        print("\nVous insérez l'amulette dans l'encoche...")
        print("Un éclat de lumière aveuglante emplit la pièce...")
        print("Lorsque la lumière se dissipe, vous vous retrouvez dans un endroit familier...")
        print("Vous êtes de retour dans le monde des vivants, avec des souvenirs retrouvés et une nouvelle appréciation pour la vie.")
        print("Félicitations, vous avez trouvé la paix et la rédemption!")
        print("FIN DU JEU !!!")
        print("Ecrit et réalisé par Thomas et Adam.")
        exit()
    
    if reponse_1 == "2":
        print("\nVous insérez votre 'avant bras' dans l'encoche...")
        print("Vous sentez une douleur intense...")
        print("Puis une lumière aveuglante emplit la pièce...")
        raison = ("Votre sex est apparement bien trop massif pour se monde...")
        mort(raison)
  

    
def jeu (info_joueur): 
    insulte = False
    pseudo (insulte, info_joueur)
    intro (info_joueur)
    
    
    

jeu(info_joueur)

















































































































































































































































# tu fais quoi ici mdrrrr


            
            
        
    
