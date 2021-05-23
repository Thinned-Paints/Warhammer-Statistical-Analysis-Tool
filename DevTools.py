
"""
This is a toolbox, used for testing and generally toying with the code, ideally, none of this will be used in the final
version.
"""
import Dice
import Shooting
from Weapons import *
from Models import *
from Units import *
from copy import copy
import random as r

uids = []
def uidgen(self):
    global uids
    nuid = (len(uids)+1)
    uids.append(nuid)
    return nuid

def passvalue(self):
    bcopy = copy(self)
    return bcopy

def setmelee(self):
    for x in self.models:
        for y in x.weapons:
            if y.type == "Melee":
                y.shots = x.attacks

#This is the hand of god, it sets a model to 0 wounds, no exceptions.
def handofgod(model):
    model.wounds = 0
    return model

#This slaps someone with a single bolter shot
def bolterslap(target,board):
    bolterguy = Units.boltsniper(None)
    Shooting.unitfire(bolterguy, target, board)

def getsquad(model,board):
    uid = model.uid



# TODO: This function should convert from imperial to metric and vice versa
    """
    def convert(measurement,presentunit,newunit):

        metric = ["cm","mt","mm"]
        imperial = ["in","ft"]

        if presentunit in metric:
            if newunit in imperial:
                if newunit == "in":
                    if presentunit == "cm":
                        measurement = (measurement*2.54)
    """
