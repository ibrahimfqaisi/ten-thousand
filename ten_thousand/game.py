from game_logic import GameLogic

class play(GameLogic):
    """
    A class representing the gameplay logic for the Ten Thousand dice game.
    Inherits from the GameLogic class.
    """

    def print_welcome(self):
        """
        Prints the welcome message and available test file names.
        """

        print(
"""
Input the number of the test file you want to run or press Enter to proceed normally
Available test file names:
1)bank_first_for_two_rounds.sim --> input number 1
2)bank_one_roll_then_quit.sim --> input number 2
3)one_and_done.sim --> input number 3
4)To run the code normally --> press Enter
"""        
    )

    def play_dice(self, roller=GameLogic.roll_dice):
        """
        Plays the Ten Thousand dice game.

        Args:
            roller (function): A function to roll the dice.

        Returns:
            None
        """
        
        rounds = 0
        total_score = 0
        print(
"""Welcome to Ten Thousand
(y)es to play or (n)o to decline"""
        )
        choice = input("> ")

        if choice == "n":
            print("OK. Maybe another time")
            count="n"
        elif choice == "y":
            count="y"
        else:
            test.play_dice(mock_roller)
            

        while count=="y":

                rounds += 1
                print(f"Starting round {rounds}")
                print("Rolling 6 dice...")

                roll = roller()
                roll_str = " ".join(str(num) for num in roll)
                print(f"*** {roll_str} ***")
                unbanked_points = 0
                num_dice = 6

                while True:
                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")

                    if choice == "q":
                        print(f"\nThanks for playing. You earned {total_score} points")
                        return
                    else:
                        dice = tuple(map(int, choice))
                        score = self.calculate_score(dice)
                        if score==0:
                            
                            print(
                                f"You have {unbanked_points} unbanked points and {num_dice} dice remaining"
                            )
                        else:    
                            unbanked_points += score
                            num_dice -= len(dice)
                            print(
                                f"You have {unbanked_points} unbanked points and {num_dice} dice remaining"
                            )

                        if num_dice > 0:
                            print("(r)oll again, (b)ank your points or (q)uit:")
                            choice = input("> ")

                            if choice == "b":
                                total_score += unbanked_points
                                print(
                                    f"You banked {unbanked_points} points in round {rounds}"
                                )
                                print(f"Total score is {total_score} points")
                                break
                            elif choice == "q":
                                print(
                                    f"\nThanks for playing. You earned {total_score} points"
                                )
                                return
                            else:
                                print("Rolling remaining dice...")
                                roll = roller(num_dice)
                                roll_str = " ".join(str(num) for num in roll)
                                print(f"*** {roll_str} ***")
                        else:
                            total_score += unbanked_points
                            print(
                                f"You banked {unbanked_points} points in round {rounds}"
                            )
                            print(f"Total score is {total_score} points")
                            break


if __name__ == "__main__":
    
    test = play()
    test.print_welcome()
    choice = input("> ")

    if choice == "1":
        rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)] 
    elif choice == "2":
        rolls = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
    elif choice == "3":
        rolls = [(4, 4, 5, 2, 3, 1)]
    else:
        rolls=[]
    def mock_roller(number_of_dice=6):
        return rolls.pop(0) if rolls else test.roll_dice(number_of_dice)

    test.play_dice(mock_roller)