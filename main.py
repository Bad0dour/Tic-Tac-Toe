from images import upload_images
import tkinter as tk
from tkmacosx import *
from setup import *


# SETUP
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.minsize(300,300)
root.geometry("700x700+100+200")
root.attributes('-topmost', True)

    #--Elements
header = tk.Label(root, text="Tic-Tac-Toe", font=("Arial", 30))
header.pack()
buttons_grid = tk.Frame(root, width=500, height=500)
buttons_grid.pack()

images_list = upload_images()
board_image = images_list[0]
naught_image = images_list[1]
cross_image = images_list[2]

def enable_all_buttons():
    for button in buttons_grid.winfo_children():
        button.configure(state="normal")

def disable_all_buttons():
    for button in buttons_grid.winfo_children():
        button.configure(state="disabled")

def game_win(shape: str) -> None:
    print(f"{shape} WINS!")
    shape_color = shape_colour_map[shape]

    # WIN LABEL
    tk.Label(
        root,
        text=f"{shape} WINS!", 
        font=("Arial", 60, "bold"),
        bg=shape_color,
        fg=bg_colour,
        relief="solid", borderwidth=2
        
    ).place(relx=0.5, rely=0.5, anchor="center")

    # PLAY AGAIN BUTTON
    Button(
        root,
        text="Play Again?", 
        font=("Arial", 30, "bold"),
        bg="white",
        fg=bg_colour,
        command=start
    ).place(relx=0.5, rely=0.6, anchor="center")
    

def game_draw():
    print("DRAW!")

    # WIN LABEL
    tk.Label(
        root,
        text="DRAW!", 
        font=("Arial", 60, "bold"),
        bg="white",
        fg=bg_colour,
        relief="solid", borderwidth=2
        
    ).place(relx=0.5, rely=0.5, anchor="center")

    # PLAY AGAIN BUTTON
    Button(
        root,
        text="Play Again?", 
        font=("Arial", 30, "bold"),
        bg="white",
        fg=bg_colour,
        command=start
    ).place(relx=0.5, rely=0.6, anchor="center")

def start():
    global naught_placements, cross_placements
    naught_placements = set()
    cross_placements = set()
    for row in range(3):
        for col in range(3):
            button = Button(
                buttons_grid,
                width=200,
                height=200,
                bg=bg_colour,
                disabledbackground=bg_colour,
                image=tk.PhotoImage(width=200, height=200),
            )
            button.grid(row=row, column=col, padx=10, pady=10)
            button.configure(command=lambda r=row, c=col, b=button: placement((r,c), b))
    print("\nCROSSES TURN:")


def placement(square: tuple[int,int], button) -> None:
    disable_all_buttons()
    global naughts_turn
    
    
    # Quit early if cell taken already
    all_placements = naught_placements | cross_placements
    print(f"All_placemetns: {all_placements}")
    if cell_mapping[square] in all_placements:
        print("Space Already Taken...")
        enable_all_buttons()
        return

    # depending who's turn it is, set the pressed cell to naught or cross
    if naughts_turn:
        print("Naught Placed")
        naught_placements.add(cell_mapping[square])
        button.config(image=naught_image, state="disabled")
    else:
        print("Cross Placed")
        cross_placements.add(cell_mapping[square])
        button.config(image=cross_image, state="disabled")

    for combo in win_combos:
        if combo.issubset(naught_placements):
            game_win('NAUGHTS')
            return
        elif combo.issubset(cross_placements):
            game_win('CROSSES')
            return

    if len(naught_placements) + len(cross_placements) == 9:
        game_draw()

    #swap turns
    naughts_turn = not naughts_turn 
    print(f"Naught Placements: {naught_placements}")
    print(f"Cross Placements: {cross_placements}")
    if naughts_turn:
        print(f"\nNAUGHTS TURN:")
    else:
        print(f"\nCROSSES TURN:")

    enable_all_buttons()

start()

root.mainloop()
