import tkinter as tk
from tkmacosx import *
from main import placement

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.minsize(300,300)
root.geometry("700x700+100+200")
root.attributes('-topmost', True)

# GAME GUI CREATION
board_image = tk.PhotoImage(file="Images/board.png")
circle_image = tk.PhotoImage(file="Images/circle.png")
cross_image = tk.PhotoImage(file="Images/cross.png")

tk.Label(root, text="Tic-Tac-Toe")

for row in range(3):
    for col in range(3):
        Button(
            root,
            width=100,
            height=100,
            bg="#1E1E1E",
            focuscolor="",
            activebackground="#1E1E1E",
            command=add_placement((row,col))
        ).grid(row=row, column=col)


root.mainloop()
