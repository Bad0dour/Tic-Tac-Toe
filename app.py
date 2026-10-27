import tkinter as tk
import os
print(os.path.exists("Images/board.png"))

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.minsize(300,300)
root.geometry("300x300")
tk.Label(root, text="Tic-Tac-Toe").pack()

board = tk.PhotoImage(file="Images/board.png")

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.create_image(0, 0, anchor=tk.NW, image=board)
canvas.pack()

square1 = tk.Frame(root, width=230, height=230, bg="white")
canvas.create_window(110, 110, window=square1)

root.mainloop()
