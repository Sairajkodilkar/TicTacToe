from board import *

#alpha at start -infinity 
#beta is +infinity
#alpha beta pruning
def minimax(ttt_board, depth, alpha, beta, ismax):
    score = ttt_board.evaluate()
    
    if(score == 10 or score == -10):
        return score

    if(ttt_board.isfull()):
        return score

    if(ismax):
        best = -10000
        for i in range(ttt_board.row):
            for j in range(ttt_board.col):
                if(ttt_board.isempty(i, j)): #board pos is empty
                    ttt_board.update(i, j, ttt_board.player_one)
                    best = max(best, minimax(ttt_board, depth + 1, alpha, beta, not ismax)) 
                    alpha = max(alpha, best)
                    ttt_board.update(i, j, Board.empty)
                    if(alpha >= beta):
                        return best - depth
        return best - depth

    else:
        best = 10000
        for i in range(ttt_board.row):
            for j in range(ttt_board.col):
                if(ttt_board.isempty(i, j)):
                    ttt_board.update(i, j, ttt_board.player_two)
                    best = min(best, minimax(ttt_board, depth + 1, alpha, beta, not ismax)) 
                    beta = min(beta, best)
                    ttt_board.update(i, j, Board.empty)
                    if(beta <= alpha):
                        return best + depth
        return best + depth

    return best 

def findbestmove(ttt_board):
    prev_best = -1000
    best_i = -1
    best_j = -1
    alpha = -1000
    beta = 1000

    for i in range(ttt_board.row):
        for j in range(ttt_board.col):
            if(ttt_board.isempty(i, j)):
                ttt_board.update(i, j, ttt_board.player_one)
                best = minimax(ttt_board, 0, alpha, beta, False)
                ttt_board.update(i, j, Board.empty)

                if(best > prev_best):
                    prev_best = best
                    best_i = i
                    best_j = j


    return best_i, best_j




if(__name__ == "__main__"):
    x = board(3, 3, 'x')
    x.insert(0, 0, x.player_one)
    x.insert(0, 1, x.player_one)
    i, j = findbestmove(x)
    print(i, j)
    

