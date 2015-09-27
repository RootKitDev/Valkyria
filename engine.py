#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyswip import Prolog
import sys
import os

                                    ############################################################
                                    #             Exemple to use Prolog in Python  	           #
                                    ############################################################
                                    # 	  v1 = what 		                                   #
                                    #     v2 = who					                           #
                                    #      						                               #
                                    # //  e.g v1 = father / v2 = jean -> who is jean's father  #
                                    #	                                                       #
                                    #     prolog = Prolog()                                    #
                                    #     prolog.consult("mod.pl")                             #
                                    #                                                          #
                                    #     for soln in prolog.query("%s(X,%s)" % (v1, v2)):     #
                                    #          print  soln["X"], "est le %s de %s" % (v1, v2)  #
                                    #                                                          #
                                    ############################################################

def main():

    mod = sys.argv[1]
    what = sys.argv[2]
    who = sys.argv[3]
    find = False

    prolog = Prolog()
    prolog.consult(mod)

    for soln in prolog.query("%s(X,%s)" % (what, who)):
        if what == 'pere' :
            print soln["X"], "est le %s de %s" % (what, who)
        else :
            print soln["X"], "est la %s de %s" % (what, who)
        find = True

    if not find:
        print "Je suis désolé, je ne dispose pas des informations requise pour vous répondre. Souhaitez-vous que jeffectue une recherche sur Internet"

if __name__ == "__main__":
    main()
