# -*-coding:Latin-1 -*
import os

print("----------REGLES----------")
print("Bienvenue dans ce minijeu, pour faire simple, vous allez lire un petit scenario et vous devrez vous enfuir du lieu où vous vous trouver a l'aide de mots cles. \n")
print("Utiliser ceux qui seront ecrit dans le texte du narrateur pour declencher des actions.")
print("----------REGLES---------- \n")

print("----------SCENARIO----------")
print("Vous êtes un espion envoyer par votre gouvernement pour derober les plans de la nations ennemis, malheuresement vous avez ete capturer juste apres avoir recuperer les plans. Vous voila donc attacher sur une chaise en bois, les mains dans le dos.")
print("----------SCENARIO---------- \n")

print("*La salle dans laquelle vous êtes est ronde et relativement petite, vous ne voyer que devant vous, a votre gauche et a votre droite, pour ce qui est de l'arriere vous ne voyer rien mais apercever une lumiere quand vous essayer de regarder derriere vous.")
print("Tout d'abord vous deviez tentez de vous liberer(sauf si vous souhaitez vous vendre aux ennemis, dans quel cas vous êtes un lâche). \n")
print("Devant vous il n'y a rien, seulement la porte a 3 bon metres de distance.")
print("A votre droite ce trouve un meuble couvert d'ustensile; couteaux, cuillieres, seringues, rapes..ect.")
print("A votre gauche ce trouve un brasier avec brulant avec un tisonnier poser dessus.")
print("Et derriere vous, vous ne voyer rien mais supposez qu'il y a une sorte de d'ouverture ou de fenetre. \n")


#boucle pour redemander en continue si user tape int ou mot inexistant
# ne detecte pas si ces un int avec des if, donc obliger? d'user de try except
# ne detecte pas les int !! PUTAIN !!

# 1) Comencer par regler les fautes de frappes en str V
# 2) Boucle pur redemander si erreur
# 3) Si chiffre taper ?
chaise = input("Que faites-vous ? ")

if chaise == str(chaise):
    if chaise == ("droite") or chaise == ("couteaux"):
        print("Vous tentez de basculez sur la droite en remuant votre corps, puis, vous parvenez a faire tomber la chaise au sol, cognant au passage le meuble.")
        print("Cette action fit tomber alors le couteau dans votre direction...la derniere chose que vous voyez c'est la lame s'approchant a grande vitesse de votre crane...")
    elif chaise == ("gauche") or chaise == ("brasier") or chaise == ("tisonnier"):
        print("Vous servir du brasier ou du tisonnier pour enflammez les attaches semblait une bonne idée..mais la réalité fut que vous tombiez sur le coté gauche tête la premiere dans le brasier..Une mort des plus douloureuses")
    elif chaise == ("devant") or chaise == ("porte"):
        print("Vous tentez de basculez vers l'avant....vous passez plusieurs secondes a basculez d'avant en arrières tel un fou dans sa chambre capitonner, puis, vous parvenez a tomber vers l'avant.")
        print("Pendant votre chute vers l'avant vous vous demander alors pourquoi avoir effectuer cette actions ? Vous n'avez malheuresement pas le temps d'y répondre puisque vous vous fracasser mortellement le crane contre le sol..")
    elif chaise == ("derriere") or chaise == ("fenetre"):
        print("Vous essayer de vous faire tombez en arriere, le choix le plus risqué puisque vous ne savez pas ce qui si trouve.\n") 
        print("Lors de votre chute, votre chaise cogne une fenetre et brise un carreau, laissant de mutliple bout de verre au sol, sur lesquelles vous tombez, vous blessant a la main, mais par chance, vous arrivez a en saisir un et a scier vos attaches avec succès. Vous êtes libre !")
    elif chaise == ("attendre") or chaise == ("rien"):
        print("Vous avez decider d'attendre et d'affronter la torture.")
    else:
        print("Essayer un autre mot clé. Relisez la phrase de description.") #Dans le cas où le mot ne correspond pas.


  

os.system("pause")
