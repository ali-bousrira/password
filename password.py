import hashlib
import json
from random import randint


spec = ["!", "@", "#", "$", "%", "^", "&", "*"]

min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#verification des types de saisie
def is_number(d):
    try:
        float(d)
        return True
    except ValueError:
        return False


#saisie du mot de passe
def password ():
    test_maj = False
    test_min = False
    test_chifre = False
    test_spec = False

    while (test_spec == False or  test_chifre == False or test_maj == False or test_min == False):
        mt_pass = input ("donnez un mot de passe de 8 caracter avec au moins caracter majuscule un minuscule un caracter spécial (!, @, #, $, %, ^, &, *) et un chifre : \n")
        while len (mt_pass) < 8:
            mt_pass = input ("donnez un mot de passe de 8 caracter avec au moins caracter majuscule un minuscule un caracter spécial (!, @, #, $, %, ^, &, *) et un chifre : \n")
        for i in mt_pass:
            if (i in spec):
                test_spec = True
            if (i in min):
                test_min = True
            if (i in maj):
                test_maj = True
            if (is_number (i)):
                test_chifre = True
    return mt_pass


#fonction de sauvegarde
def sauvegard (cript):

    try :

        cont = []
        with open("list_de_mot_de_pass.json", "r") as file:
            for ligne in file:
                cont.append (json.loads(ligne))

        while cript in cont :
            print ("le mot de passe existe deja")
            cript = [hashlib.sha256 (password ().encode('UTF-8')).hexdigest()]



        with open("list_de_mot_de_pass.json", "a") as file:
            json.dump(cript, file)
            file.write('\n')
        
    
    except:
        print ("le ficier sauvegarde de mot de pass nexiste pas on la crer")
        with open("list_de_mot_de_pass.json", "w") as file:
            json.dump(cript, file)
            file.write('\n')

#fonction daffichage
def affiche ():

    try :

        cont = []
        with open("list_de_mot_de_pass.json", "r") as file:
            for ligne in file:
                cont.append (json.loads(ligne))
        print (cont)
        
    
    except:
        print ("le ficier sauvegarde de mot de pass nexiste pas")

#generateur de mot de passe
def random_mot ():
    result = ""

    long = randint(8, 20)

    x = randint (0, long)

    y = randint (0, long)

    while x == y:
        y = randint (0, long)

    z = randint (0, long)
    while x == z:
        z = randint (0, long)

    for i in range (long+1):
        if i == x :
            result += spec [randint (0, len(spec)-1)]

        elif i == y :
            result += min [randint (0, len(min)-1)]

        elif i == z :
            result += maj [randint (0, len(maj)-1)]

        else:        
            result += chr (randint(33, 122))

    return result

def ut_rand (x):
    for i in range (x) :
        ran = random_mot ()
        print ("mot de passe aleatoir ", i, " ", ran)
        sauvegard (ran)




#programe principal

#hashashe du mot de passe
cript = [hashlib.sha256 (password ().encode('UTF-8')).hexdigest()]

#affichage
print ("le mot de passe hasher est : \n", cript)

#creation des mot de passe aleatoire
ut_rand (5)#5 est le nombre de mot de passe a crer


chois = input ("vouler vous enregistrer ce mot de passe hasher oui ou non : \n")
while not (chois == "oui" or chois == "non"):
    chois = input ("vouler vous enregistrer ce mot de passe hasher oui ou non : \n")

if chois == "oui":

    sauvegard (cript)

chois = input ("vouler vous afficher les mot de passe hasher oui ou non : \n")
while not (chois == "oui" or chois == "non"):
    chois = input ("vouler vous afficher les mot de passe hasher oui ou non : \n")

if chois == "oui":
    affiche ()
