from elements import Line, TicTacToeButton
import tkinter

class Board:
    def __init__(self, win):
        self._win = win
        self._board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.create_board()

    def create_board(self):
        self.lines = [
            Line(self._win.width / 3, 0, self._win.width / 3, self._win.height),
            Line(self._win.width / 3 * 2, 0, self._win.width /3 * 2, self._win.height),
            Line(0, self._win.height / 3, self._win.width, self._win.height / 3),
            Line(0, self._win.height / 3 * 2, self._win.width, self._win.height / 3 * 2)
        ]
        self.buttons = []

        for i in range(len(self._board)):
            inner_list = []
            for j in range(len(self._board[0])):
                width = int(self._win.width / 3) - 20
                height = int(self._win.height / 3) - 20
                inner_list.append(TicTacToeButton(
                    width, 
                    height,
                    self._win,
                    self._board[i][j],
                    int(self._win.width / 3 * j + (20 / 3 * (j + 1))),
                    int(self._win.height / 3 * i + (20 / 3 * (i + 1))),
                    pos=(i, j),
                    command=self.on_click
                ))
            self.buttons.append(inner_list)

    def draw(self):
        for line in self.lines:
            line.draw(self._win.canvas)

        for row in self.buttons:
            for button in row:
                button.draw()

    def on_click(self, pos):
        if self.is_game_over():
            self.disable_board()
            return

        i, j = pos
        button = self.buttons[i][j].button
        if button.cget("text") == "":
            button.config(text="O")
            self._board[i][j] = "O"

        if len(self._possible_moves(self._board)) > 0:
            i, j = self._get_best_move()
            self._board[i][j] = "X"
            button = self.buttons[i][j].button
            button.config(text="X")

    def disable_board(self):
        for row in self.buttons:
            for button in row:
                button.button.config(state=tkinter.DISABLED)

    def _did_x_win(self, board):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == "X":
                return True

        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j] == "X":
                return True

        if board[0][0] == board[1][1] == board[2][2] == "X":
            return True

        if board[0][2] == board[1][1] == board[2][0] == "X":
            return True

        return False

    def _did_o_win(self, board):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == "O":
                return True

        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j] == "O":
                return True

        if board[0][0] == board[1][1] == board[2][2] == "O":
            return True

        if board[0][2] == board[1][1] == board[2][0] == "O":
            return True

        return False

    def is_game_over(self):
        board = self._board
        if self._possible_moves(board) == []:
            return True

        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == "O" or board[i][0] == "X":
                    return True

        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == "O" or board[0][j] == "X":
                    return True
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "X" or board[0][0] == "O":
                return True

        if board[2][0] == board[1][1] == board[0][2]:
            if board[2][0] == "X" or board[2][0] == "O":
                return True

        return False

    def _possible_moves(self, board):
        possible_moves = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "":
                    possible_moves.append((i, j))
        return possible_moves

    def _get_best_move(self):
        moves = []
        for i, j in self._possible_moves(self._board):
            self._board[i][j] = "X"
            moves.append((i, j, self._minimax(self._board, 0, False)))
            self._board[i][j] = ""

        best_move = (2, 2, float("-inf"))

        for move in moves:
            if move[2] > best_move[2]:
                best_move = move
        return best_move[0], best_move[1]

    def _minimax(self, board, depth, is_maximizing_player):
        if self.is_game_over():
            if self._did_x_win(board):
                return 10 - depth
            elif self._did_o_win(board):
                return depth - 10
            else:
                return 0  # Draw

        if is_maximizing_player:
            best_val = float("-inf")

            for i, j in self._possible_moves(board):
                board[i][j] = "X"
                value = self._minimax(board, depth + 1, False)
                board[i][j] = ""
                best_val = max(value, best_val)

            return best_val

        else:
            best_val = float("inf")
            for i, j in self._possible_moves(board):
                board[i][j] = "O"
                value = self._minimax(board, depth + 1, True)
                board[i][j] = ""
                best_val = min(value, best_val)

            return best_val

    def who_won(self):
        if self._did_o_win(self._board):
            return "O"
        elif self._did_x_win(self._board):
            return "X"
        else:
            return "DRAW"

