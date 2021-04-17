import pygame
import sys
from time import sleep

from board import Board

yellow = pygame.Color("yellow")
red = pygame.Color("red")
red1 = pygame.Color("red1")
green = pygame.Color("green")

leftclick = 1

class GuiBoard(Board):

    def __init__(self, height = 400, width = 400, player = "x", rows = 3, column = 3, gap = 5, bg = "black", status = True):

        super().__init__(rows, column, player)
        pygame.init()

        self.gap = 5
        self.rowsize = 64
        self.columnsize = 64 
        self.height = height 
        self.width = width
        self.offsetx = int((self.height / 2) - ((self.rowsize * 3 + gap * 4 ) / 2))
        self.offsety = int((self.width / 2) - ((self.columnsize * 3 + gap * 4 ) / 2))
        self.bg = pygame.Color(bg)
        self.clock = pygame.time.Clock()
        
        self._initGraphics()
        self._initscreen(status)
        self._intfont()

        self.drawboard()

    def _initscreen(self, status):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TicTacToe")
        self.screen.fill(self.bg)
        self.showstatus(status)
        

    def _intfont(self):
        pygame.font.init()
        self.myfont = pygame.font.SysFont("Cosmic Sans MS", 75)
        self.xlabel = self.myfont.render("X", 1, yellow)
        self.olabel = self.myfont.render("O", 1, red)

    def _initGraphics(self):
        normallinep = "./resources/normalline.png"
        self.normallinev = pygame.image.load(normallinep)
        self.normallineh = pygame.transform.rotate(self.normallinev, -90)

        greenindicator = "./resources/greenindicator.png"
        self.greenstatus = pygame.image.load(greenindicator)

        redindicator = "./resources/redindicator.png"
        self.redstatus = pygame.image.load(redindicator)

    def showstatus(self, status):
        if(status == True):
            self.screen.blit(self.greenstatus, [5, 5])
        else:
            self.screen.blit(self.redstatus, [5, 5])
        self.status = status
        pygame.display.flip()
        
    def updateboard(self):
        #60 fps game
        self.clock.tick(60) 
        self.screen.fill(self.bg)
        self.showstatus(self.status)

        self.drawboard()
        self.drawsymbols(self.ttt_board)

    def getclick(self):
        self.showstatus(True)
        while(1):
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                sys.exit(0)

            mouse = pygame.mouse.get_pos()
            state = pygame.mouse.get_pressed(3)

            i = j = None
            if(state[0] == leftclick):

                i = int((mouse[0] - self.offsetx) / 64)
                j = int((mouse[1] - self.offsety) / 64)

                if(i < self.row and j < self.col):
                    break
        self.showstatus(False)
        return i, j

    def drawboard(self):
        for y in range(self.col+ 1):
            for x in range(self.row):
                self.screen.blit(self.normallineh, [x * self.rowsize + 5 + self.offsetx, y * self.columnsize + self.offsety])

        for x in range(self.row + 1):
            for y in range(self.col):
                self.screen.blit(self.normallinev, [x * self.rowsize + self.offsetx, y * self.columnsize + 5 + self.offsety])

        pygame.display.flip()


    def drawsymbols(self, lis):
        for i, row in enumerate(lis):
            for j, symbol in enumerate(row):
                label = None
                symbol = symbol.upper()
                if(symbol == "X"):
                    label = self.xlabel
                elif(symbol == "O"):
                    label = self.olabel
                if(label):
                    self.screen.blit(label, [i * (self.rowsize) + 14 + self.offsetx, j * (self.columnsize) + 10 + self.offsety])
        pygame.display.flip()


    def cont(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        return 1

    def showwinner(self):
        myfont = pygame.font.SysFont("Cosmic Sans MS", 75)

        if(self.winner == self.player_one):
            winnertext = myfont.render("You Won", 1, green)
        elif(self.winner == self.player_two):
            winnertext = myfont.render("You lost", 1, red)
        else:
            winnertext = myfont.render("  Draw", 1, yellow)


        self.screen.blit(winnertext, [self.offsetx, 10])
        pygame.display.flip()
        sleep(3)





class WelcomeScreen:

    def __init__(self, height = 400, width = 400, maincolor=red,
            highlight=yellow, bg="black"):

        pygame.init()
        self.height = height 
        self.width = width 
        self.bg = pygame.Color(bg)
        self.clock = pygame.time.Clock()

        self.maincolor = maincolor
        self.highlight = highlight
        self.select = 0
        self.rawtext = {"Computer":1, "Host":0, "Connect":0, "Quit":0}

        self.optionlist = []
        self._initscreen()
        self._inittext()
        self.show_options()
        pass

    def _initscreen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TicTacToe")
        self.screen.fill(self.bg)

    def _inittext(self):
        self.myfont = pygame.font.SysFont("Cosmic Sans MS", 75)
        for option in self.rawtext:
            if(self.rawtext[option] == 1):
                self.optionlist += [self.myfont.render(option, 1, self.highlight)]
            else:
                self.optionlist += [self.myfont.render(option, 1, self.maincolor)]

 
    def select_option(self, select):
        optlist = ["Computer", "Host", "Connect", "Quit"]
        self.rawtext[self.select] = 0
        self.optionlist[self.select] = self.myfont.render(optlist[self.select], 1, self.maincolor)

        self.select = select
        opt = optlist[select]

        self.optionlist[select] = self.myfont.render(opt, 1, self.highlight)


    def show_options(self):
        self.clock.tick(60) 

        xcord = self.width / 2 
        ycord = self.height / 8

        for option in self.optionlist:
            text_rect = option.get_rect(center=[xcord, ycord])
            self.screen.blit(option, text_rect)
            ycord += self.height / 4
        
        pygame.display.flip()

    def get_selected_option(self):

        while True:
            self.clock.tick(60) 
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                sys.exit(0)


            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_RETURN]:
                return self.select

            if keys_pressed[pygame.K_UP]:
                self.select_option((self.select - 1) % 4)
                self.show_options()
                sleep(0.25)
            
            if keys_pressed[pygame.K_DOWN]:
                self.select_option((self.select + 1) % 4)
                self.show_options()
                sleep(0.25)

