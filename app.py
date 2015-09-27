#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import os
import subprocess

def main():

    modules = {'pere': "arbre",
        'mere': "arbre",
        'heure': "date",
        'jour': "date"
    }

    str = sys.argv[1]

    if str:
        global list
        find = False
        list = str.split()


        for keys in modules:
            for words in list:
                if findWord(keys)(words):
                    exec(modules[keys]+"(\"{0}\")".format(keys))
                    find = True

                if not find:
                    os.system("sudo echo 'désolée, je ne possède pas la bibliothèque requise pour vous répondre. Souhaitez-vous que jeffectue une recherche sur Internet ?' > ./file/rep")

#######################################################################################################################################################################

def findWord(word):
	return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

def findName(name):
	return re.compile(r'\b^({0})$\b'.format(name), flags=re.IGNORECASE).search

def arbre(key):

    mod = "./lib/arbre.pl"
    file = "./file/nameM"
    i = 0

    while i < 2:
        if searchInFile(file):
            os.system("sudo python engine.py " + mod + " " + key + " " + name + " > ./file/rep")
            i = 2
        else:
            file = "./file/nameF"

        i += 1

def date(key):

    if key == "heure":
        str = subprocess.check_output("date +%k:%M", shell=True)
                
        time = str.split(":")
        heure = int(time[0])
        min = int(time[1])

        if min == 00:
            res = "pile"
        elif min == 15:
            res = "et quart"
        elif min == 30:
            res = "et demi"
        else:
            res = "{0}".format(min)

        if heure == 0:
            res = "il est minuit " + res
        elif heure ==1:
            res = "il est une heure " + res
        elif heure == 12:
            res = "il est midi " + res
        else:
            res = ("il est {0} heure {1}".format(heure,min))
            
    else:
        str = subprocess.check_output("date", shell=True)
        date = str.split()
        res = "Nous somme le " + date[0] + " " + date[1] + " " + date[2] + " " + date[3]

    os.system("sudo echo '" + res + "' > ./file/rep")
                
def searchInFile(file):

    global name
    find = False

    for line in open(file,"r"):
        for word in list:
            if findName(word)(line):
                name = word
                find = True
                break

    return find

##########################################################################################################################################################################

if __name__ == "__main__":
    main()