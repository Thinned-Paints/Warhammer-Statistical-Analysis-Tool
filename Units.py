"""
Units are a custom type, containing a collection of models, often with diffrent model types in there.
They're fiddly.
"""

from DevTools import DevTools
from Types import *
from Wargear import *
from Weapons import *
from Models import *


class Units:

    def LCannonDevs(self):

        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.LCDevestator(None)
        devestator2 = Model.LCDevestator(None)
        devestator3 = Model.LCDevestator(None)
        devestator4 = Model.LCDevestator(None)

        name = "LasCannon Devestators"
        LCDevs = unit(name, 0, 0, 0, 0, 0)

        LCDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in LCDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        LCDevs.currentleadership = ld
        LCDevs.points = p
        LCDevs.power = bp
        if mno == 10:
            LCDevs.power += 4

        return LCDevs

    def MMDevs(self):

        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.MMDevestator(None)
        devestator2 = Model.MMDevestator(None)
        devestator3 = Model.MMDevestator(None)
        devestator4 = Model.MMDevestator(None)

        name = "Multimelta Devestators"
        MMDevs = unit(name, 0, 0, 0, 0, 0)

        MMDevs.models = [devestator1, devestator2, devestator3, devestator4, devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in MMDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        MMDevs.currentleadership = ld
        MMDevs.points = p
        MMDevs.power = bp
        if mno == 10:
            MMDevs.power += 4

        return MMDevs


    def KMDevs(self):

        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.KMDevestator(None)
        devestator2 = Model.KMDevestator(None)
        devestator3 = Model.KMDevestator(None)
        devestator4 = Model.KMDevestator(None)

        name = "Krak Missile Devestators"
        KMDevs = unit(name, 0, 0, 0, 0, 0)

        KMDevs.models = [devestator1, devestator2, devestator3, devestator4, devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in KMDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        KMDevs.currentleadership = ld
        KMDevs.points = p
        KMDevs.power = bp
        if mno == 10:
            KMDevs.power += 4

        return KMDevs

    def FMDevs(self):

        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.FMDevestator(None)
        devestator2 = Model.FMDevestator(None)
        devestator3 = Model.FMDevestator(None)
        devestator4 = Model.FMDevestator(None)

        name = "Krak Missile Devestators"
        FMDevs = unit(name, 0, 0, 0, 0, 0)

        FMDevs.models = [devestator1, devestator2, devestator3, devestator4, devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in FMDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        FMDevs.currentleadership = ld
        FMDevs.points = p
        FMDevs.power = bp
        if mno == 10:
            FMDevs.power += 4

        return FMDevs

    def HBolterDevs(self):
        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.HBDevestator(None)
        devestator2 = Model.HBDevestator(None)
        devestator3 = Model.HBDevestator(None)
        devestator4 = Model.HBDevestator(None)

        name = "Heavy Bolter Devestators"
        HBolterDevs = unit(name, 0, 0, 0, 0, 0)

        HBolterDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in HBolterDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        HBolterDevs.currentleadership = ld
        HBolterDevs.points = p
        HBolterDevs.power = bp
        if mno == 10:
            HBolterDevs.power += 4

        return HBolterDevs


    def GCDevs(self):
        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.GCDevestator(None)
        devestator2 = Model.GCDevestator(None)
        devestator3 = Model.GCDevestator(None)
        devestator4 = Model.GCDevestator(None)

        name = "Grav Cannon Devestators"
        GravDevs = unit(name, 0, 0, 0, 0, 0)

        GravDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in GravDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        GravDevs.currentleadership = ld
        GravDevs.points = p
        GravDevs.power = bp
        if mno == 10:
            GravDevs.power += 4

        return GravDevs

    def HFDevs(self):
        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.HFDevestator(None)
        devestator2 = Model.HFDevestator(None)
        devestator3 = Model.HFDevestator(None)
        devestator4 = Model.HFDevestator(None)

        name = "Heavy Flamer Devestators"
        FlameDevs = unit(name, 0, 0, 0, 0, 0)

        FlameDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in FlameDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        FlameDevs.currentleadership = ld
        FlameDevs.points = p
        FlameDevs.power = bp
        if mno == 10:
            FlameDevs.power += 4

        return FlameDevs



    def PCDevs(self):
        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.PCDevestator(None)
        devestator2 = Model.PCDevestator(None)
        devestator3 = Model.PCDevestator(None)
        devestator4 = Model.PCDevestator(None)

        name = "PlasmaCannon Devestators"
        PlasmaDevs = unit(name, 0, 0, 0, 0, 0)

        PlasmaDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in PlasmaDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        PlasmaDevs.currentleadership = ld
        PlasmaDevs.points = p
        PlasmaDevs.power = bp
        if mno == 10:
            PlasmaDevs.power += 4

        return PlasmaDevs

    def LPCDevs(self):
        devsgt = Model.DevestatorSGT(None)
        devestator1 = Model.LPCDevestator(None)
        devestator2 = Model.LPCDevestator(None)
        devestator3 = Model.LPCDevestator(None)
        devestator4 = Model.LPCDevestator(None)

        name = "PlasmaCannon Low Devestators"
        LowPlasmaDevs = unit(name, 0, 0, 0, 0, 0)

        LowPlasmaDevs.models = [devestator1,devestator2,devestator3,devestator4,devsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in LowPlasmaDevs.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1


        LowPlasmaDevs.currentleadership = ld
        LowPlasmaDevs.points = p
        LowPlasmaDevs.power = bp
        if mno == 10:
            LowPlasmaDevs.power += 4

        return LowPlasmaDevs

    def FullTacticalSquad(self):
        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.TacticalMarine(None)
        tactical2 = Model.TacticalMarine(None)
        tactical3 = Model.TacticalMarine(None)
        tactical4 = Model.TacticalMarine(None)
        tactical5 = Model.TacticalMarine(None)
        tactical6 = Model.TacticalMarine(None)
        tactical7 = Model.TacticalMarine(None)
        tactical8 = Model.TacticalMarine(None)
        tactical9 = Model.TacticalMarine(None)

        name = "10 Man brick"
        tacticalsquad = unit(name, 0, 0, 0, 0, 0)

        tacticalsquad.models = [tactical1, tactical2, tactical3, tactical4,tactical5,tactical6,tactical7,tactical8,tactical9,tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad

    def TacticalSquad(self):

        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.TacticalMarine(None)
        tactical2 = Model.TacticalMarine(None)
        tactical3 = Model.TacticalMarine(None)
        tactical4 = Model.TacticalMarine(None)


        name = "Tactical Squad"
        tacticalsquad = unit(name, 0, 0, 0,0,0)

        tacticalsquad.models = [tactical1,tactical2,tactical3,tactical4,tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno +=1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad



    def PlasmaTacticals1(self):

        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.TacticalMarine(None)
        tactical2 = Model.TacticalMarine(None)
        tactical3 = Model.TacticalMarine(None)
        tactical4 = Model.PlasmaTactical(None)

        name = "Plasma Tactical Squad"
        tacticalsquad = unit(name, 0, 0, 0, 0, 0)

        tacticalsquad.models = [tactical1, tactical2, tactical3, tactical4, tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad

    def PlasmaTacticals2(self):

        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.TacticalMarine(None)
        tactical2 = Model.TacticalMarine(None)
        tactical3 = Model.PlasmaTactical(None)
        tactical4 = Model.PlasmaTactical(None)

        name = "Plasma Tactical Squad"
        tacticalsquad = unit(name, 0, 0, 0, 0, 0)

        tacticalsquad.models = [tactical1, tactical2, tactical3, tactical4, tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad

    def PlasmaTacticals3(self):

        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.TacticalMarine(None)
        tactical2 = Model.PlasmaTactical(None)
        tactical3 = Model.PlasmaTactical(None)
        tactical4 = Model.PlasmaTactical(None)

        name = "Plasma Tactical Squad"
        tacticalsquad = unit(name, 0, 0, 0, 0, 0)

        tacticalsquad.models = [tactical1, tactical2, tactical3, tactical4, tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad

    def PlasmaTacticals4(self):

        tacticalsgt = Model.TacticalSergeant(None)
        tactical1 = Model.PlasmaTactical(None)
        tactical2 = Model.PlasmaTactical(None)
        tactical3 = Model.PlasmaTactical(None)
        tactical4 = Model.PlasmaTactical(None)

        name = "Plasma Tactical Squad"
        tacticalsquad = unit(name, 0, 0, 0, 0, 0)

        tacticalsquad.models = [tactical1, tactical2, tactical3, tactical4, tacticalsgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in tacticalsquad.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno += 1

        tacticalsquad.currentleadership = ld
        tacticalsquad.points = p
        tacticalsquad.power = bp
        if mno == 10:
            tacticalsquad.power += 4

        return tacticalsquad

    def boltsniper(self):

        sniper = Model.boltsniper(None)

        name = "BoltSniper"
        boltsniper = unit(name, 0, 0, 0,0,0)

        boltsniper.models = [sniper]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in boltsniper.models:
            if x.leadership > ld:
                ld = x.leadership
            p += x.points

            for y in x.weapons:
                p += y.points
                bp += y.power

            for z in x.wargear:
                p += z.points
                bp += z.power

            bp += x.power
            mno +=1

        boltsniper.currentleadership = ld
        boltsniper.points = p
        boltsniper.power = bp

        return boltsniper

    def Guardsmen(self):

        sgt = Model.GuardSergeant(None)
        Guardsman1 = Model.Guardsman(None)
        Guardsman2 = Model.Guardsman(None)
        Guardsman3 = Model.Guardsman(None)
        Guardsman4 = Model.Guardsman(None)
        Guardsman5 = Model.Guardsman(None)
        Guardsman6 = Model.Guardsman(None)
        Guardsman7 = Model.Guardsman(None)
        Guardsman8 = Model.Guardsman(None)
        Guardsman9 = Model.Guardsman(None)

        name = "Infantry Squad"
        infantrysquad = unit(name, 0, 0, 0, 0, 0)

        infantrysquad.models = [Guardsman1,Guardsman2,Guardsman3,Guardsman4,
                                Guardsman5,Guardsman6,Guardsman7,Guardsman8,Guardsman9,sgt]

        ld = 0
        p = 0
        bp = 0
        mno = 0

        for x in infantrysquad.models:
            if x == None:
                pass
            else:
                if x.leadership > ld:
                    ld = x.leadership
                p += x.points

                for y in x.weapons:
                    p += y.points


                for z in x.wargear:
                    p += z.points


            mno += 1

        infantrysquad.currentleadership = ld
        infantrysquad.points = p
        infantrysquad.power = 3


        return infantrysquad

    def custodianGuard(self):

        custode1 = Model.custodianGuard(None)
        custode2 = Model.custodianGuard(None)
        custode3 = Model.custodianGuard(None)

        name = "Custodian Guard"
        custodianGuard = unit(name, 0, 0, 0, 0, 0)

        custodianGuard.models = [custode1,custode2,custode3]

        ld = 0
        p = 0
        mno = 0

        for x in custodianGuard.models:
            if x == None:
                pass
            else:
                if x.leadership > ld:
                    ld = x.leadership
                p += x.points

                for y in x.weapons:
                    p += y.points


                for z in x.wargear:
                    p += z.points


            mno += 1

        custodianGuard.currentleadership = ld
        custodianGuard.points = p
        custodianGuard.power = 3


        return custodianGuard

    def predator(self):

        predator = Model.predator(None)

        name = "Predator"
        Predator = unit(name, 0, 0, 0, 0, 0)

        Predator.models = [predator]

        ld = 0
        p = 0
        mno = 0

        for x in Predator.models:
            if x == None:
                pass
            else:
                if x.leadership > ld:
                    ld = x.leadership
                p += x.points

                for y in x.weapons:
                    p += y.points


                for z in x.wargear:
                    p += z.points


            mno += 1

        Predator.currentleadership = ld
        Predator.points = p
        Predator.power = 3


        return Predator

    def LandRaider(self):

        landraider = Model.landraider(None)

        name = "Landraider"
        LandRaider = unit(name, 0, 0, 0, 0, 0)

        LandRaider.models = [landraider]

        ld = 0
        p = 0
        mno = 0

        for x in LandRaider.models:
            if x == None:
                pass

            else:
                if x.leadership > ld:
                    ld = x.leadership
                p += x.points

                for y in x.weapons:
                    p += y.points

                for z in x.wargear:
                    p += z.points


            mno += 1

        LandRaider.currentleadership = ld
        LandRaider.points = p
        LandRaider.power = 3


        return LandRaider

    def LandSpeeder(self):

        landspeeder = Model.landspeeder(None)

        name = "landspeeder"
        landSpeeder = unit(name, 0, 0, 0, 0, 0)

        landSpeeder.models = [landspeeder]

        ld = 0
        p = 0
        mno = 0

        for x in landSpeeder.models:
            if x == None:
                pass

            else:
                if x.leadership > ld:
                    ld = x.leadership
                p += x.points

                for y in x.weapons:
                    p += y.points

                for z in x.wargear:
                    p += z.points


            mno += 1

        landSpeeder.currentleadership = ld
        landSpeeder.points = p
        landSpeeder.power = 3


        return landSpeeder
