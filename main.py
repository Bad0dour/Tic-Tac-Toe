from images import upload_images
import tkinter as tk
from tkmacosx import *
from setup import *

def disable_all_buttons():
    for button in buttons_grid.winfo_children():
        button.config(state="disabled")

def swap_turns():
    global naughts_turn
    print(f"All Placements: {button_tracker.items()}")
    naughts_turn = not naughts_turn
    if naughts_turn:
        print("\nO - NAUGHTS TURN:")

        for button in buttons_grid.winfo_children():
            button.config(activebackground=colour_map["NAUGHTS_ACCENT"])
    else:
        print("\nX - CROSSES TURN:")

        for button in buttons_grid.winfo_children():
            button.config(activebackground=colour_map["CROSSES_ACCENT"])

def start():
    global naught_placements, cross_placements, first_load, naughts_turn, button_tracker
    naughts_turn = False
    
    # Hide all labels
    draw_label.place_forget()
    play_again.place_forget()
    win_label.place_forget()
    print("\nCROSSES TURN:")
    
    #reset placements
    naught_placements, cross_placements = set(), set()
    button_tracker =  {
        1 : None,
        2 : None,
        3 : None,
        4 : None,
        5 : None,
        6 : None,
        7 : None,
        8 : None,
        9 : None,
    }

    if first_load == True:
        first_load = False
        #place buttons for the first time
        for row in range(3):
            for col in range(3):
                button = Button(
                    buttons_grid,
                    width=200,
                    height=200,
                    bg=bg_colour,
                    disabledbackground=bg_colour,
                    image=tk.PhotoImage(width=200, height=200),
                    activebackground=colour_map["CROSSES_ACCENT"],
                )
                button.grid(row=row, column=col, padx=10, pady=10)
                button.config(command=lambda r=row, c=col, b=button: placement((r,c), b))
    else:
        #reset already made buttons
        for button in buttons_grid.winfo_children():
            button.config(
                image=tk.PhotoImage(width=200, height=200),
                activebackground=colour_map["CROSSES_ACCENT"],
                state="normal")
            
def place(label) -> None:
    label.place(relx=0.5, rely=0.5, anchor="center")

def game_end(winner):
    global score_label, score
    disable_all_buttons()
    if winner == "draw":
        print("DRAW!")
        place(draw_label)
    else:
        print(f"{winner} WINS!")
        score[winner] += 1
        win_label.config(text=f"{winner} WINS!", bg=colour_map[f"{winner}_ACCENT"])
        place(win_label)
        score_label[winner].config(text=score[winner])
    play_again.place(relx=0.5, rely=0.6, anchor="center")

def placement(square: tuple[int,int], button) -> None:
    square_num = cell_mapping[square]

    # Quit early if cell taken already
    if button_tracker[square_num]:
        print("Space Already Taken...")
        return

    # depending who's turn it is, set the pressed cell to naught or cross
    if naughts_turn:
        print(f"Naught Placed in square {square_num}")
        button_tracker[square_num] = "NAUGHT"
        button.config(image=naught_image, state="disabled")
    else:
        print(f"Cross Placed in square {square_num}")
        button_tracker[square_num] = "CROSS"
        button.config(image=cross_image, state="disabled")

    for box, owner in button_tracker.items():
        if owner == "NAUGHT":
            naught_placements.add(box)
        elif owner == "CROSS":
            cross_placements.add(box)
    
    for combo in win_combos:
        if combo.issubset(naught_placements):
            game_end('NAUGHTS')
            return
        elif combo.issubset(cross_placements):
            game_end('CROSSES')
            return

    if len(naught_placements) + len(cross_placements) == 9:
        game_end('draw')
        return

    print(f"Naught Placements: {naught_placements}")
    print(f"Cross Placements: {cross_placements}")

    swap_turns()

# SETUP
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.minsize(300,300)
root.geometry("720x755+100+200")
root.attributes('-topmost', True)

images_list = upload_images()
board_image = images_list[0]
naught_image = images_list[1]
cross_image = images_list[2]

header = tk.Label(root,text="Tic-Tac-Toe",font=BIG_FONT)
header.pack()
buttons_grid = tk.Frame(root,width=500,height=500)
buttons_grid.pack()
draw_label = tk.Label(root,text="DRAW!",font=BIG_FONT,bg="white",fg=bg_colour,relief="solid",borderwidth=4,padx=10)
win_label = tk.Label(root,text="",font=BIG_FONT,bg="white",fg="white",relief="solid",borderwidth=4, padx=10)
play_again = Button(root,text="Play Again?",font=SMALL_FONT,bg="white",fg=bg_colour,command=start,padx=5)

naughts_label = tk.Label(root,text="- O",font=BIG_FONT,bg=bg_colour,fg=colour_map['NAUGHTS_ACCENT'])
naughts_label.place(relx=0.04, rely=0.01, x=50)
NAUGHTS_score_label = tk.Label(root,text=0,font=BIG_FONT,bg=bg_colour,fg=colour_map['NAUGHTS_ACCENT'])
NAUGHTS_score_label.place(relx=0.04, rely=0.01)
score_label["NAUGHTS"] = NAUGHTS_score_label

crosses_label = tk.Label(root,text="X -",font=BIG_FONT,bg=bg_colour,fg=colour_map['CROSSES_ACCENT'])
crosses_label.place(relx=0.9, rely=0.01, x=-90)
CROSSES_score_label = tk.Label(root,text=0,font=BIG_FONT,bg=bg_colour,fg=colour_map['CROSSES_ACCENT'])
CROSSES_score_label.place(relx=0.9, rely=0.01)
score_label["CROSSES"] = CROSSES_score_label


first_load = True
start()
root.mainloop()
