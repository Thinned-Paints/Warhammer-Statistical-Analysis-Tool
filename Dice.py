from __future__ import absolute_import
from random import randrange
import sys

sys.path.append(".")

'''
These do exactly what they say on the tin, one rolls a single die, the other returns an array of dice.
'''
def die():
    x = randrange(1,7)

    return int(x)

def d3():
    x = randrange(1,4)
    return int(x)

def rolldice(pool):

    dicepool = []
    for x in range(0,pool):
        dicepool.append(die())

    return dicepool
