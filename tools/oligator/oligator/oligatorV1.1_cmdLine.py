#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LECHAUVE Frederic - frederic_lechauve@yahoo.fr
# Command line version (03/09/2013) : CORMIER Alexandre -
#                                       acormier@sb-roscoff.fr
# Command line version (26/04/2018) : LE CORGUILLE Gildas -
#                                       lecorguille@sb-roscoff.fr

# ##################################import des librairies######################

import argparse                     # module pour parser les arguments

import traitefasta

# #################################creation du module pour les options#########

parser = argparse.ArgumentParser(
    description="Oligator : design PCR primers\n")
parser.add_argument(
    "-i", "--input", action="store", dest="file", type=open,
    required=True, help="input file : fasta format")
parser.add_argument(
    "-t", "--tm", action="store", type=int, dest="Tm",
    required=True, help="Tm value")
parser.add_argument(
    "-o", "--output", action="store", dest="output",
    type=argparse.FileType('w'), help="output filename")
parser.add_argument(
    '--version', action='version', version='%(prog)s v1.1')

options = parser.parse_args()

fileIn = options.file.name
Tm = options.Tm
Out = 'oligator'  # nom par defaut (utile pour Galaxy)
if options.output is not None:
    Out = options.output.name

traitefasta.traitefasta(fileIn, Tm, Out)
