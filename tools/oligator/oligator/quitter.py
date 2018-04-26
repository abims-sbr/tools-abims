#!/usr/bin/python

from Tkinter import *                          # get widget classes
from tkMessageBox import askokcancel           # get canned std dialog

class Quitter(Frame):                          # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = askokcancel('Verifier exit', "Voulez vous quitter l'application?")
        if ans: Frame.quit(self)

if __name__ == '__main__':  Quitter().mainloop()
#def ende(): Quitter().mainloop()
