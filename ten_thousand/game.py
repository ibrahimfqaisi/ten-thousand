from game_logic import GameLogic

if __name__ == "__main__":
    test = GameLogic()
    test.print_welcome()
    choice = input("> ")
    if choice == "1":
        rolls = [(1, 1, 1, 1, 1, 1), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)] 
    elif choice == "2":
        rolls = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
    elif choice == "3":
        rolls = [(4, 4, 5, 2, 3, 1)]
    else:
        rolls=[]
    
    def mock_roller(number_of_dice=6):
        return rolls.pop(0) if rolls else test.roll_dice(number_of_dice)

    mock_rollerd=test.mock_roller
    test.play_dice(mock_rollerd)