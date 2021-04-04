class Board():
    empty = '_'

    def __init__(self, row, col, player_one):
        self.row = row
        self.col = col
        self.player_one = player_one
        if(player_one.lower() == 'o'):
            self.player_two = 'x'
        else:
            self.player_two = 'o'
        self.ttt_board = [[Board.empty  for j in range(self.col)] for i in range(self.row)]
        self.winner = None


    def isempty(self, i, j):
        return self.ttt_board[i][j] == Board.empty

    def update(self, i, j, xo): #xo player 1 or 2
        self.ttt_board[i][j] = xo
        self.evaluate()

    def isfull(self):
        for i in range(self.row):
            for j in range(self.col):
                if(self.ttt_board[i][j] == Board.empty):
                    return False
        return True

    def evaluate(self):
        for i in range(self.row):
            if(self.ttt_board[i][0] == self.ttt_board[i][1] and self.ttt_board[i][1] == self.ttt_board[i][2]):
                if(self.ttt_board[i][0] == self.player_one):
                    self.winner = self.player_one
                    return 10

                elif(self.ttt_board[i][0] == self.player_two):
                    self.winner = self.player_two
                    return -10

        for i in range(self.col):
            if(self.ttt_board[0][i] == self.ttt_board[1][i] and self.ttt_board[1][i] == self.ttt_board[2][i]):
                if(self.ttt_board[0][i] == self.player_one):
                    self.winner = self.player_one
                    return 10
                elif(self.ttt_board[0][i] == self.player_two):
                    self.winner = self.player_two
                    return -10

        if(self.ttt_board[0][0] == self.ttt_board[1][1] and self.ttt_board[1][1] == self.ttt_board[2][2]):
            if(self.ttt_board[0][0] == self.player_one):
                self.winner = self.player_one
                return 10
            elif(self.ttt_board[0][0] == self.player_two):
                self.winner = self.player_two
                return -10

        if(self.ttt_board[0][2] == self.ttt_board[1][1] and self.ttt_board[1][1] == self.ttt_board[2][0]):
            if(self.ttt_board[0][2] == self.player_one):
                self.winner = self.player_one
                return 10
            elif(self.ttt_board[0][2] == self.player_two):
                self.winner = self.player_two
                return -10

        return 0

    def getlist(self):
        return self.ttt_board

    def __repr__(self):
        lis = self.ttt_board
        return f'\t\t|{lis[0][0]}|{lis[0][1]}|{lis[0][2]}|\n\
                -------\n\
                |{lis[1][0]}|{lis[1][1]}|{lis[1][2]}|\n\
                -------\n\
                |{lis[2][0]}|{lis[2][1]}|{lis[2][2]}|\n\
                -------'

    '''
    def __str__(self):
        string = ''
        for i in self.ttt_board:
            string += "".join(i)

        return string
        '''




if(__name__ == '__main__'):
    x = Board(3, 3, 'x')
    print(x)



