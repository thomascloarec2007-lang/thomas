from random import randint 

# Déclaration des variables représentant des caractéristiques du joueur pour une utilisation future
pv = 20
épée = 2
stam = 100

inventaire = ["amullette", "épée"]

info_joueur = {"pv":pv, "épée": épée, "stam": stam, "inventaire":inventaire}




#fonction triche
def triche (insulte, info_joueur):

    reponse_1 = input(print("Choisisez la fonction que vous voulez atteindre, entre: \n1)intro\n2)combat1 (étrangé)\n3)combat2(gardien)\n4)partie2\n5)pseudo\n6)fin_du_jeu "))
    info_joueur["nom"] = "joueur214"
    if reponse_1 =="intro" or reponse_1 =="1":
        intro(info_joueur)

    if reponse_1 =="combat1" or reponse_1 =="2":
        pv_du_moche = 10
        raison = "Le sale moche vous a tué..."
        num_combat = 1
        combat(info_joueur, pv_du_moche, raison, num_combat)

    if reponse_1 =="combat2(gardien)" or reponse_1 =="3":
        num_combat = 2
        pv_du_moche = 50
        raison = "Le monstre vous a tué... Il semble bien trop fort, ou bien VOUS êtes bien trop faible."
        combat(info_joueur, pv_du_moche, raison, num_combat)

    if reponse_1 =="partie2" or reponse_1 =="4":
        partie_2(info_joueur)

    if reponse_1 =="pseudo" or reponse_1 =="5":
        pseudo (insulte, info_joueur)

    if reponse_1 =="fin_du_jeu" or reponse_1 =="6":
        fin_combat_2()
    else:
        triche(info_joueur)
    return

#focntion quand joeur ouvre son inventaire
def inventaire(info_joueur):
    action = False
    print ("Vous avez dans votre inventaire: ")
    for i in range (len(info_joueur["inventaire"])):
        print (str(i+1) + ") " + str(info_joueur["inventaire"][i]))
        if info_joueur["inventaire"][i] == "potions":
            action = True
            tmp = i
    if action == True:
        print ("Vous pouvez: ")
        diff_choix = ["vous soignez", "rien faire"]
        reponse_1 = reponse(diff_choix)
        if reponse_1 == "1":
            info_joueur["inventaire"].pop(tmp)
            info_joueur["pv"] += 10
            return info_joueur
        if reponse_1 == "2":
            print("Vous ne faites rien.")
            return
    if action == False:
        return

# fonction qui gère les différents choix
def reponse (diff_choix):
    valeur_accepter = []
    for i in range (len(diff_choix)):
        tmp = i + 1
        print ((str(tmp)) + ")" + str(diff_choix[i]))
        valeur_accepter.append(str(tmp))

    rep_user = input("Entrez votre choix : ")
    if rep_user == "exit":
        print("Au revoir !")
        exit()
    elif rep_user not in valeur_accepter:
        print("Veuillez choisir une réponse correcte ou entrer 'exit' pour quitter le programme.")
        return reponse(diff_choix)
    else:
        print("Vous choisissez " + str(diff_choix[int(rep_user)-1]) + ".")
        print("-----------------------------------CHOIX---------------------------------------\n")
        return rep_user

# fonction pour mort joueur, avec possibilité de voir la cause de sa mort
def mort(raison):
    print("Vous êtes mort, GAME OVER")
    tmp = input("Afficher la cause de la mort ? (oui/non) ")
    if tmp != "oui" and tmp != "non":
        mort(raison)
    else:
        if tmp == "oui":
            print("La cause de votre mort est : " + raison)
            exit()
        else:
            exit()

# Récupère dans une variable le nom pour une utilisation future
def pseudo (insulte, info_joueur):
    nom = input("Choisissez un pseudonyme, il ne doit contenir que des lettres.\nIndiquez votre nom : ")
    cara = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNéàèûù"
    for i in nom:
        if i not in cara:
            insulte = True
            print("Gros, apprends à lire des consignes, sinon ça ne va pas le faire.")
            pseudo (insulte, info_joueur)
     
    if insulte == True:
        print("Bon toutou !")
    info_joueur["nom"] = nom
    return info_joueur

