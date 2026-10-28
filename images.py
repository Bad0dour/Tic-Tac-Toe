import tkinter as tk

def upload_images():
    board = tk.PhotoImage(file="Images/board.png")
    board_image = board.subsample(2,2)
    naught = tk.PhotoImage(file="Images/circle.png")
    naught_image = naught.subsample(2,2)
    cross = tk.PhotoImage(file="Images/cross.png")
    cross_image = cross.subsample(2,2)
    return [board_image, naught_image, cross_image]