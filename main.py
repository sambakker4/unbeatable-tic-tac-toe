from board import Board
from window import Window
from game import Game


def main():
    win = Window(1000, 1000, "Unbeatable Tic Tac Toe")
    game = Game(win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
