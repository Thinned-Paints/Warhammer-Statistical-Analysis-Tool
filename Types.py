"""
This file defines all the custom types, and some basic functions for displaying the data within those types.
"""


import DevTools
class weapon:
    def __init__(self, type, range, shots, strength, AP, damage, modifier, givetoken, name, points, power):
        self.type = str(type)
        self.range = int(range)
        self.shots = int(shots)
        self.strength = int(strength)
        self.AP = int(AP)
        self.damage = int(damage)
        self.modifier = modifier
        self.givetoken = str(givetoken)
        self.name = str(name)
        self.points = int(points)
        self.power = int(power)

    def dump(self):
        print ("Name: ",self.name," Type: ",self.type," Shots: ",self.shots," Strength: ",self.strength," AP: ",self.AP,
               " Damage: ",self.damage," Modifiers: ",self.modifier,
               " Tokens: ",self.givetoken, " Points: ", self.points," Power: ",self.power)


class wargear:

    def __init__(self, modifier, name, points, power):
        self.modifier = modifier
        self.name = str(name)
        self.points = int(points)
        self.power = int(power)


    def dump(self):
        print("Name: ",self.name," Modifier ref: ",self.modifier," Points: ",self.points," Power: ",self.power)

class model:

    def __init__(self, name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear,
                 abilities,activeabilities, factionkeywords, keywords, points, power, role,base,basesize, xc, yc):
        self.uid = DevTools.uidgen(None)
        self.keywords = keywords
        self.factionkeywords = factionkeywords
        self.abilities = abilities
        self.activeabilities = activeabilities
        self.wargear = wargear
        self.weapons = weapons
        self.y = 0
        self.x = 0
        self.name = str(name)
        self.movement = int(movement)
        self.ws = int(ws)
        self.bs = int(bs)
        self.strength = int(strength)
        self.toughness = int(toughness)
        self.wounds = int(wounds)
        self.attacks = int(attacks)
        self.leadership = int(leadership)
        self.save = int(save)
        self.points = int(points)
        self.power = int(power)
        self.role = str(role)
        self.base = str(base)
        self.basesize = int(basesize)



    def dump(self):
        print("Name: ", self.name," UID: ", self.uid," Movement: ",self.movement," Weapon Skill: ", self.ws," Ballistic Skill: ", self.bs,
              " Strength: ", self.strength," Toughness: ", self.toughness,
             " Wounds: ",self.wounds, " Attacks: ",self.attacks," Leadership: ",self.leadership," Save: ", self.save)

        print(
              "Abilities Refrence: ",
              self.abilities," Faction keywords: ", self.factionkeywords, " Keywords:", self.keywords," Points: ",
              self.points," Power: ",self.power, " Role: ", self.role," ",self.basesize, "mm ",self.base," base")
        print(self.xc," ", self.yc)
        print("Weapons: ")

        for x in self.weapons:
            weapon.dump(x)

        for x in self.wargear:
            wargear.dump(x)

        print("")


class unit:

    def __init__(self, name, points, power, currentleadership,tokens, models):
        self.name = name
        self.points = points
        self.power = power
        self.currentleadership = currentleadership
        self.tokens = tokens
        self.models = []
        self.uid = DevTools.uidgen(None)

    def dump(self):
        print("Unit: ", self.name)
        modcount = 0
        for x in self.models:
            modcount +=1
        print("Points: ", self.points," Power: ", self.power, " Current Leadership: ",
        self.currentleadership," Model Count: ", modcount )
        for x in self.models:
            model.dump(x)

    def litedump(self):
        print("Unit: ",self.name)
        modcount = 0
        names = []
        coordinates = []
        for x in self.models:
            modcount +=1
            names.append(x.name)
            mc = [x.xc, x.y]
            coordinates.append(mc)
        print("There are ",modcount," models remaining")

        print("The models are:", end="", flush=True)
        for x in names:
            if names[-1] == x:
                print(x,"", end="\n", flush=True)
            else:
                print(x, ",", end="", flush=True)


        print("Coordinates of the squad are:",end="",flush=True)
        for x in coordinates:
            if coordinates[-1] == x:
                print(x,end="\n\n", flush=True)
            else:
                print(x,end=",",flush=True)



class army:

    def __init__(self,units,modifiers,faction,ID):
        self.units = units
        self.modifiers = modifiers
        self.faction = faction
        self.ID = ID

    def dump(self):
        print("ID is: ",self.ID," Name is: ", self.faction)
        print("Modifiers are: ")
        for x in self.modifiers:
            print (x)

        print("Units are:")
        for x in self.units:
            unit.dump(x)

class terrain:

    def __init__(self,name,x,y,keywords,rules):
        self.name = name
        self.x= x
        self.y= y
        self.keywords = keywords
        self.rules = rules

    def dump(self):

        print("Name: ",self.name)
        print("Size is ", self.x)



