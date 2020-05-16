import numpy as np
import game

import numpy as np

class Game(object):

    def __init__(self):
        pass
        
    def state(self):
        raise NotImplementedError()
        
    def score(self):
        return 0
        
    def make_move(self, move):
        raise NotImplementedError()
        
    def undo_move(self):
        raise NotImplementedError()
        
    def legal_moves(self):
        raise NotImplementedError()
        
    def game_over(self):
        return False

class UltimateTicTacToe(Game):

    def __init__(self):
        self.board = [[' ' for i in range(9)] for j in range(9)]
        self.turn = 'X'
        self.moves = []
        self.all_possible = [(a,b) for a in range(9) for b in range(9)]
        
    def won_box(self, letter, index):
        box = self.board[index]
        top_row = box[0] == letter and box[1] == letter and box[2] == letter
        middle_row = box[3] == letter and box[4] == letter and box[5] == letter
        bottom_row = box[6] == letter and box[7] == letter and box[8] == letter
        left_column = box[0] == letter and box[3] == letter and box[6] == letter
        middle_column = box[1] == letter and box[4] == letter and box[7] == letter
        right_column = box[2] == letter and box[5] == letter and box[8] == letter
        right_diagonal = box[0] == letter and box[4] == letter and box[8] == letter
        left_diagonal = box[2] == letter and box[4] == letter and box[6] == letter

        return (top_row or middle_row or bottom_row or left_column or middle_column or right_column or 
            right_diagonal or left_diagonal)
            
    def is_winner(self, letter):        
        top_row = (self.won_box(letter, 0) and self.won_box(letter, 1) and self.won_box(letter, 2))
        middle_row = (self.won_box(letter, 3) and self.won_box(letter, 4) and self.won_box(letter, 5))
        bottom_row = (self.won_box(letter, 6) and self.won_box(letter, 7) and self.won_box(letter, 8))
        left_column = (self.won_box(letter, 0) and self.won_box(letter, 3) and self.won_box(letter, 6))
        middle_column = (self.won_box(letter, 1) and self.won_box(letter, 4) and self.won_box(letter, 7))
        right_column = (self.won_box(letter, 2) and self.won_box(letter, 5) and self.won_box(letter, 8))
        right_diagonal = (self.won_box(letter, 0) and self.won_box(letter, 4) and self.won_box(letter, 8))
        left_diagonal = (self.won_box(letter, 2) and self.won_box(letter, 4) and self.won_box(letter, 6))
        
        return (top_row or middle_row or bottom_row or left_column or middle_column or right_column or             
            right_diagonal or left_diagonal)
            
    def score(self):     
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        return 0
        
    def game_over(self):
        if self.score != 0:
            return True
        else:
            check = [[a != ' ' for a in group] for group in self.board]
            outer_check = [all(box) for box in check]
            return all(outer_check)
            
    def state(self):  
        data = np.zeros((10,3,3))
        data[9, :, :] = (1 if (self.turn == 'X') else -1)
        for i in range(9):
            data[i, :, :] = self.board[i].reshape(3,3)
            
        return data
        
    def legal_moves(self):
        if not self.moves or self.won_box('X', moves[-1][1]) or self.won_box('O', moves[-1][1]):   
            return [m for m in self.all_possible if m not in self.moves]
        else:
            return [m for m in self.all_possible if m[0] == moves[-1][1]]
            
    def make_move(self, move):
        self.board[move[0]][move[1]] = self.turn
        self.turn = ('X' if self.turn == 'O' else 'O')
        self.moves.append(move)
        self.all_possible.remove(move)
    
    def undo_move(self):
        move = self.moves.pop()
        self.turn = ('X' if self.turn == 'O' else 'O')
        self.board[move[0]][move[1]] = ' '
        self.all_possible.append(move)
        
    def to_string(self):
        for i in range(9):
            for j in range(9):
                print('|' + self.board[(i/3)*3 + (j/3)][(i%3)*3 + (j%3)] + '| '),
                if j==2 or j==5:
                    print('  '),
            print('\n')
            if i==2 or i==5:
                print('\n')

def main():
    
    print("hello")
    tictac = UltimateTicTacToe()
    tictac.make_move((4,5))
    tictac.make_move((3,7))
    tictac.make_move((6,2))
    tictac.make_move((2,8))
    tictac.to_string()     

if __name__ == '__main__':
    main()