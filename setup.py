bg_colour = "#1E1E1E"

BIG_FONT = ("Avenir Next", 60, "bold")
SMALL_FONT = ("Avenir Next", 30, "bold")

colour_map = {
    "CROSSES": "#FFB766",
    "CROSSES_ACCENT": "#F2600C",
    "NAUGHTS": "#89CFF0",
    "NAUGHTS_ACCENT": "#1E4E8C"
}

score_label = {}

score = {
    "NAUGHTS": 0,
    "CROSSES": 0
}

win_combos = [
    {1,2,3},
    {4,5,6},
    {7,8,9},
    {1,4,7},
    {2,5,8},
    {3,6,9},
    {1,5,9},
    {3,5,7},
]

naughts_turn = False

cell_mapping: dict[tuple[int,int],int] = {
    (0,0) : 1,
    (0,1) : 2,
    (0,2) : 3,
    (1,0) : 4,
    (1,1) : 5,
    (1,2) : 6,
    (2,0) : 7,
    (2,1) : 8,
    (2,2) : 9,
}

button_tracker: dict[int, None | str] =  {
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