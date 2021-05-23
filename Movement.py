import copy
import math
from DevTools import *
class movement:
    playspace = []
    def maxmove(unit,angle):
        # THIS ONE
        try:
            mod = 0
            looping = True
            while looping:
                model = unit.models[mod]
                maxdist = model.movement
                looping = True
                movement.move(model, maxdist, angle)
                if mod<len(unit.models):
                    mod+=1
                else:
                    looping=False

        except:
            pass

    def move(model, distance, angle):
        maxdist = model.movement*25.4
        distance = distance*25.4

        if distance > maxdist:
            distance = DevTools.passvalue(maxdist)

        radAngle = math.radians(angle)

        model.x = model.x + (distance * math.cos(radAngle))
        model.y = model.y + (distance * math.sin(radAngle))
        movement.collision(model)

    xbound = 0
    ybound = 0
    def setbounds(board):
        global xbound
        xbound = board.x
        global ybound
        ybound = board.y
    def collision(model):
        global xbound
        global ybound
        if model.x >= xbound:
            print("Top Collision")
            model.x = xbound-model.base

        if model.x <= 0:
            print("Bottom Collision")
            model.x = 25


        if model.y >= ybound:
            print("Right Collision")
            model.y = 1779

        if model.y <= 0:
            print("Left Collision")
            model.y = 25


    def unitmove(unit, distance, angle):
        for x in unit.models:
            movement.move(x,distance,angle)

    def advance(unit, angle):
        #Take a copy of their original movement
        ogmove = copy.deepcopy(unit.models[0],movement)

        #Roll a D6, add to their base movement
        advdie = Dice.die()
        for x in unit.models:
            x.movement = ogmove + (advdie)

        #Move with the new extended movement
        movement.maxmove(unit, angle)

        #Return their movement to original
        for x in unit.models:
            x.movement = ogmove


    def placemodel(model,x,y):
        model.xc = int(x)
        model.y = int(y)

    def linedeploy(startposition, unit):
        sx = startposition[0]
        sy = startposition[1]
        c=0

        for x in unit.models:

            x.y = sy
            x.xc = (sx+x.basesize+c)
            c+=25.4


