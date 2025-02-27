from elements import Line, TicTacToeButton
import time
import tkinter

class Board:
    def __init__(self, win):
        self._win = win
        self.create_board()

    def create_board(self):
        self._board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
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
        i, j = pos
        button = self.buttons[i][j].button
        if button.cget("text") == "":
            button.config(text="O")
            self._board[i][j] = "O"

        if len(self._possible_moves(self._board)) > 0:
            i, j = self._get_best_move()
            self._board[i][j] = "X"
            button = self.buttons[i][j].button
            button.config(fg="red")
            button.config(text="X")

        if self.is_game_over():
            if self._did_x_win(self._board) or self._did_o_win(self._board):
                self.disable_board()
                self.cross_winner()

    def disable_board(self):
        for row in self.buttons:
            for button in row:
                button.button.config(state=tkinter.DISABLED)
                button.button.lower()

    def cross_winner(self):
        if self._did_x_win(self._board):
            target = "X"
        elif self._did_o_win(self._board):
            target = "O"
        else:
            return
        board = self._board
        buttons = self.buttons

        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                self.draw_char((i, j), self._board[i][j])

        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == target:
                line = Line(
                    buttons[i][0].x,
                    buttons[i][0].y + (buttons[i][0].height / 2),
                    buttons[i][2].x + (buttons[i][2].width),
                    buttons[i][2].y + (buttons[i][0].height / 2)
                )
                line.draw(self._win.canvas, width=5)

        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j] == target:
                line = Line(
                    buttons[0][j].x + (buttons[0][j].width / 2), 
                    buttons[0][j].y, 
                    buttons[2][j].x + (buttons[2][j].width / 2), 
                    buttons[2][j].y + (buttons[2][j].height)
                )
                line.draw(self._win.canvas, width=5)

        if board[0][0] == board[1][1] == board[2][2] == target:
            line = Line(
                buttons[0][0].x, 
                buttons[0][0].y, 
                buttons[2][2].x + (buttons[2][2].width), 
                buttons[2][2].y + (buttons[2][2].height)
            )
            line.draw(self._win.canvas, width=5)
        
        if board[0][2] == board[1][1] == board[2][0] == target:
            line = Line(
                buttons[0][2].x + (buttons[0][2].width), 
                buttons[0][2].y, 
                buttons[2][0].x, 
                buttons[2][0].y + (buttons[2][0].height)
            )
            line.draw(self._win.canvas, width=5)
        

    def draw_char(self, pos, char):
        i, j = pos
        if self._board[i][j] == "X":
            color = "red"
        else:
            color = "black"

        x = int((self._win.width / 3 * j) + self._win.width / 6)
        y = int((self._win.height / 3 * i) + self._win.width / 6)

        self._win.canvas.create_text(x, y, text=char, font=("Arial", 50), fill=color)

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

