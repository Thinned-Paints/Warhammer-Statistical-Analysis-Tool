import Dice
import DevTools
from Casualties import casualties

"""This is a pool of modifiers, any modifiers you want to add, you have to create something that can actually do their
effects here."""
#TODO: Test these
class modifiers:

    def rerollone(dicepool):
        for x in dicepool:
            if x==1:
                x = Dice.die()
        return dicepool

    def rapidfire(dicepool):
        dicepool2 = Dice.rolldice(len(dicepool))
        dicepool +=dicepool2
        return dicepool

    def flamer(dicepool):
        for x in dicepool:
            x = 7
        return dicepool

    def grav(weapon):
        weapon.damage = 2
        return weapon

    def d6blast(weapon):
        weapon.shots = 6
        return weapon

    def d3blast(weapon):
        weapon.shots = 3
        return weapon

    def getshot(dicepool,model):
        for x in dicepool:
            if x==1:
                model.wounds -=1
                casualties.smolcasualtycheck(model)

    def variableshotsd3(weapon):
        weapon.shots = Dice.d3()

    def variableshotsd6(weapon):
        weapon.shots = Dice.die()

    def variabledamaged3(weapon):
        weapon.damage = Dice.d3()

    def variabldamaged6(weapon):
        weapon.damage = Dice.die()
