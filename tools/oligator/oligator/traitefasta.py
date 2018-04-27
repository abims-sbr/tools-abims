#!/usr/bin/env python


# ##################################import des librairies#####################

# import math                     # module de mathematique
import string                     # module d'utilitaire standard

# #################################Fonction###################################


def traitefasta(n, tm, nom_sortie):

    n = open(n, 'r')                   # ouverture dufichier
    dico = {}                         # declaration du dictionnaire
    liste_id = []

    for ligne in n.readlines():       # lit toute les lignes du fichier

        if ligne[0] == '>':            # matche les lignes debutant par >
            # une variable recoit la ligne contenant le nom de la seq
            # sans le superieur et sans le retour chariot
            n = ligne[1:-1]
            liste_id.append(n)
            t = ''                      # la variable t est initialisee
        else:
            t = t + ligne[:-1]   # t recoit la sequence sans le retour chariot

        t = string.upper(t)      # on passe la sequence en majuscule
        # on cree un dictionnaire ayant pour cle le nom de la seq
        # et pour valeur la sequence
        dico[n] = t

    # #######################traitement du dictionnaire#######################
    sortie = open(nom_sortie+'_results.csv', 'w')
    sortie_csv = nom_sortie+'_sens.csv'
    sortie_anticsv = nom_sortie+'_anti-sens.csv'
    sortie1 = open(sortie_csv, 'w')
    sortie2 = open(sortie_anticsv, 'w')
    temp = int(tm)

    for x in liste_id:          # balaie tous les cles du fichier

        i = 0                         # initialisation du compteur de lettre
        j = 0                         # initialisation du Tm
        # la variable seq recoit la sequence correspondante a la cle
        seq = dico[x]
        oligo = ''                    # initialisation de l'oligo
        # tant que le tm est inferieur a 70 la boucle continue
        while j < temp:
            if seq[i] == 'A':      # test le nucleotide de rang i
                j = j+2
            elif seq[i] == 'T':
                j = j+2
            elif seq[i] == 'G':
                j = j+4
            elif seq[i] == 'C':
                j = j+4
            # on concatene les resultats pour creer l'oligo sens
            oligo = oligo+seq[i]
            i = i+1                    # on incremente

        taille = len(oligo)
        taille = str(taille)
        j = str(j)              # transforme le chiffre en chaine de caractere
        sortie.write(x)   # on ecrit les resultats dans le fichier de resultat
        sortie.write('\n')
        sortie.write(oligo)
        sortie.write('\n')
        sortie.write('Tm = ')
        sortie.write(j)
        sortie.write('\n')
        sortie.write('The oligo length is ')
        sortie.write(taille)
        sortie.write(' nucleotide(s)\n\n')

        sortie1.write(x)
        sortie1.write(';')
        sortie1.write(oligo)
        sortie1.write(';')
        sortie1.write(taille)
        sortie1.write('\n')

    for x in dico.keys():         # balaie tous les cles du fichier
        # initialisation du compteur de lettre a -1
        # pour creer l'oligoantisens pour parcourir le mot a l'envers
        i = -1
        j = 0                        # initialisation du Tm
        # la variable seq recoit la sequence correspondante a la cle
        seq = dico[x]
        oligo = ''                   # initialisation de l'oligo
        inv = ''
        # tant que le Tm est inferieur a 70 la boucle continue
        while j < temp:
            if seq[i] == 'A':     # test le nucleotide de rang i
                j = j+2
                inv = 'T'
            elif seq[i] == 'T':
                j = j+2
                inv = 'A'
            elif seq[i] == 'G':
                j = j+4
                inv = 'C'
            elif seq[i] == 'C':
                j = j+4
                inv = 'G'
            oligo = oligo+inv
            i = i-1                 # on decremente

        taille = len(oligo)
        taille = str(taille)
        j = str(j)            # transforme le chiffre en chaine de caractere
        sortie.write(x)
        sortie.write('_antisens\n')
        sortie.write(oligo)
        sortie.write('\n')
        sortie.write('Tm = ')
        sortie.write(j)
        sortie.write('\n')
        sortie.write('The oligo length is ')
        sortie.write(taille)
        sortie.write(' nucleotide(s)\n\n')

        sortie2.write(x)
        sortie2.write(';')
        sortie2.write(oligo)
        sortie2.write(';')
        sortie2.write(taille)
        sortie2.write('\n')

    sortie.close()
    sortie1.close()
    sortie2.close()