# Introduction
def intro (info_joueur):

    print("\nVous vous réveillez amnésique et affaibli en dessous d'un grand arbre en amont d'une colline aride.")
    print("Vous regardez vos effets personnels.")
    print("Vous avez sur vous une étrange amulette ainsi qu'une épée.")
    print("\nLa nuit va bientôt tomber.")
    partie_1 (info_joueur)

# partie 1, premier choix
def partie_1 (info_joueur):
    print("Vous regardez autour de vous.")
    print("À l'ouest : une intense source de lumière blanche.")
    print("Vous décidez :")
    diff_choix = ["de vous réfugier", "de retrouver d'où vous venez"]
    reponse_1 = reponse (diff_choix)

    if reponse_1 == "1":
        branche1 (info_joueur)

    if reponse_1 == "2":
        branche2(info_joueur)

# partie 1, branche 1, grotte
def branche1 (info_joueur): 
    print("\nVous trouvez une grotte sombre à l'abri pour la nuit.")
    print("Vous décidez de : ")
    diff_choix = ["Vous y réfugier pour la nuit", "Passer la nuit à l'extérieur malgré la pluie"]
    reponse_1_1 = reponse (diff_choix)

    if reponse_1_1 == "1":
        branche1_1(info_joueur)

    if reponse_1_1 == "2":
        raison = "mort de froid"
        mort(raison)

# partie 1, branche 2 ; source lumineuse      
def branche2 (info_joueur):  
    print("\nVous marchez vers l'intense et éblouissante source lumineuse.")
    print("Vous croisez le chemin d'un inconnu.")
    print("Ce dernier est disgracieux, avec une peau grasse et rugueuse, un visage boursouflé, un nez imposant et large, une pilosité hors de contrôle et la moitié de ses dents.")
    print("Il inspirait le vice.")
    print("Celui-ci vous demande si vous êtes perdu.")
    print("Vous lui expliquez votre situation puis vous lui demandez s'il reconnaît le blason sur votre amulette.")
    print("Il vous répond qu'il s'agit du blason de l'intermonde et vous conseille de vous rendre dans la ville la plus proche située à l'est, en traversant une forêt.")
    print("\nVous décidez : ")
    diff_choix = ["De lui faire confiance et de suivre son indication", "De ne pas lui faire confiance et de continuer votre chemin vers l'ouest"]
    reponse_1_1 = reponse (diff_choix)

    if reponse_1_1 == "1":
        branche2_1(info_joueur)

    if reponse_1_1 == "2":
        branche2_2(info_joueur)


# fonction entrez pour partie 2
def branche1_1(info_joueur):
    print("\nVous entrez dans la grotte.")
    print("Après plusieurs minutes de vérifications, vous apercevez une faible lueur dans la pénombre.")
    print("Vous êtes apeuré et intrigué par cette dernière.")
    print("Une voix mystérieuse vous appelle : 'v..vv...viens par ici " + str(info_joueur["nom"]) + "'")
    
    partie_2(info_joueur)

# partie 1, branche 2 (rencontre brigand), choix 1
def branche2_1(info_joueur):
    print("\nVous rentrez dans une forêt.")
    print("Deux chemins s'offrent à vous : ")
    print("\nVous décidez : ")
    diff_choix = ["D'aller à droite", "De ne respecter aucune règle et de faire tout droit (BAAAKKAAA)", "D'aller à gauche"]
    reponse_1_1 = reponse(diff_choix)
    if reponse_1_1 == "1":
        rencontre_brigant_apres_forêt(info_joueur)

    if reponse_1_1 == "2":
        print("\nVous vous sentez enfin libre ! Plus personne ne vous dicte quoi que ce soit !!! Vous courez, sautez, riez !!!\nPuis trébuchez et mourez...")
        raison = "Frérot, tu n'es personne, redescends un peu..."
        mort(raison)

    if reponse_1_1 == "3":
        body_dead(info_joueur)
