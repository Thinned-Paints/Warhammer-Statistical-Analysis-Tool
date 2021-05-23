import csv
import Simulations
import pandas as panda
import matplotlib
import os
import Types
from Units import *
from matplotlib import pyplot as plot
import seaborn as sns

def heavyweaponsgraph(runs):
    logging = False
    #Runs is how many times you run each simulation, not the total, the total is 35* that size
    ran = 0
    HB = Units.HBolterDevs(None)
    MM = Units.MMDevs(None)
    LC = Units.LCannonDevs(None)
    GC = Units.GCDevs(None)
    FM = Units.FMDevs(None)
    KM = Units.FMDevs(None)
    HF = Units.HFDevs(None)
    PC = Units.PCDevs(None)
    weapons = [HB,MM,LC,GC,FM,KM,HF,PC]


    GM = Units.Guardsmen(None)
    M = Units.TacticalSquad(None)
    C = Units.custodianGuard(None)
    P = Units.predator(None)
    LR = Units.LandRaider(None)


    targets = [GM,M,C,P,LR]

    gunincrement = 0
    targetincrement = 0
    effectiverange = False

    resultar = []



    name = (weapons[gunincrement].name)+(targets[targetincrement].name)

    while ran<runs:
        gunincrement=0
        while gunincrement<9:
            HB = Units.HBolterDevs(None)
            MM = Units.MMDevs(None)
            LC = Units.LCannonDevs(None)
            GC = Units.GCDevs(None)
            FM = Units.FMDevs(None)
            KM = Units.KMDevs(None)
            HF = Units.HFDevs(None)
            PC = Units.PCDevs(None)
            LPC = Units.LPCDevs(None)
            #9
            weapons = [HB, MM, LC, GC, FM, KM, HF,PC,LPC]
            targetincrement=0

            while targetincrement<6:
                GM = Units.Guardsmen(None)
                M = Units.TacticalSquad(None)
                C = Units.custodianGuard(None)
                LS = Units.LandSpeeder(None)
                P = Units.predator(None)
                LR = Units.LandRaider(None)
                #6
                targets = [GM, M, C,LS, P, LR]

                spacemarines = army([weapons[gunincrement]], "", "Space Marines", 0)
                targetpractice = army([targets[targetincrement]], "", "Target Practice", 1)
                result = Simulations.heavyweaponstest(name, spacemarines, targetpractice, effectiverange)
                resultar.append(result)
                targetincrement+=1
            gunincrement+=1
        ran+=1
    targetar = []
    def dig(board):
        if board.armies:
            if board.armies[1].units:
                targetar.append([board.armies[1].units[0],board.turn,board.armies[0].units[0].models[0].weapons[0].name])
        if (board.prevboard):
            dig(board.prevboard)

    count = 0
    while True:
        if count>=len(resultar):
            break
        else:
            dig(resultar[count])
        if count==len(resultar):
            break
        count+=1

    """
    Create a loop, it will cycle through each data set, collating them into the right groups, each group will have it's
    average taken and a graph will be generated for each one.
    """
    hbolterresults=[]
    mmresults = []
    lcresults = []
    mlfresults = []
    mlkresults = []
    pcresults = []
    lpcresults = []
    gcresults = []
    hfresults = []

    for item in targetar:
        wounds = 0
        if logging:
            print(item[2],item[0])
        for model in item[0].models:
            wounds += model.wounds
        if item[2] == "Heavy Bolter":
            hbolterresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Modified Multi-Melta":
            mmresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Modified Lascannon":
            lcresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Modified Gravcannon":
            gcresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Modified Missile-Launcher-Frag":
            mlfresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Modified Missile-Launcher-Krak":
            mlkresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Heavy Flamer":
            hfresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Plasma Cannon High" or item[2] == "Boltgun":
            pcresults.append({'Weapon':item[2],'Turn':item[1],'Target':item[0].name,'Wounds':wounds})
        elif item[2] == "Plasma Cannon Low":
            lpcresults.append({'Weapon': item[2], 'Turn': item[1], 'Target': item[0].name, 'Wounds': wounds})
        else:
            print("Unrecognised value of ", item[2])

    sets = [hbolterresults,mmresults,mlfresults,lcresults,mlkresults,pcresults,lpcresults,gcresults,hfresults]

    for set in sets:

        datalist = []
        for x in set:
            print(x)
            thisset = x["Weapon"]
            if thisset=="Boltgun":
                thisset= "Plasma Cannon High"
            turn = x["Turn"]
            target = x["Target"]
            if x["Wounds"]==0:
                datalist.append([turn,target])

        df = panda.DataFrame.from_records(datalist)
        df.columns = ['Turn','Target']

        sns.set_theme(style="whitegrid")
        sns.violinplot(y='Target',x='Turn',scale='count',data=df).set_title(thisset)
        plot.show()



