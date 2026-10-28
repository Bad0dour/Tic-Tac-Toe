from win_combos import win_combos
from app import naught_placements, cross_placements

for combo in win_combos:
    if combo.issubset(naught_placements):
        print("NAUGHTS WINS!")
    elif cross_placements == combo:
        print("CROSSES WINS!")
