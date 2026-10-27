from win_combos import win_combos

def main():

    naught_placements = set()
    cross_placements = set()
    
    def add_placement(shape: str, square: int) -> None:
        if shape == "naught":
            naught_placements.add(square)
        else:
            cross_placements.add(square)
    
    for combo in win_combos:
        if combo.issubset(naught_placements):
            print("NAUGHTS WINS")
        elif cross_placements == combo:
            print("CROSSES WINS")

if __name__ == "__main__":
    main()
