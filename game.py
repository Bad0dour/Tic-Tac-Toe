naughts_turn = False

naught_placements = set()
cross_placements = set()

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

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

def placement(square: tuple[int,int]) -> None:
    if naughts_turn:
        print("Naught Placed")
        naught_placements.add(cell_mapping[square])
    else:
        print("Cross Placed")
        cross_placements.add(cell_mapping[square])