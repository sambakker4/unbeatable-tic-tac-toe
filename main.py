from board import Board
from window import Window


def main():
    win = Window(1000, 1000, "Unbeatable Tic Tac Toe")
    board = Board(win)
    board.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