#corp trouvé
def body_dead(info_joueur):
    print("\nVous vous baladez et trouvez la dépouille d'un voyageur... Étrange...")
    print("Vous décidez : ")
    diff_choix = ["De le fouiller", "De respecter les morts..."]
    reponse_1_1 = reponse(diff_choix)

    if reponse_1_1 == "1":
        print("\nVous trouvez une potions de soin !!")
        info_joueur["inventaire"].append("potions")
        print("\nVous décidez de partir avant de rencontrer l'auteur du crime.\nMais...")
        rencontre_brigant_apres_forêt(info_joueur)

    if reponse_1_1 == "2":
        print("\nVous vous éloignez, la nausée vous monte à la gorge...\nVous vous retournez et partez en courant...")
        rencontre_brigant_apres_forêt(info_joueur)

def rencontre_brigant_apres_forêt(info_joueur):
    print("Vous recroisez l'étranger à un tournant, qui vous regarde d'un air menaçant...")
    print("Il s'agissait d'un piège... Il ne faut jamais faire confiance aux personnes moches...")
    print("\nL'homme s'élance vers vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    raison = "Le sale moche vous a tué..."
    num_combat = 1
    combat(info_joueur, pv_du_moche, raison, num_combat)

# partie 1, branche 2 (rencontre brigand), choix 2
def branche2_2(info_joueur):
    print("\nVous partez dans la direction opposée.")
    print("Vous recroisez l'étranger à un tournant, qui vous regarde d'un air menaçant...")
    print("Il s'agissait d'un piège... Les moches sont toujours vicieux...")
    print("\nL'homme s'élance vers vous, armé d'une dague !!!")
    print("Vous devez vous battre !!!")
    pv_du_moche = 10
    raison = "Le sale moche vous a tué..."
    num_combat = 1
    combat(info_joueur, pv_du_moche, raison, num_combat)

# fonction pour la partie défense du combat
def deffense (info_joueur, raison): 
    if info_joueur["stam"] <= 0:
        print("\nVous n'avez pas la force d'esquiver...")
        info_joueur["pv"] -= 5
    else:    
        attaque = randint(1,2)
        print("\nAttention, esquivez !!!")
        diff_choix = ["vers la droite", "vers la gauche"]
        reponse_1_1 = reponse(diff_choix)
        if int(reponse_1_1) == attaque:
            chance = randint(1, 100)
            if chance > 90:  
                info_joueur["pv"] -= 2 
                print("\nBonne esquive !!! Mais vous êtes tout de même touché !!!")
                print("Il vous reste : " + str(info_joueur["pv"]) + " pv.")
            else:
                print("\nBien esquivé !!! Vous ne subissez aucun dommage !!!")
        if int(reponse_1_1) != attaque:
            info_joueur["pv"] -= 5
            print("\nMauvais côté... Vous subissez d'importants dommages...")
        
    if info_joueur["pv"] <= 0:
        mort(raison)
    return info_joueur




# fonction pour la partie attaque du combat
def attaque (info_joueur, pv_du_moche):
    if info_joueur["stam"] <= 0:
        print("\nC'est à votre tour d'attaquer, mais vous n'avez plus d'endurance... Vous devez vous reposer.")
        info_joueur["stam"] += 20 
    else:
        print("\nÀ votre tour, choisissez votre attaque.")
        diff_choix =  ["Attaque vive", "Attaque basique", "Attaque lourde", "Se reposer", "inventaire"]
        attaque = reponse(diff_choix)
        if attaque == "1":
            info_joueur["stam"] -= 8
            chance = randint (1,100)
            if chance > 90:
                print ("\nVotre attaque échoue...")
            else:
                print("\nBravo, vous infligez des dégâts !!!")
                pv_du_moche -= info_joueur["épée"]
            
        if attaque == "2":
            info_joueur["stam"] -= 15
            chance = randint (1,100)
            if chance > 80:
                print ("\nVotre attaque échoue...")  
            else:
                print("\nBravo, vous infligez des dégâts !!!")
                pv_du_moche -= info_joueur["épée"] + 3

        if attaque == "3":
            info_joueur["stam"] -= 20
            chance = randint (1,100)
            if chance > 70:
                print ("\nVotre attaque échoue...") 
            else:
                print("\nBravo, vous infligez des dégâts !!!")
                pv_du_moche -= info_joueur["épée"] + 6

        if attaque == "4":
            print("\nVous vous reposez et regagnez de l'endurance.")
            info_joueur["stam"] += 30 
            if info_joueur["stam"] > 200:
                info_joueur["stam"] = 200
                print("Abuse de la redbull fréro")
        
        if attaque == "5":
            inventaire(info_joueur)

        if pv_du_moche > 0:
            print("Il lui reste : " + str(pv_du_moche) + " pv.")
        else:
            print("Votre ennemi semble mal en point... Il titube puis s'effondre !")

        if info_joueur["stam"] < 15:
            print("Vous vous sentez fatigué...")

    return (info_joueur, pv_du_moche)


def combat(info_joueur, pv_du_moche, raison, num_combat):  
    
    while pv_du_moche > 0:
        deffense(info_joueur, raison)
        print ("Il vous reste " + str(info_joueur["pv"]) + " pv, ainsi que " + str(info_joueur["stam"]) + " de stamina." )
        pv_du_moche_tmp = attaque (info_joueur, pv_du_moche)

        pv_du_moche = pv_du_moche_tmp[1]
    if num_combat == 1:
        fin_combat_1 (info_joueur)
    if num_combat== 2:
        fin_combat_2 ()

# fin combat avec le brigand
def fin_combat_1 (info_joueur):
    print("\nFélicitations, vous avez vaincu l'ennemi !!!")
    print("Vous fouillez le corps de l'ennemi...")
    print("Vous récupérez sa dague ainsi que de la nourriture.")
    info_joueur["épée"] += 20
    print("Vous décidez de : ")

    diff_choix = ["Manger pour vous restaurer", "Laisser pour le prochain"]
    reponse_1_1 = reponse(diff_choix)
    if reponse_1_1 == "1":
        info_joueur["pv"] += 20
        print("\nVous mangez et vous vous restaurez.")
    if reponse_1_1 == "2":
        print("\nVous laissez la nourriture pour le prochain.")
    
    print("\nVous êtes encore complètement perdu, mais au moins vous êtes en vie...")
    print("La nuit commence à tomber, vous décidez de chercher un abri pour la nuit...")
    branche1 (info_joueur)



# partie 2
def partie_2(info_joueur): 
    print("\nLa chose semble vous connaître...")
    print("En sait-elle davantage sur vous et sur ce monde ?")
    print("Vous décidez de vous avancer vers la voix...")
    print("Vous arpentez de longs corridors humides et sombres...\nSoudain, vous arrivez dans une vaste salle éclairée par des torches.")    
    print("Au centre de cette pièce se tient une silhouette encapuchonnée...")
    print("Elle ne semble pas hostile...\nElle vous fait signe de vous approcher...\nVous vous avancez prudemment...")
    print("\n« Cela fait bien longtemps que je n'ai pas vu un mortel... » dit la créature d'une voix rauque.")
    print("« Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde. »")

    print("Vous demandez :")

    diff_choix = ["Pouvez-vous me parler plus de ce qu'est cet intermonde ?", "Mais qui êtes-vous au juste ?"]
    reponse_1 = reponse(diff_choix)
    if reponse_1 == "1":
        branche2_1_1(info_joueur)
    if reponse_1 == "2":
        branche2_1_2(info_joueur)

def branche2_1_1(info_joueur):
    print("\n« L'intermonde est un lieu entre les mondes, un carrefour pour les âmes perdues », répond l'Archiviste.")
    print("« Certaines personnes y sont envoyées pour expier leurs fautes, d'autres errent ici après la mort, incapables de trouver la paix. »")
    branche2_2_1(info_joueur)

def branche2_1_2 (info_joueur):
    print("\n« Je suis l'Archiviste, gardien des savoirs oubliés de cet intermonde », répond la créature.")
    print("« Mon rôle est de préserver les connaissances anciennes et d'aider ceux qui cherchent des réponses. »")
    print("Ainsi que de guider les âmes égarées comme la vôtre, à retrouver la voie de la paix éternelle.")
    branche2_2_1(info_joueur)

def branche2_2_1(info_joueur):
    print("\nAvec ces simples mots, vous comprenez que vous êtes mort...")
    print("Mais vous ne vous rappelez toujours pas qui vous étiez de votre vivant...")
    print("Vous hésitez à lui montrer votre amulette, qui semble avoir une signification particulière ici...")
    print("Vous choisissez :")

    diff_choix = ["De lui montrer", "De garder le secret"]
    reponse_1 = reponse(diff_choix)
    if reponse_1 == "1":
        branche2_3_1(info_joueur)
    if reponse_1 == "2":
        branche2_3_2(info_joueur)

def branche2_3_2(info_joueur):
    print("\nVous n'avez plus rien à faire ici et décidez de partir.")
    print("Vous quittez la grotte et marchez dans la nuit sombre...")
    print("Tourmenté par cette révélation, vous errez sans but à travers les paysages de l'intermonde...")
    print("Vous vous sentez vide, perdu et désespéré...")
    print("Finalement, vous vous effondrez, submergé par la tristesse et la solitude...")
    print("Vous sortez votre épée et vous vous suicidez...")
    raison = "Vous vous êtes suicidé de tristesse #BAAAKKKKAAAA"
    mort(raison)

def branche2_3_1(info_joueur): 
    print("\nL'Archiviste regarde l'amulette avec une expression de surprise.")
    print("Cependant, cette expression se transforme vite en un regard farouche.")
    print("La chose vous fixe dans les yeux avec un regard noir... Vous voyez maintenant son visage, qui n'a rien d'humain...")
    print("« Cette amulette est une relique perdue... ou plutôt volée... » dit la créature.")
    print("« Volée il y a des milliers d'années, au prix de la vie de nombreux des miens... Tu paieras pour les crimes de tes ancêtres !!! »")
    print("La créature se jette sur vous, furieuse de votre possession de l'amulette...")
    print("Vous devez vous battre pour votre survie !!!")
    print("\nLe monstre s'élance vers vous !!!")
    num_combat = 2
    pv_du_moche = 50
    raison = "Le monstre vous a tué... Il semble bien trop fort, ou bien VOUS êtes bien trop faible."
    combat(info_joueur, pv_du_moche, raison, num_combat)

def fin_combat_2():
    print("\nFélicitations, vous avez vaincu l'ennemi !!!")
    print("En mourant, la créature murmure : « Peut-être qu'un jour tu comprendras le fardeau que tu possède... »")
    print("Vous sentez une étrange paix vous envahir...")
    print("Vous continuez votre chemin, l'amulette brillant faiblement autour de votre cou...")
    print("Alors, vous tombez nez à nez avec une structure qui s'apparente à un portaille...")
    print("En vous approchant, vous discernez des inscriptions anciennes gravées sur le cadre de la structure...")
    print("Vous repérez une encoche en forme de serrure au centre de la porte...")
    print("Vous décidez de : ")

    diff_choix = ["Insérer l'amulette", "Insérer votre machin"]
    reponse_1 = reponse(diff_choix)
    
    if reponse_1 == "1":
        print("\nVous insérez l'amulette dans l'encoche...")
        print("Un éclat de lumière aveuglante emplit la pièce...")
        print("Lorsque la lumière se dissipe, vous vous retrouvez dans un endroit familier...")
        print("Vous êtes de retour dans le monde des vivants, avec des souvenirs retrouvés et une nouvelle appréciation pour la vie.")
        print("Félicitations, vous avez trouvé la paix et la rédemption !\n\n\n")
        chapitre2(info_joueur)
    

    
    if reponse_1 == "2":
        print("\nVous insérez votre machin dans l'encoche...")
        print("Vous ressentez une douleur intense...")
        print("Puis une lumière aveuglante emplit la pièce...")
        raison = "Votre machin est apparemment bien trop massif pour ce monde..."
        mort(raison)






def chapitre2(info_joueur):
    print("----------------------------CHAPITRE II------------------------------")
    print("En vous révéyant vos souvenires vous reviennent.")
    print("Vous vous rappellez de TOUT, votre famille, vos amis et même votre plus grande passion, le jeu video.")
    print("Mais... Vous n'avez pas oubliez ce que vous venez de vivre...")
    print("Alors vous assaye de comprendre ce qu'il vient de ce passer")
    print("Après vous être cresé les méninges, vous comprenez (infin) que vous étiez apparement mort ou du moins presque mort...")
    print("Vous vous demandez donc tout naturelement comment vous auriez pue mourir")
    print("Vous descidez de regarder votre historique internet et apparement, votre dernière recherche porte sur une chaine youtube au nom de EGO...")
    print("Vous ne conaissez pourtant pas ce youtubeur, alors vous cliquez et votre ordinateur lance une video qui parle d'un certain jeu, le jeu de la vie... ")
    print("Y a t'il un rapport entre ce jeu et votre mort??? Seul vous pouvez le déterminer")
    diff_choix = ["continuer les recherches", "en rester là et être dans l'ignorance"]
    reponse_1 = reponse(diff_choix)
    if reponse_1 == "1":
        recherche_cause_mort(info_joueur)
    if reponse_1 == "2":
        print("Vous reprenez le cours de votre vie, et restez dans le déni")
        raison = "Vous mourrez à cause d'une torsion testiculaire peut après que votre femme vous quitte pour votre frère"
        mort (raison)

def recherche_cause_mort(info_joueur): 
    print("Vous descidez de faire vos propres recherche sur ce jeu, donc vous l'installé.")
    print("Lors du lancement, votre écran ce met à buger, des terminaux s'ouvrent dans tout les senses!!!")
    print("Alors une fenêtre s'ouvre est vous demande: ")
    chance = 0
    while chance < 3:
        print("\nil vous reste "+str(3 - chance)+" éssaie")
        reponse_1 = input("Entrez PASSWORD: ")
        
        if reponse_1 == "PASSWORD" or reponse_1 == "password": 
            chance = 10
            print("'MOT DE PASSE CORRECTE' s'affiche sûr l'écran")
            print ("Le jeu de la vie de lance correctement\n\n")
            jeu_de_la_vie()
            exit()
        chance += 1
    print("\n3 erreurs... c'est pas bon signe... Votre pc commence à faire du bruit... que dis-je, à VROMBIRE, BOUF BOUF BOUF!!!")
    print("Puis une énorme explosion se preduit ... ")
    print("Soudain ...\n")
    intro(info_joueur)




def jeu_de_la_vie ():
    largeur = 0
    largeur = int(input("largeur: "))

    def affichage (tableau):
        for i in range (len(tableau)):
            tmp = ""
            for k in range (len(tableau[i])):
                tmp += str(tableau[i][k][0]) + "|"
            print (tmp)
        print ("\n")

    def tableau (largeur):
        tableau = []
        ligne = []
        case = [0]

        for l in range (largeur):
            for c in range (largeur):
                ligne.append(case)
            tableau.append(ligne)
            ligne = []
            
        affichage (tableau)
        return tableau

    tableau = tableau (largeur)
    

    


    def modification(largeur):
        nombre_de_mod = 0
        nombre_de_mod = int(input("nombre de modification: "))
        cara = []
        for i in range (largeur):
            cara.append(i+1)
        co_tmp_x = 0 
        co_tmp_y = 0 
        coordonnée = []
        for i in range (nombre_de_mod):
            co_tmp_x = int(input("entrée la valeur de la coordonée x de votre modification n°"+ str(i + 1) + ": "))
            if co_tmp_x not in cara:
                print("valeur out of range")
                return modification(nombre_de_mod, largeur)
            co_tmp_y = int(input("entrée la valeur de la coordonée y de votre modification n°"+ str(i + 1) + ": "))
            if co_tmp_y not in cara:
                print("valeur out of range")
                return modification(nombre_de_mod, largeur)
            z = (co_tmp_x, co_tmp_y)
            coordonnée.append(z)
        return (coordonnée)

    coordonnée = modification(nombre_de_mod, largeur )


    def modification_tabelau(tableau, coordonnée, nombre_de_mod):
        for i in range (nombre_de_mod):
            x = coordonnée[i][0]
            y = coordonnée[i][1]
            tableau[y-1][x-1] = ["X"]
            
        affichage (tableau)
        return tableau

    tableau = modification_tabelau(tableau, coordonnée, nombre_de_mod)

    def tabeleau_modi(tableau):
        
        mort = []
        vie = []
        x = 0
        y = 0
        for i in range (len(tableau)):
            for k in range (len(tableau[i])):
                x = k + 1
                y = i + 1
                tmp = []

                if y-2 >= 0 and y-2 <= len(tableau)-1:
                    if x-2 >= 0 and x-2 <= len(tableau[i])-1:
                        tmp.append(tableau[y-2][x-2])  
                    if x-1 >= 0 and x-1 <= len(tableau[i])-1:
                        tmp.append(tableau[y-2][x-1]) 
                    if x >= 0 and x <= len(tableau[i])-1: 
                        tmp.append(tableau[y-2][x])    
                    else: 
                        tmp.append([])  
                else:
                    tmp.append([])
            
                if y-1 >= 0 and y-1 <= len(tableau)-1:
                    if x-2 >= 0 and x-2 <= len(tableau[i])-1:
                        tmp.append(tableau[y-1][x-2])
                    if x >= 0 and x <= len(tableau[i])-1:
                        tmp.append(tableau[y-1][x])
                    else:
                        tmp.append([]) 
                else:
                    tmp.append([])  


                if y >= 0 and y <= len(tableau)-1:
                    if x-2 >= 0 and x-2 <= len(tableau[i])-1:
                        tmp.append(tableau[y][x-2])
                    if x-1 >= 0 and x-1 <= len(tableau[i])-1:
                        tmp.append(tableau[y][x-1])
                    if x >= 0 and x <= len(tableau[i])-1:
                        tmp.append(tableau[y][x])
                    else:
                        tmp.append([]) 
                else:
                    tmp.append([]) 

                nbr_case_en_vie = 0
                for h in range (len(tmp)):
                    if tmp[h] == ["X"]:
                        nbr_case_en_vie += 1

                   
                    
                coordonnée = (k, i)

                if tableau[i][k] == ["X"] and nbr_case_en_vie < 2:
                    mort.append(coordonnée)
                

                if tableau[i][k] == ["X"]and nbr_case_en_vie > 3:
                    mort.append(coordonnée)
                    

                if tableau[i][k] == [0] and nbr_case_en_vie == 3:
                    vie.append(coordonnée)
                   


        #remplace case vivante en morte
        for t in range (len(mort)):
            x_1 = mort[t][0]
            y_1 = mort[t][1]
            tableau[y_1][x_1] = [0]

        #remplace case morte en vivante  
        for t in range (len(vie)):
            x_1 = vie[t][0]
            y_1 = vie[t][1]
            tableau[y_1][x_1] = ["X"]

        affichage (tableau)        
        return tableau

    tour = 0            
    nbr_de_tour = int(input("Combien de tour voulez vous?: "))     
    while tour != nbr_de_tour:
        tabeleau_modi (tableau)
        tour += 1
    modification(largeur )



def initialisation_jeu ():
    insulte = False
    triche_activé = input("Voulez vous trichez?: ")
    if triche_activé == "oui" or triche_activé == "OUI":
        triche (insulte, info_joueur)
    else: 
        print("Bienvenue dans ce jeu !")
        print("Vous pouvez le quitter à tout moment en tapant 'exit'.")
        pseudo(insulte, info_joueur)
        intro(info_joueur)


initialisation_jeu()

