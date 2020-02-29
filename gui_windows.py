import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)

        self.generate = tk.Button(self, text="Generate Solar System")
        self.run = tk.Button(self, text="Run Solar System")