from game_logic import GameLogic

class paly(GameLogic):
    def play_dice(self, roller=GameLogic.roll_dice):
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
                            unbanked_points += score
                            
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
    
    test = paly()
    print(
"""
Input the name of the test file you want to run or press enter to proceed normaly
Available test file names:
1)bank_first_for_two_rounds.sim
2)bank_one_roll_then_quit.sim
3)one_and_done.sim
"""        
    )
    choice = input("> ")

    if choice == "bank_first_for_two_rounds.sim":
        rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)] 
    elif choice == "bank_one_roll_then_quit.sim":
        rolls = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
    elif choice == "one_and_done.sim":
        rolls = [(4, 4, 5, 2, 3, 1)]
    else:
        rolls=[]
    def mock_roller(number_of_dice=6):
        return rolls.pop(0) if rolls else test.roll_dice(number_of_dice)

    test.play_dice(mock_roller)