from game_logic import GameLogic

if __name__ == "__main__":
    test = GameLogic()
    test.print_welcome()
    choice = input("> ")
    if choice == "1":
        rolls = [(2, 2, 2, 2, 2, 2), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)]
    elif choice == "2":
        rolls = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
    elif choice == "3":
        rolls = [(4, 4, 5, 2, 3, 1)]
    else:
        rolls=[]

    mock_rollerd=test.mock_roller
    test.play_dice(mock_rollerd)