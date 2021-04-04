from graphics import *
from board import *
from network import *

class LanGame:

    def __init__(self, server = True, port = 8080, hostname = "localhost"):

        print("Connecting to other player...")

        self.server = not (not server)
        if(server):
            self.play_board = GuiBoard(player="x", status=True)
            self.player = Server(port)
            self.player.connect()
            self.player.sendmsg(self.play_board.player_two)
            print("Server connected")
        else:
            self.player = Client(port, hostname)
            self.player.connect()
            sym = self.player.recvmsg()
            self.play_board = GuiBoard(player=sym, status=False)
            print("Client connected")

    def play(self):
        while(not self.gameover()):
            if(server):
                self.sendmov()
                if(self.gameover()):
                    break
                self.recvmov()

            if(not server):
                self.recvmov()
                if(self.gameover()):
                    break
                self.sendmov()

        game.player.close()

    def gameover(self):
        return self.play_board.evaluate() != 0 or self.play_board.isfull()

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


if(__name__ == "__main__"):
    server = int(input("server "))
    game = LanGame(server)
    game.play()


