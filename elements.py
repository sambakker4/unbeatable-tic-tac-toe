from tkinter import Button
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas, fill="black", width=2):
        id = canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill, width=width)
        canvas.tag_raise(id)

class TicTacToeButton:
    def __init__(self, width, height, win, text, x, y, command, pos):
        self._win = win
        self.width = width
        self.pos = pos
        self.height = height

        self.button = Button(
            win.root,
            text=text,
            font=("Arial", 50),
            bg=self._win.canvas['bg'],
            activebackground=self._win.canvas['bg'],  # Match when active
            borderwidth=0,  # Remove the border
            highlightthickness=0,
            command=lambda: command(self.pos)
        )
        self.x = x
        self.y = y

    def draw(self):
        self.button.place(x=self.x, y=self.y, width=self.width, height=self.height)
