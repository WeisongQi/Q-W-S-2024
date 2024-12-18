# Spiel Schere Stein Papier
import random

wahl_sum = ["Schere", "Stein", "Papier"]


def player_input():
    spiel_ab = input("Spielen ? y/n : ")
    if spiel_ab.lower() == "y":
        player_wahl = input("Schere or Stein or Papier : ")
        if player_wahl in wahl_sum:
            # print(f"{player_wahl}")
            return player_wahl
        else:
            print("error")
            return player_input()
    else:
        return None


""" def com_player():
    com_wahl = random.choice(wahl_sum)
    print(com_wahl)
    return com_wahl """


# Main


def main():
    rules = {"Schere": "Papier", "Papier": "Stein", "Stein": "Schere"}
    player_wins = 0
    computer_wins = 0
    tie = 0
    while True:
        player_choice = player_input()
        if player_choice is None:
            break
        com_player = random.choice(wahl_sum)
        # print(f"Computer wählt : {com_player}")

        # win ?
        if com_player == player_choice:
            print("draw")
            gleich += 1
        elif rules[player_choice] == com_player:
            print("Player win")
            player_wins += 1
        else:
            print("Computer Win")
            computer_wins += 1
        print(
            f"Aktueller Spielstand-Spieler: {player_wins} |Computer:{computer_wins} |draw:{tie}"
        )


main()
