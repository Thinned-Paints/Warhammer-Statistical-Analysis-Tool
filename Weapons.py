"""
This sets up all the weapons.
the switcher function needs replacing with a switchcase, based on a bastardised dictionary
"""
import Dice
from Types import weapon

class Weapon:

    def none(self):
        pass

    def Fists(self):
        fists = Weapon()
        fists.type = "Melee"
        fists.range = 1
        fists.shots = 1
        fists.strength = 1
        fists.AP = 0
        fists.damage = 1
        fists.modifier = []
        fists.givetoken = ""
        fists.name= "Fists"
        fists.points = 0
        fists.power = 0
        return fists

    def Boltgun(self):
        boltgun = Weapon()
        boltgun.type = "Rapid Fire"
        boltgun.range = 24
        boltgun.shots = 2
        boltgun.strength = 4
        boltgun.AP = 0
        boltgun.damage = 1
        boltgun.modifier = []
        boltgun.givetoken = ""
        boltgun.name = "Boltgun"
        boltgun.points = 0
        boltgun.power = 0
        return boltgun

    def lasgun(self):
        lasgun = Weapon()
        lasgun.type = "Rapid Fire"
        lasgun.range = 24
        lasgun.shots = 1
        lasgun.strength = 3
        lasgun.AP = 0
        lasgun.damage = 1
        lasgun.modifier = []
        lasgun.givetoken = ""
        lasgun.name = "Lasgun"
        lasgun.points = 0
        lasgun.power = 0
        return lasgun

    def Plasmagun(self):
        Plasmagun = Weapon()
        Plasmagun.type = "Rapid Fire"
        Plasmagun.range = 24
        Plasmagun.shots = 2
        Plasmagun.strength = 8
        Plasmagun.AP = 3
        Plasmagun.damage = 2
        Plasmagun.modifier = ["Getshot"]
        Plasmagun.givetoken = ""
        Plasmagun.name = "Plasmagun"
        Plasmagun.points = 10
        Plasmagun.power = 0
        return Plasmagun


    def Chainsword(self):
        chainsword = Weapon()
        chainsword.type = "Melee"
        chainsword.range = 1
        chainsword.shots = 1
        chainsword.strength = 1
        chainsword.AP = -1
        chainsword.damage = 1
        chainsword.modifier = []
        chainsword.givetoken = ""
        chainsword.name = "Chainsword"
        chainsword.points = 0
        chainsword.power = 0
        return chainsword

    def BoltPistol(self):
        boltpistol = Weapon()
        boltpistol.type = "Pistol"
        boltpistol.range = 12
        boltpistol.shots = 1
        boltpistol.strength = 4
        boltpistol.AP = 0
        boltpistol.damage = 1
        boltpistol.modifier = []
        boltpistol.givetoken = ""
        boltpistol.name = "Boltpistol"
        boltpistol.points = 0
        boltpistol.power = 0
        return boltpistol

    def PlasmaPistol(self):
        plasmapistol = Weapon()
        plasmapistol.type = "Pistol"
        plasmapistol.range = 12
        plasmapistol.shots = 1
        plasmapistol.strength = 8
        plasmapistol.AP = -3
        plasmapistol.damage = 2
        plasmapistol.modifier = ["Getshot"]
        plasmapistol.givetoken = ""
        plasmapistol.name = "Plasma Pistol"
        plasmapistol.points = 5
        plasmapistol.power = 0
        return plasmapistol

    def HeavyBolter(self):
        heavybolter = Weapon()
        heavybolter.type = "Heavy"
        heavybolter.range = 36
        heavybolter.shots = 3
        heavybolter.strength = 5
        heavybolter.AP = -1
        heavybolter.damage = 2
        heavybolter.modifier = []
        heavybolter.givetoken = ""
        heavybolter.name = "Heavy Bolter"
        heavybolter.points = 10
        heavybolter.power = 0
        return heavybolter

    def Lascannon(self):
        lascannon = Weapon()
        lascannon.type = "Heavy"
        lascannon.range = 48
        lascannon.shots = 1
        lascannon.strength = 9
        lascannon.AP = -3
        lascannon.damage = Dice.die()
        lascannon.modifier = []
        lascannon.givetoken = ""
        lascannon.name = "Lascannon"
        lascannon.points = 15
        lascannon.power = 0
        return lascannon

    def mLascannon(self):
        lascannon = Weapon()
        lascannon.type = "Heavy"
        lascannon.range = 48
        lascannon.shots = 1
        lascannon.strength = 9
        lascannon.AP = -3
        lascannon.damage = (3 + Dice.d3())
        lascannon.modifier = []
        lascannon.givetoken = ""
        lascannon.name = "Modified Lascannon"
        lascannon.points = 15
        lascannon.power = 0
        return lascannon

    def Multimelta(self):
        multimelta = Weapon()
        multimelta.type = "Heavy"
        multimelta.range = 24
        multimelta.shots = 2
        multimelta.strength = 8
        multimelta.AP = -4
        multimelta.damage = Dice.die()
        multimelta.modifier = ["melta"]
        multimelta.name = "Multi-Melta"
        multimelta.points = 20
        multimelta.power = 0
        return multimelta

    def mMultimelta(self):
        multimelta = Weapon()
        multimelta.type = "Heavy"
        multimelta.range = 24
        multimelta.shots = 1
        multimelta.strength = 8
        multimelta.AP = -4
        multimelta.damage = Dice.die()
        multimelta.modifier = ["2sv","melta"]
        multimelta.name = "Modified Multi-Melta"
        multimelta.points = 20
        multimelta.power = 0
        return multimelta

    def Missilelauncherfrag(self):
        missilelauncherfrag = Weapon()
        missilelauncherfrag.type = "Heavy"
        missilelauncherfrag.range = 48
        missilelauncherfrag.shots = Dice.die()
        missilelauncherfrag.strength = 4
        missilelauncherfrag.AP = 0
        missilelauncherfrag.damage = 1
        missilelauncherfrag.modifier = ["Blast"]
        missilelauncherfrag.name = "Missile-Launcher-Frag"
        missilelauncherfrag.points = 15
        missilelauncherfrag.power = 0
        return missilelauncherfrag

    def mMissilelauncherfrag(self):
        missilelauncherfrag = Weapon()
        missilelauncherfrag.type = "Heavy"
        missilelauncherfrag.range = 48
        missilelauncherfrag.shots = (3 + Dice.d3())
        missilelauncherfrag.strength = 4
        missilelauncherfrag.AP = 0
        missilelauncherfrag.damage = 1
        missilelauncherfrag.modifier = ["Blast"]
        missilelauncherfrag.name = "Modified Missile-Launcher-Frag"
        missilelauncherfrag.points = 15
        missilelauncherfrag.power = 0
        return missilelauncherfrag

    def Missilelauncherkrak(self):
        missilelauncherkrak = Weapon()
        missilelauncherkrak.type = "Heavy"
        missilelauncherkrak.range = 48
        missilelauncherkrak.shots = 1
        missilelauncherkrak.strength = 8
        missilelauncherkrak.AP = -2
        missilelauncherkrak.damage = Dice.die()
        missilelauncherkrak.modifier = []
        missilelauncherkrak.name = "Missile-Launcher-Krak"
        missilelauncherkrak.points = 0
        missilelauncherkrak.power = 0
        return missilelauncherkrak

    def mMissilelauncherkrak(self):
        missilelauncherkrak = Weapon()
        missilelauncherkrak.type = "Heavy"
        missilelauncherkrak.range = 48
        missilelauncherkrak.shots = 1
        missilelauncherkrak.strength = 8
        missilelauncherkrak.AP = -2
        missilelauncherkrak.damage = (Dice.die() + 1)
        missilelauncherkrak.modifier = []
        missilelauncherkrak.name = "Modified Missile-Launcher-Krak"
        missilelauncherkrak.points = 0
        missilelauncherkrak.power = 0
        return missilelauncherkrak


    def Plasmacannonlow(self):
        plasmacannonlow = Weapon()
        plasmacannonlow.type = "Heavy"
        plasmacannonlow.range = 36
        plasmacannonlow.shots = Dice.d3()
        plasmacannonlow.strength = 7
        plasmacannonlow.AP = -3
        plasmacannonlow.damage = 1
        plasmacannonlow.modifier = ["Blast"]
        plasmacannonlow.name = "Plasma Cannon Low"
        plasmacannonlow.points = 15
        plasmacannonlow.power = 0
        return plasmacannonlow

    def plasmacannonhigh(self):
        plasmacannonhigh = Weapon()
        plasmacannonhigh.type = "Heavy"
        plasmacannonhigh.range = 36
        plasmacannonhigh.shots = 2
        plasmacannonhigh.strength = 8
        plasmacannonhigh.AP = -3
        plasmacannonhigh.damage = 2
        plasmacannonhigh.modifier = ["Blast", "Getshot"]
        plasmacannonhigh.name = "Plasma Cannon High"
        plasmacannonhigh.points = 0
        plasmacannonhigh.power = 0
        return plasmacannonhigh

    def gravcannon(self):
        gravcannon = Weapon()
        gravcannon.type = "Heavy"
        gravcannon.range = 30
        gravcannon.shots = 4
        gravcannon.strength = 5
        gravcannon.AP = -1
        gravcannon.damage = 1
        gravcannon.modifier = ["Grav"]
        gravcannon.name = "Gravcannon"
        gravcannon.points = 10
        gravcannon.power = 0
        return gravcannon

    def mgravcannon(self):
        gravcannon = Weapon()
        gravcannon.type = "Heavy"
        gravcannon.range = 20
        gravcannon.shots = 3
        gravcannon.strength = 4
        gravcannon.AP = -1
        gravcannon.damage = 1
        gravcannon.modifier = ["Grav"]
        gravcannon.name = "Modified Gravcannon"
        gravcannon.points = 10
        gravcannon.power = 0
        return gravcannon

    def predatorautocannon(self):
        predatorautocannon = Weapon()
        predatorautocannon.type = "Heavy"
        predatorautocannon.range = 48
        predatorautocannon.shots = (Dice.d3() + Dice.d3())
        predatorautocannon.strength = 7
        predatorautocannon.AP = -1
        predatorautocannon.damage = 3
        predatorautocannon.modifier = []
        predatorautocannon.name = "Predator Autocannon"
        predatorautocannon.points = 40
        predatorautocannon.power = 0
        return predatorautocannon

    def heavyflamer(self):
        heavyflamer = Weapon()
        heavyflamer.type = "Heavy"
        heavyflamer.range = 12
        heavyflamer.shots = Dice.die()
        heavyflamer.strength = 5
        heavyflamer.AP = -1
        heavyflamer.damage = 1
        heavyflamer.modifier = ["Flamer"]
        heavyflamer.name = "Heavy Flamer"
        heavyflamer.points = 10
        heavyflamer.power = 0
        return heavyflamer

    def guardianSpear(self):
        guardianSpear = Weapon()
        guardianSpear.type= "Rapid Fire"
        guardianSpear.range = 24
        guardianSpear.shots = 1
        guardianSpear.strength = 4
        guardianSpear.AP = -1
        guardianSpear.damage = 2
        guardianSpear.modifier = []
        guardianSpear.name = "Guardian spear"
        guardianSpear.points = 0
        guardianSpear.power = 0

        return guardianSpear

    def guardianSpearMelee(self):
        guardianSpearMelee = Weapon()
        guardianSpearMelee.type = "Melee"
        guardianSpearMelee.range = 1
        guardianSpearMelee.shots = 1
        guardianSpearMelee.strength = 1
        guardianSpearMelee.AP = -3
        guardianSpearMelee.damage = Dice.d3()
        guardianSpearMelee.modifier = []
        guardianSpearMelee.name = "Guardian spear melee"
        guardianSpearMelee.points = 0
        guardianSpearMelee.power = 0
        return guardianSpearMelee


    def Misericordia(self):

        Miserecordia = Weapon()
        Miserecordia.type = "Melee"
        Miserecordia.range = 1
        Miserecordia.shots = 1
        Miserecordia.strength = 0
        Miserecordia.AP = -2
        Miserecordia.damage = 1
        Miserecordia.modifier = ["AT1"]
        Miserecordia.name = "Misericordia"
        Miserecordia.points = 3
        Miserecordia.power = 0

        return Miserecordia
