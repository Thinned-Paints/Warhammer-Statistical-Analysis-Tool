"""
This is the class containing the board
"""
from Movement import movement
from Types import *
from DevTools import DevTools
from Casualties import *
'''
Within this class the board is generated, the board is fundamental to the game, as it is the physical space the game
takes place in, I am also using it as a container to hold all the variables for the game. It's X and Y are the dimensions
of the board, as all boards are rectangular, this should be fine.

Of course, if non rectangular boards are ever introduced, I will just start crying.
'''
class board:

    def __init__(self, x, y, armies, terrain,turn,phase,player,prevboard):
        self.armies = armies
        self.terrain = terrain
        self.y = y
        self.x = x
        self.turn = turn
        self.phase = phase
        self.player = player
        self.prevboard = prevboard

    def dump(self):
        xmm = self.x/10
        ymm = self.y/10
        xin = xmm/25.4
        yin = ymm/25.4

        print("X = ",xmm,"mm / ",round(xin),'"')
        print("Y = ",ymm,"mm / ",round(yin),'"')
        if self.armies:
            print("Running unit dump")
            for i in self.armies:
                army.dump(i)
        if self.terrain:
            print("Running Terrain dump")
            for i in self.terrain:
                print(i)


    def phasestatus(board):
        print("Phase is: ",board.phase)
        print("Turn is: ", board.turn)
        print("Player is: ", board.player, "Their army is", board.armies[(board.player-1)].faction)

    def advancetophase(board1,goal):

        board.advancephase(board1)
        x = False
        while x==False:
            if board1.phase == goal:
                x = True
            else:
                board.advancephase(board1)


    def skipturn(board):
        board.turn +=1


    def advancephase(board):
        """
        This is a key function, it advances the phases of the game, the phase order is:
        Movement
        Psychic
        Shooting
        Charge
        Melee
        Morale

        These are done sequentially

        There is also a deployment phase, it only occurs in the first turn and cannot be accessed again.
        """
        phase = board.phase
        if board.phase=="Deployment":
            movement.setbounds(board)
        if board.phase == "Morale":
            casualties.morale(board)
            if board.player == 0:
                board.phase = "Movement"
                board.player = 1
                return

            elif board.player == 1:
                board.phase = "Movement"
                board.turn += 1
                #print(board.turn)
                board.player = 0
                return
        '''
        This saves the current board to prevboard, this lets the game remember what was happening at the start of every
        turn, allowing for things like morale, and checking if models have moved.
        '''

        if phase == "Deployment":
            board.phase = "Movement"

        if phase == "Movement" and board.player == 0:
            boardcopy = copy.deepcopy(board)
            board.prevboard = boardcopy

        if phase == "Melee":
            board.phase = "Morale"

        if phase == "Charge":
            board.phase = "Melee"

        if phase == "Shooting":
            board.phase = "Charge"

        if phase == "Psychic":
            board.phase = "Shooting"

        if phase == "Movement":
            board.phase = "Psychic"

