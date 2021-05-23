'''
This class will handle all the shooting mechanics, so reading from profiles to throw the correct dice, hopefully.
'''
import math

import Dice
from Casualties import casualties
from Modifiers import *
from DevTools import *
import copy


def shoot(model, targetunit, gun, modifier,board):
    logging = True

    target = targetunit.models[0]
    if logging:
        print(model.name, " is shooting at: ", targetunit.name, " with: ",gun.name)

    if gun.modifier:
        if gun.modifier[0]=="2sv" and targetunit.models[0].keywords[0]=="Vehicle":
            gun.shots=2
    shotroll = Dice.rolldice(gun.shots)
    if gun.modifier:
        if gun.modifier[0]=="2sv":
            gun.shots=1
    if logging:
        for x in shotroll:
            if logging:
                print("Rolled a: ", x)

    hits = []
    explode = False
    gtht = False
    for die in shotroll:
        if getshot(gun):
            gtht = True
            if die==1:
                explode = True
                model.wounds = 0
                if logging:
                    print("Exploded on 1")
                casualties.smolcasualtycheck(model,board)

        if (not explode)and gtht and logging:
            print("Didn't get hot")

        bs = model.bs + modifier
        if logging:
            print("BS:",bs,"\nM:",modifier)

        if die >= bs:
            hits.append(die)
            if gun.modifier:
                if gun.modifier[0]=="Flamer":
                    hits.append(die)

        if gun.modifier:
            if gun.modifier[0]=="Blast" and len(targetunit.models)>5:
                while(len(hits)<3):
                    hits.append(Dice.die())

    shotroll = hits

    if logging:
        print("Out of ", gun.shots, " shots, ", len(shotroll), " hit")

    if len(shotroll) > 0:
        woundroll = Dice.rolldice(len(shotroll))
        towound = None
        if logging:
            print(gun.strength, " ", target.toughness)

        if gun.strength == target.toughness:
            towound = 4
        if gun.strength > target.toughness:
            towound = 3
        if gun.strength >= (target.toughness * 2):
            towound = 2
        if gun.strength < target.toughness:
            towound = 5
        if gun.strength <= (math.ceil(target.toughness / 2)):
            towound = 6

        if logging:
            print("Wounding on a: ", towound)
        for x in woundroll:
            if x < towound:
                woundroll.remove(x)
                if logging:
                    print("Wound failed with a:", x)
            else:
                pass
                if logging:
                    print("Wound scored with a:", x)

        casualties.saves(targetunit, gun, len(woundroll))
    else:
        pass
        # print("MISS")


def InRange(model, target, gun):
    # Measures if a model is in range to fire with a given weapon.
    # Additionally, go watch InRangeTV
    x1 = model.x
    x2 = target.x
    y1 = model.y
    y2 = target.y


    maxrange = (gun.range * 25.4)


    part1 = math.pow((x1 - x2), 2)

    part2 = math.pow((y1 - y2), 2)

    modeldistance = math.sqrt(part1 + part2)

    if (maxrange - modeldistance >= 0):
        return True
    else:
        return False


# print (modeldistance)

def halfrange(model, target, gun):
    halfrangecopy = DevTools.passvalue(gun)
    halfrangecopy.range = halfrangecopy.range / 2
    result = Shooting.InRange(model, target, halfrangecopy)

    if result:
        return True
    else:
        return False



def unitfire(unit, targetunit, board):
    import Shooting
    logging = False
    modifier = 0
    '''
    This function will iterate through a unit, firing their primary weapon's at the target
    The target will be decided by first orgnising the target into a sorted list, by points
    When a model is killed, it'll move to the next cheapest model
    Once all models are killed, the unit will be deleted, and a ping will come back
    saying to stop shooting.
    All further shots will be wasted
    '''
    if logging:
        print(unit.name, "is shooting at ", targetunit.name, "\n")
    if board.phase == "Shooting":
        for model in unit.models:
            if hasmovedheavy(model, board):
                modifier = 1
            else:
                modifier = 0

            if targetunit.models:
                primaryweapon = model.weapons[0]

                if targetunit.models[0]:
                    if (Shooting.InRange(model, targetunit.models[0], primaryweapon)):
                        # print("InRange!")
                        Shooting.shoot(model, targetunit, primaryweapon, modifier, board)
                        # except:
                        # if logging:
                        # print("It threw 'the' error")
                        # break
                    else:
                        if logging:
                            print("Out of range")
                    casualties.casualtycheck(board)
                else:
                    if logging:
                        print("Firing at empty unit")
                    pass
            else:
                break
    else:
        print("You are in ", board.phase, ", you can only fire in the shooting phase")


def hasmovedheavy(markermodel, board):
    logging = False
    if markermodel.weapons[0].type == "Heavy":
        mmcoords = [markermodel.x, markermodel.y]
        prevturnmarkermodel = None
        while prevturnmarkermodel==None:
            for army in board.prevboard.armies:
                for unit in army.units:
                    for model in unit.models:
                        if markermodel.uid==model.uid:
                            prevturnmarkermodel=model
                            break

        #if board.turn==2:
            #print("Its happening")
        if prevturnmarkermodel!=None:
            ptmmcoords = [prevturnmarkermodel.x,prevturnmarkermodel.y]
            if ptmmcoords==mmcoords:
                if logging:
                    print("Not moved heavy")
                return False
            if ptmmcoords!=mmcoords:
                if logging:
                    print("Has moved heavy")
                return True

    return False

def getshot(gun):

    for attribute in gun.modifier:
        if attribute == "Getshot":
            return True

    return False