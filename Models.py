"""
A model is a single man/woman/alien/gribbly, there are many of them in the game, and they're fundamental to the game
Here's some of my models, if you want an idea of what some of them look like:
https://imgur.com/a/uBQFtkZ
"""

from Types import *
from Weapons import *
from Wargear import *

class Model:

    def TacticalMarine(self):

        bolter = Weapon.Boltgun(None)
        fists = Weapon.Fists(None)
        boltpistol = Weapon.BoltPistol(None)
        name = "Tactical Marine"
        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [bolter, boltpistol,fists]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ["Imperium","Adeptus Astartes","Carcharodons"]
        keywords = ["Core","Troops"]
        points = (18+bolter.points+boltpistol.points)
        power = 0
        role = "Troop"
        base = "Circle"
        basesize = 32
        x = int()
        y = int()

        TacticalMarine = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )
        return TacticalMarine

    def PlasmaTactical(self):

        plasmagun = Weapon.Plasmagun(None)
        fists = Weapon.Fists(None)
        boltpistol = Weapon.BoltPistol(None)
        name = "Plasma Tactical"
        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [plasmagun, boltpistol,fists]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ["Imperium","Adeptus Astartes","Carcharodons"]
        keywords = ["Core","Troops"]
        points = (18+plasmagun.points+boltpistol.points)
        power = 0
        role = "Troop"
        base = "Circle"
        basesize = 32
        x = int()
        y = int()

        TacticalMarine = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )
        return TacticalMarine



    def TacticalSergeant(self):

        bolter = Weapon.Boltgun(None)
        plasmapistol = Weapon.PlasmaPistol(None)
        chainsword = Weapon.Chainsword(None)


        name = "Tactical Sergeant"
        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 2
        leadership = 8
        save = 3
        weapons = [bolter, plasmapistol, chainsword]

        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ["Imperium", "Adeptus Astartes", "Carcharodons"]
        keywords = ["Core", "Troops"]
        points = (18+bolter.points+plasmapistol.points+chainsword.points)
        power = 0
        role = "Troop"
        base = "Circle"
        basesize = 28
        x = int
        y = int

        TacticalSergeant = model(
            name,movement,ws,bs,strength,toughness,wounds,attacks,leadership,save,weapons,wargear,abilities,
            activeabilities, factionkeywords,keywords,points,power,role, base, basesize, x, y
        )
        return (TacticalSergeant)

    def predator(self):
        RightHeavyBolter = Weapon.HeavyBolter(None)
        LeftHeavyBolter = Weapon.HeavyBolter(None)
        PredatorAutoCannon = Weapon.predatorautocannon(None)

        name = "Predator"
        movement = 12
        ws = 3
        bs = 3
        strength = 6
        toughness = 7
        wounds = 11
        attacks = 3
        leadership = 8
        save = 3
        weapons = [RightHeavyBolter,LeftHeavyBolter,PredatorAutoCannon]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ["Imperium", "Adeptus Astartes", "Carcharodons"]
        keywords = ["Vehicle","Heavy Support"]
        points = (70+RightHeavyBolter.points+LeftHeavyBolter.points+PredatorAutoCannon.points)
        power = 8
        role = "Heavy Support"
        base = "rectangle"
        basesize = 100
        x = None
        y = None

        Predator = model(
            name,movement,ws,bs,strength,toughness,wounds,attacks,leadership,save,weapons,wargear,abilities,
            activeabilities, factionkeywords,keywords,points,power,role, base, basesize, x, y
        )
        return Predator


    def HBDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        HeavyBolter = Weapon.HeavyBolter(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "HBDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [HeavyBolter,BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry','Core','Heavy Support']
        points = (18+HeavyBolter.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        HBDevestator = model(
            name,movement,ws,bs,strength,toughness,wounds,attacks,leadership,save,weapons,wargear,abilities,
            activeabilities, factionkeywords,keywords,points,power,role, base, basesize, x, y
        )
        return HBDevestator

    def LCDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        Lascannon = Weapon.mLascannon(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "LCDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [Lascannon, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + Lascannon.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        LCDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return LCDevestator

    def HFDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        HeavyFlamer = Weapon.heavyflamer(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "HFDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [HeavyFlamer, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + HeavyFlamer.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        HFDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return HFDevestator

    def GCDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        GravCannon = Weapon.mgravcannon(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "GCDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [GravCannon, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + GravCannon.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        GCDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return GCDevestator

    def FMDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        FragMissile = Weapon.mMissilelauncherfrag(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "FMDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [FragMissile, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + FragMissile.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        FMDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return FMDevestator

    def KMDevestator(self):

        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        KrakMissile = Weapon.mMissilelauncherkrak(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "KMDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [KrakMissile, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + KrakMissile.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        KMDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return KMDevestator

    def MMDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        MultiMelta = Weapon.mMultimelta(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "MMDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [MultiMelta, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + MultiMelta.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        MMDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return MMDevestator

    def PCDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        PlasmaCannon = Weapon.plasmacannonhigh(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "PCDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [PlasmaCannon, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + PlasmaCannon.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        PCDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return PCDevestator

    def LPCDevestator(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        PlasmaCannon = Weapon.Plasmacannonlow(None)
        BoltPistol = Weapon.BoltPistol(None)

        name = "LPCDevestator"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 1
        leadership = 7
        save = 3
        weapons = [PlasmaCannon, BoltPistol]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18 + PlasmaCannon.points)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        LPCDevestator = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return LPCDevestator

    def boltsniper(self):
        bolter = Weapon.Boltgun(None)
        name = "Boltsniper"
        movement = 6
        ws = -1
        bs = -1
        strength = 4
        toughness = 4
        wounds = 1
        attacks = 2
        leadership = 8
        save = 7

        weapons = [bolter]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ["Imperium"]
        keywords = ["Core", "Elite"]
        points = (999 + bolter.points)
        power = 0
        role = "Elite"
        base = "Circle"
        basesize = 28
        x = 69
        y = 69

        boltsniper = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return (boltsniper)
    def DevestatorSGT(self):
        '''
        Bolt Pistol
        Main Gun
        Default marine profile
        '''
        Bolter = Weapon.Boltgun(None)
        Chainsword = Weapon.Chainsword(None)

        name = "DevestatorSGT"

        movement = 6
        ws = 3
        bs = 3
        strength = 4
        toughness = 4
        wounds = 2
        attacks = 2
        leadership = 8
        save = 3
        weapons = [Bolter, Chainsword]
        wargear = []
        abilities = ['Signum']
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Infantry', 'Core', 'Heavy Support']
        points = (18)
        power = 0
        role = 'Heavy Support'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        DevestatorSGT = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return DevestatorSGT
    def landspeeder(self):
        '''
        Heavy bolter only
        '''

        name = "LandSpeeder"
        Heavybolter = Weapon.HeavyBolter(None)
        movement = 16
        ws = 3
        bs = 3
        strength = 4
        toughness = 5
        wounds = 6
        attacks = 2
        leadership = 7
        save = 3
        weapons = [Heavybolter]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodons']
        keywords = ['Vehicle', 'Fly', 'Fast Attack']
        points = (45)
        power = 6
        role = 'Fast Attack'
        base = 'Circle'
        basesize = 32
        x = None
        y = None

        LandSpeeder = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return LandSpeeder

    def custodianGuard(self):
        '''
        Spear
        Miserecordia
        Custode statline
        '''
        guardianSpear = Weapon.guardianSpear(None)
        guardianSpearMelee = Weapon.guardianSpearMelee(None)
        misericordia = Weapon.Misericordia(None)


        name = "Custodian Guard"

        movement = 6
        ws = 2
        bs = 2
        strength = 5
        toughness = 5
        wounds = 3
        attacks = 3
        leadership = 8
        save = 2
        weapons = [guardianSpear, guardianSpearMelee, misericordia]
        wargear = []
        abilities = ['Aegis of the Emperor','Invun 5']
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Custodes', 'Carcharodons']
        keywords = ['Infantry', 'Custodian Guard']
        points = (45)
        power = 0
        role = 'Troops'
        base = 'Circle'
        basesize = 40
        x = None
        y = None

        custodianGuard = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return custodianGuard


    def GuardSergeant(self):
        '''Plain and simple, cannon fodd-, I mean uh, the Emperors finest '''

        lasgun = Weapon.lasgun(None)

        name = "Sergeant"
        movement = 6
        ws = 4
        bs = 4
        strength = 3
        toughness = 3
        wounds = 1
        attacks = 2
        leadership = 7
        save = 5
        weapons = [lasgun]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Astra Militarum', 'Cadian']
        keywords = ['Infantry', 'Troop']
        points = 5
        power = 0
        role = 'Troops'
        base = 'Circle'
        basesize = 28
        x = None
        y = None

        Sergeant = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return Sergeant


    def Guardsman(self):
        '''Plain and simple, cannon fodd-, I mean uh, the Emperors finest '''

        lasgun = Weapon.lasgun(None)

        name = "Guardsman"
        movement = 6
        ws = 4
        bs = 4
        strength = 3
        toughness = 3
        wounds = 1
        attacks = 1
        leadership = 6
        save = 5
        weapons = [lasgun]
        wargear = []
        abilities = []
        activeabilities = []
        factionkeywords = ['Imperium', 'Astra Militarum', 'Cadian']
        keywords = ['Infantry', 'Troop']
        points = 5
        power = 0
        role = 'Troops'
        base = 'Circle'
        basesize = 28
        x = None
        y = None

        Guardsman = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return Guardsman

    def landraider(self):

        lascannon1 = Weapon.Lascannon(None)
        lascannon2 = Weapon.Lascannon(None)
        lascannon3 = Weapon.Lascannon(None)
        lascannon4 = Weapon.Lascannon(None)
        heavybolter1 = Weapon.HeavyBolter(None)
        heavybolter2 = Weapon.HeavyBolter(None)
        smokelaunchers = Wargear.smokelaunchers(None)

        name = "Land Raider"
        movement = 10
        ws = 6
        bs = 3
        strength = 8
        toughness = 8
        wounds = 16
        attacks = 6
        leadership = 9
        save = 2
        weapons = [lascannon1,lascannon2,lascannon3,lascannon4,heavybolter1,heavybolter2]
        wargear = [smokelaunchers]
        abilities = ["Angels Of Death","Explodes","Transport 10","Degrading:[8:BS'4',A'D6'],[4:BS'5',A'D3']"]
        activeabilities = []
        factionkeywords = ['Imperium', 'Adeptus Astartes', 'Carcharodon']
        keywords = ['Vehicle', 'Transport', 'Machine Spirit', 'Smokescreen','Land Raider']
        points = 285
        power = 15
        role = 'Troops'
        base = 'Circle'
        basesize = 160
        x = None
        y = None

        landraider = model(
            name, movement, ws, bs, strength, toughness, wounds, attacks, leadership, save, weapons, wargear, abilities,
            activeabilities, factionkeywords, keywords, points, power, role, base, basesize, x, y
        )

        return landraider