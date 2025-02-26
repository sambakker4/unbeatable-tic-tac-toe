from board import Board
import time
import tkinter

class Game:
    def __init__(self, win):
        self.win = win 
        self.board = Board(win) 
        self.board.draw()

    def get_winner(self):
        winner = self.board.who_won()
        
        if winner == "O":
           print("O won") 
        elif winner == "X":
           print("X won") 
        elif winner == "DRAW":
           print("Draw") 
