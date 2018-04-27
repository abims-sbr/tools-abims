#!/usr/bin/env python

from Tkinter import Button, Entry, Label, Tk

# from guimixin import *

from quitter import Quitter

from tkFileDialog import askopenfilename

from tkMessageBox import showerror, showinfo

from traitefasta import traitefasta
# import math                       # module de mathematique
# import string                     # module d'utilitaire standard


class Application:

    def __init__(self):

        self.root = Tk()                 # cree la fenetre
        self.root.title('OLIGATOR')

        # cree le texte
        Label(self.root, text='Fichier a traiter:').grid(row=0)
        self.entree1 = Entry(self.root, width=10)
        self.entree1.grid(row=0, column=1)
        test = self.entree1
        Button(
            self.root, text='Browse...',
            command=(
                lambda x=test: x.insert(0, askopenfilename()))).grid(
                    row=0, column=2)

        Label(self.root, text='Tm (temperature de fusion) :').grid(row=1)
        self.entree2 = Entry(self.root, width=10)
        self.entree2.grid(row=1, column=1)

        Label(self.root, text='Nom des fichiers de sortie:').grid(row=2)
        self.entree3 = Entry(self.root, width=10)
        self.entree3.grid(row=2, column=1)

        Button(
            self.root, text='Run',
            command=self.runOligator).grid(row=3, column=1)
        Quitter(self.root).grid(row=3, column=4)
        Button(
            self.root, text='Help',
            command=self.runHelp).grid(row=3, column=5)

        self.root.mainloop()

    def runOligator(self):
        self.n = self.entree1.get()
        self.tm = self.entree2.get()
        self.nom_sortie = self.entree3.get()

        self.message_creation = 'vous venez de creer 3 fichiers de resultats:'
        self.message_creation += '\n-'+self.nom_sortie+'\n-'+self.nom_sortie
        self.message_creation += '_sens.csv\n-'
        self.message_creation += self.nom_sortie+'_anti-sens.csv'

        if self.n != "" and self.tm != "" and self.nom_sortie != "":
            try:
                traitefasta(self.n, self.tm, self.nom_sortie)
                showinfo('resultat', self.message_creation)
            except ImportError:
                showerror('Error!', "Votre fichier n'est pas au format fasta")

        if self.n == "" or self.nom_sortie == "" or self.tm == "":
            showerror('Error!', "Vous n'avez pas remplis tous les champs")

    def runHelp(self):
        showinfo(
            'Help', 'Oligator version 1.1 edition du 29 octobre 2004.\n\n \
            Ce logiciel a ete realise par Frederic Lechauve \
            frederic_lechauve@yahoo.fr en python 2.3')


f = Application()
