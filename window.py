from tkinter import Tk, Canvas, Frame, BOTH


class Window:
    def __init__(self, width, height, title):
        self.root = Tk()
        self.width = width
        self.height = height
        self.root.title(title)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.running = False
        self.canvas.pack(expand=1, fill=BOTH)
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def draw_line(self, line, fill="black"):
        line.draw(self.canvas, fill)
