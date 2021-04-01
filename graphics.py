import pygame
import sys
from time import sleep

yellow = pygame.Color("yellow")
red = pygame.Color("red")

leftclick = 1

class GuiBoard:

    def __init__(self, rows, column, rowsize = 64, columnsize = 64, gap = 5, bg = "black"):
        pygame.init()

        self.rows = rows
        self.column = column
        self.gap = gap
        self.rowsize = rowsize
        self.columnsize = columnsize
        self.height = rows * rowsize + gap
        self.width = column * columnsize + gap
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.Color(bg)
        self.screen.fill(self.bg)
        

        pygame.display.set_caption("TIC TAC TOE")

        self.clock = pygame.time.Clock()
        self._initGraphics()
        self._intfont()

        self.drawboard()


    def _intfont(self):
        pygame.font.init()
        self.myfont = pygame.font.SysFont("Cosmic Sans MS", 75)
        self.xlabel = self.myfont.render("X", 1, yellow)
        self.olabel = self.myfont.render("O", 1, red)

    def _initGraphics(self):
        normallinep = "./resources/normalline.png"
        self.normallinev = pygame.image.load(normallinep)
        self.normallineh = pygame.transform.rotate(self.normallinev, -90)
        
    def updateboard(self, lis):
        self.clock.tick(60) 
        self.screen.fill(self.bg)

        self.drawboard()
        self.drawsymbols(lis)

    def getclick(self):
        #60 fps game
        while(1):
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                sys.exit(0)

            state = pygame.mouse.get_pressed(3)

            i = j = None
            if(state[0] == leftclick):
                mouse = pygame.mouse.get_pos()

                i = int(mouse[0] / 64)
                j = int(mouse[1] / 64)

                if(i < self.rows and j < self.column):
                    break

        return i, j

    def drawboard(self):
        for y in range(self.column + 1):
            for x in range(self.rows):
                self.screen.blit(self.normallineh, [x * self.rowsize + 5, y * self.columnsize])

        for x in range(self.rows + 1):
            for y in range(self.column):
                self.screen.blit(self.normallinev, [x * self.rowsize, y * self.columnsize + 5])

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
                    self.screen.blit(label, [i * (self.rowsize) + 14, j * (self.columnsize) + 10])
        pygame.display.flip()
 
    def cont(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        return 1



if __name__ == "__main__":
    g = GuiBoard(3, 3, bg = "white")
    lis = [[" " for i in range(3)] for j in range(3)]
    while(g.cont()):
        i, j = g.getclick()
        if(i != None and j != None):
            lis[i][j] = "O"
            g.updateboard(lis)



