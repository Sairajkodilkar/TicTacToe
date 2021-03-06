from graphics import *
from board import *
from network import *
from minimax import *
import random

class LanGame:

    def __init__(self, server = True, port = 8080, hostname = "localhost"):

        print("Connecting to other player...")

        self.server = server
        if(server):
            self._initserver(port)
        else:
            self._initclient(port, hostname)
    
    def _initserver(self, port):
            print("initializing server")
            self.play_board = GuiBoard(player="x", status=True)
            self.player = Server(port)
            self.player.connect()
            self.player.sendmsg(self.play_board.player_two)
            print("Server connected")

    def _initclient(self, port, hostname):
            print("initializing client")
            self.player = Client(port, hostname)
            self.player.connect()
            sym = self.player.recvmsg()
            self.play_board = GuiBoard(player=sym, status=False)
            print("Client connected")

    def play(self):

        while(not self.play_board.gameover()):
            if(self.server):
                self.sendmov()
                if(self.play_board.gameover()):
                    break
                self.recvmov()

            if(not self.server):
                self.recvmov()
                if(self.play_board.gameover()):
                    break
                self.sendmov()

        game.player.close()

        self.play_board.showwinner()
        return self.play_board.winner


    def sendmov(self):
        while(1):
            i, j = self.play_board.getclick()
            if(not self.play_board.isempty(i, j)):
                continue
            self.update_playboard(i, j, self.play_board.player_one)
            self.player.sendmsg(f"{i} {j}")
            self.play_board.evaluate()
            break

    def recvmov(self):
        mov = self.player.recvmsg()
        mov = mov.split()
        i, j = int(mov[0]), int(mov[1])
        self.update_playboard(i, j, self.play_board.player_two)
        self.play_board.evaluate()


    def update_playboard(self, i, j, player):
        self.play_board.update(i, j, player)
        self.play_board.updateboard()


class ComputerGame:

    def __init__(self, player_one="x"):
            self.play_board = GuiBoard(player=player_one, status=True)

    def play(self, player_one):
        while(not self.play_board.gameover()):
            if(player_one):
                self.getmov()
            
            if(self.play_board.gameover()):
                break

            i, j = findbestmove(self.play_board)
            self.update_playboard(i, j, self.play_board.player_two)
            self.play_board.evaluate()

            if(self.play_board.gameover()):
                break

            if(not player_one):
                self.getmov()

        withcomp.play_board.showwinner()
        return self.play_board.winner


    def getmov(self):
        while(1):
            i, j = self.play_board.getclick()
            if(not self.play_board.isempty(i, j)):
                continue
            self.update_playboard(i, j, self.play_board.player_one)
            self.play_board.evaluate()
            break

    def update_playboard(self, i, j, player):
        self.play_board.update(i, j, player)
        self.play_board.updateboard()


if(__name__ == "__main__"):
    while(1):
        wcs = WelcomeScreen()
        option = wcs.get_selected_option()

        if(option == 0):
            withcomp = ComputerGame("x")
            random.seed()
            random_player = random.randint(0, 1)
            withcomp.play(player_one=random_player)
            continue

        if(option == 1):
            game = LanGame(True)
            game.play()
            game.player.close()
            continue

        if(option == 2):
            game = LanGame(False)
            game.play()
            game.player.close()
            continue

        if(option == 3):
            exit(0)
            continue




















