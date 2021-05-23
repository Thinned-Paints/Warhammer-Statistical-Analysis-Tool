from Units import *
from Models import Model
from Board import *
from Shooting import *
from Movement import *
from Types import *
from DevTools import *


def boltsnipers(param):
    sniper1 = Units.boltsniper(None)
    sniper1.xc = 250
    sniper1.y = 70
    # movement.placemodel(sniper1, 250, 70)
    sniper2 = Units.boltsniper(None)
    sniper2.xc = 35
    sniper2.y = 1800
    movement.placemodel(sniper2, 35, 1800)

    redsnipers = army([sniper1], "", "Sniper Team 1", 0)

    bluesnipers = army([sniper2], "", "Sniper Team 2", 0)

    board1 = board(1219, 1829, [redsnipers, bluesnipers], [], 1, "Movement", 0)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(sniper1, sniper2, board1)

    return None


def taccontroller(runs):
    for x in range(0, runs):
        tacticalsVStacticals(None)


def plasmaVSnumbers0(param):
    logging = False

    v = -1
    tacsquad = Units.FullTacticalSquad(None)

    eviltacsquad = Units.TacticalSquad(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    # print("sm firing")
    # shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v


def plasmaVSnumbers1(param):
    logging = False
    v = -1
    tacsquad = Units.FullTacticalSquad(None)

    eviltacsquad = Units.PlasmaTacticals1(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    # print("sm firing")
    # shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v


def plasmaVSnumbers2(param):
    logging = False
    v = -1
    tacsquad = Units.FullTacticalSquad(None)

    eviltacsquad = Units.PlasmaTacticals2(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    # print("sm firing")
    # shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v


def plasmaVSnumbers3(param):
    logging = False
    v = -1
    tacsquad = Units.FullTacticalSquad(None)

    eviltacsquad = Units.PlasmaTacticals3(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    # print("sm firing")
    # shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v


def plasmaVSnumbers4(param):
    logging = False
    v = -1
    tacsquad = Units.FullTacticalSquad(None)

    eviltacsquad = Units.PlasmaTacticals4(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    # print("sm firing")
    # shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        # print("sm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        # print("csm firing")
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v


def tacticalsVStacticals(param):
    v = -1
    tacsquad = Units.TacticalSquad(None)

    eviltacsquad = Units.TacticalSquad(None)

    spacemarines = army([tacsquad], "", "Space Marines", 0)

    renegademarines = army([eviltacsquad], "", "Evil space marines", 1)

    board1 = board(1219, 1829, [spacemarines, renegademarines], [], 1, "Movement", 0, [])

    movement.linedeploy([25, 25], tacsquad)

    movement.linedeploy([25, 250], eviltacsquad)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(tacsquad, eviltacsquad, board1)

    if (casualties.tabledcheck(renegademarines)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")
    movement.maxmove(eviltacsquad, 30)

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    if (tacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(tacsquad, eviltacsquad, board1)
        if casualties.tabledcheck((renegademarines)):
            v = 0
            return v

    if (eviltacsquad != None):
        board.advancetophase(board1, "Shooting")
        Shooting.unitfire(eviltacsquad, tacsquad, board1)
        if (casualties.tabledcheck(spacemarines)):
            v = 1
            return v

    return v
    # print("Test finished")


def movetesting(param):
    tacsquad = Units.TacticalSquad(None)
    tacsquad2 = Units.TacticalSquad(None)
    spacemarines = army([tacsquad], "", "Space Marines", 0)
    placeholder = army([tacsquad2], "", "Placeholders", 0)

    board1 = board(1219, 1829, [spacemarines], [placeholder], 1, "Movement", 0, [])
    movement.linedeploy([884, 150], tacsquad)
    board1.advancetophase("Movement")
    unit.dump(tacsquad)
    movement.unitmove(tacsquad, 6, 45)
    unit.dump(tacsquad)
    return


def moraletest(param):
    import Shooting

    guardsquad = Units.Guardsmen(None)
    tacsquad = Units.TacticalSquad(None)

    shooter = army([tacsquad], "", "Shooters", 0)
    target = army([guardsquad], "", "Targets", 0)

    board1 = board(1219, 1829, [shooter], [target], 1, "Deployment", 0, [])

    movement.linedeploy([884, 150], tacsquad)

    movement.linedeploy([884, 150], guardsquad)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(tacsquad, guardsquad, board1)

    board.advancetophase(board1, "Morale")
    unit.litedump(guardsquad)
    unit.litedump(tacsquad)


def HBoltervsguard(param):
    v = -1

    HBDevs = Units.HBolterDevs()

    guardsmen = Units.Guardsmen()

    spacemarines = army([HBDevs], "", "Space Marines", 0)
    guard = army([guardsmen], "", "Imperial Guard", 1)

    board1 = board(1219, 1829, [spacemarines, guard], [], 1, "Movement", 0, [])

    movement.linedeploy([609, 150], HBDevs)

    movement.linedeploy([609, 1679], guardsmen)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(HBDevs, guardsmen, board1)

    if (casualties.tabledcheck(guard)):
        v = 0
        return v

    board.advancetophase(board1, "Movement")


def multimeltavscustodes(param):
    v = -1

    MMDevs = Units.PlasmaTacticals4(None)

    custodes = Units.custodianGuard(None)

    spacemarines = army([MMDevs], "", "Space Marines", 0)
    custodians = army([custodes], "", "Golden Janitors", 1)

    board1 = board(1219, 1829, [spacemarines, custodians], [], 1, "Movement", 0, [])

    movement.linedeploy([609, 150], MMDevs)

    movement.linedeploy([609, 679], custodes)

    board.advancetophase(board1, "Movement")

    movement.unitmove(MMDevs, 500, 90)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(MMDevs, custodes, board1)

    MMDevs.litedump()

    if (casualties.tabledcheck(custodians)):
        v = 0
        return v
    print("Turn Over")

    # Moving to custodes shooting phase
    board.advancetophase(board1, "Shooting")
    # Advancing to SM Movement
    board.advancetophase(board1, "Movement")

    movement.unitmove(MMDevs, 500, 90)

    board.advancetophase(board1, "Shooting")

    Shooting.unitfire(MMDevs, custodes, board1)

    if (casualties.tabledcheck(custodians)):
        v = 0
        return v

    # Moving to custodes shooting phase
    board.advancetophase(board1, "Shooting")
    # Advancing to SM Movement
    board.advancetophase(board1, "Movement")

    movement.unitmove(MMDevs, 500, 90)


def heavyweaponstest(name, devarmy, targetarmy, effectiverange):
    # Name is the name of the test, this will be used to identify it within the CSV
    # devarmy is the space marines, it should contain one unit of devestators
    # targetarmy is the target, it should only contain one target unit
    # Effectiverage is a boolean that is used for melta selection, it determines if you get to your maximum range, or your effective range
    gameboard = None
    logging = False

    gameboard = board(381, 1016, [devarmy, targetarmy], [], 1, "Deployment", 0, [])
    devestators = devarmy.units[0]
    target = targetarmy.units[0]
    movement.linedeploy([129, 25], devestators)

    movement.linedeploy([129, 996], target)

    board.advancetophase(gameboard, "Movement")

    dev1 = devestators.models[0]
    dev1primary = dev1.weapons[0]
    if logging:
        print(dev1primary.name)
    try:
        target1 = target.models[0]
    except:
        return board

    while True:
        if InRange(dev1, target1, dev1primary) and not effectiverange:
            if logging:
                print("Shooting")
            if gameboard.phase == "Shooting":
                board.advancetophase(gameboard, "Movement")
            board.advancetophase(gameboard, "Shooting")
            Shooting.unitfire(devestators, target, gameboard)
            if not target.models:
                return (gameboard)
            if gameboard.turn > 12:
                return (gameboard)
            board.advancetophase(gameboard, "Movement")

        else:
            if logging:
                print("Moving")
            # print("Moving")
            if gameboard.phase == "Movement":
                board.advancetophase(gameboard, "Shooting")
                board.advancetophase(gameboard, "Movement")
            movement.maxmove(devestators, 90)
            board.advancetophase(gameboard, "Movement")


def casualtytest(self):
    MMDevs = Units.MMDevs(None)

    custodes = Units.custodianGuard(None)

    spacemarines = army([MMDevs], "", "Space Marines", 0)
    custodians = army([custodes], "", "Golden Janitors", 1)

    board1 = board(1219, 1829, [spacemarines, custodians], [], 1, "Movement", 0, [])

    board1.dump()

    Shooting.unitfire(MMDevs, custodes, board1)
