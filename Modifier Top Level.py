from Modifiers import *
from Shooting import *
class conditionals:

    def rerollone(ability,dicepool,model,target,board):
        pass

    def rapidfire(ability,dicepool,model,target,board):
        #If a rapid fire weapon is within half of it's max rangem, it fires twice as many shots
        gun = model.weapon[0]
        range = gun.range
        if gun.type =="Rapid Fire":
            if Shooting.halfrange(model, target, model.weapons[0]):
                dicepool = modifiers.rapidfire(dicepool)
                return (ability,dicepool,model,target,board)

    x = [(rapidfire(),"rapidfire"),(rerollone(),"rerollone")]
