naught_placements = set()
cross_placements = set()

bg_colour = "#1E1E1E"

shape_colour_map = {
    "CROSSES": "#FFB766",
    "NAUGHTS": "#89CFF0"
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
