import copy
from Types import *
from Dice import *
'''
Casualties are an important part of the game, whenever a model is reduced to 0 wounds, it is dead and removed from play.
When a squad loses all its models, it is considered dead for the purposes of the game.
'''
class casualties:

    '''
    This runs through everything on the board, checking for any models at 0 wounds, and killing them.
    Whilst comprehensive, it is inefficient.
    '''
    def casualtycheck(board):
        logging = False
        for x in board.armies:
            for u in x.units:
                if len(u.models)>0:
                    for z in u.models:
                        casualties.smolcasualtycheck(z,board)
                if len(u.models)<=0:
                    casualties.tabledcheck(x)
                    u = None

    '''
    This is a much lighter version of the casualty checker, although it can only kill a single model at a time and has
    no ability to search.
    '''

    def smolcasualtycheck(model,board):
        uid = model.uid
        if model.wounds <= 0:
            for army in board.armies:
                for unit in army.units:
                    for unitmodel in unit.models:
                        if unitmodel.uid==uid:
                            casualties.kill(model,unit)








    '''This is a bit fiddly, but I am basing the casualties off of points values, as the most expensive model in the 
    squad should probably die first, in the rules the player decides, but there's no player here so I'll make do.'''
    def allocatewounds(unit, weapon, wounds):
        for x in range(1,wounds):
            if unit.models[0]:
                casualties.saves(unit.models[0],weapon,1)
            else:
                pass

    def tabledcheck(army):
        tabled = True
        for unit in army.units:
            if len(unit.models)>0:
                tabled = False
        if(tabled):
            return tabled

        return tabled
    deploymentunits = []


    def morale(board):
        '''
        This takes a sample of the board at the start of the turn, and the board now, and if you've lost enough models
        to trigger morale, then it will roll morale for you and apply the results.
        '''
        logging = False
        oldboard = board.prevboard
        pboard = oldboard
        firstboard = None
        global deploymentunits

        while firstboard==None:
            if pboard.turn == 1:
                firstboard = pboard
            if pboard.turn !=1:
                pboard = pboard.prevboard

        originalunits = []

        for x in firstboard.armies:
            for y in x.units:
                originalunits.append(y)

        for x in board.armies:
            for y in x.units:
                for z in oldboard.armies:
                    for a in z.units:
                        if a.uid==y.uid:
                            if len(y.models)<len(a.models):
                                dif = len(a.models)-len(y.models)
                                moraledie = die()
                                if moraledie==1:
                                    pass

                                elif (moraledie+dif)>y.currentleadership:
                                    understrength = False
                                    for x in originalunits:
                                        if x.uid == y.uid:
                                            if (len(x.models)/2)>len(y.models):
                                                understrength = True
                                    for k in y.models:
                                        d = die()
                                        if understrength:
                                            if d>=2:
                                                if logging:
                                                    print("Understrength")
                                                    print("Killed : ",k.name)
                                                casualties.kill(k,a)
                                        if d==1:
                                            if logging:
                                                print("Killed : ", k.name)
                                            casualties.kill(k,a)






    '''
    Whenever a model takes damage, it is allowed to make a saving throw before said damage is actually taken from its
    wounds, there are two types of save, for now I will be using armour saves, however I will get invunerable saves
    working eventually.
    '''

    def saves(unit,weapon,shotnumber):
        mod = 0
        logging = False
        saves = rolldice(shotnumber)

        if len(unit.models)<1:
            return
        for x in saves:
            if unit.models:
                if(len(unit.models)<mod):
                    mod= len(unit.models)
                try:
                    model = unit.models[mod]
                except:
                    pass
                    #print("Breaking")
                if weapon.AP<0:
                    AP = abs(weapon.AP)
                else:
                    AP = weapon.AP

                actualsave = (model.save + AP)
                invun = casualties.calcinvun(model)

                if invun<actualsave:
                    actualsave = invun

                if (model.save<=3):
                    if weapon.modifier:
                        if weapon.modifier[0]=="Grav":
                                weapon.damage = 2

                if x <= actualsave:
                    model.wounds -= weapon.damage

                    if model.wounds <=0:
                        casualties.kill(model,unit)
                        try:
                            mod += 1
                        except:
                            try:
                                mod==0
                            except:
                                pass

                    if model.wounds <0 and logging:
                        print("\n \n Negative wounds \n \n")


                    if logging:
                        print("Save failed, ",weapon.damage," damage was inflicted")
                        print("Wounds are now", model.wounds)
                else:
                    if logging:
                        print("Save passed")

                #This undoes the grav modifier, just so you don't end up with a permenant 2 damage grav weapon, which would
                #be a significant bug.
                if weapon.modifier:
                    if weapon.modifier[0] == "Grav":
                        weapon.damage = 1

    def kill(model,unit):
        uid = model.uid
        newmodels = []

        for model in unit.models:
            if model.uid != uid:
                newmodels.append(model)

        unit.models = newmodels



    def calcinvun(model):
        invun = 7
        wargearlist = model.wargear

        for x in wargearlist:
            for y in x.modifier:
                #This is looking for any piece of wargear that could confer an invun, such as a storm shield
                if y[0] == "I":
                    invun = y[1]

        abilitylist = model.abilities

        for x in abilitylist:
            if x == "Aegis of the Emperor":
                if invun>4:
                    invun=4

        return invun
