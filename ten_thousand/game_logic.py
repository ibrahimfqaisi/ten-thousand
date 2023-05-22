import random


class GameLogic:
    """
    A class representing game logic for a dice game.
    """

    @staticmethod
    def calculate_score(dice):
        """
        Calculates the score based on the dice values.

        Args:
            dice (tuple): A tuple of dice values.

        Returns:
            int: The calculated score.
        """
         
        score = 0
        counts = [0] * 7

        for die in dice:
            counts[die] += 1

        counter = 0
        for die in range(1, 7):
            if counts[die] == 1:
                counter += 1
            if counter == 6:
                score += 1500
                return score

        counter = 0
        for die in range(1, 7):
            if counts[die] == 2:
                counter += 1
            if counter == 3:
                score += 1500
                return score
        list_check=[2,3,4,6]
        count_check=0
        for x in list_check :
            
            if counts[x]<3 :
                count_check+= counts[x]
        
               
        if counts[1] >= 3:
            score += (counts[1] - 2) * 1000
        elif counts[1] > 0:
            score += counts[1] * 100

        if counts[5] == 3:
            score += 500
            counts[5] = 0

        if 0 < counts[5] < 3:
            score += counts[5] * 50
            counts[5] = 0

        for die in range(2, 7):
            if counts[die] >= 3:
                score += (counts[die] - 2) * 100 * die
                counts[die] -= 3

        return score ,count_check

    @staticmethod
    def roll_dice(number_of_dice):
        """
        Rolls a specified number of dice and returns the values.

        Args:
            number_of_dice (int): The number of dice to roll.

        Returns:
            tuple: A tuple of dice values.
        """
                
        dice_roll = []
        for _ in range(number_of_dice):
            dice_roll.append(random.randint(1, 6))
        return tuple(dice_roll)
    
    def validate_keepers(self,digits,roll_2,roll_str=0):
        check=1
        for x in digits :
            if x in roll_2 :
                roll_2.remove(x)
                
            else:
                print("Cheater!!! Or possibly made a typo...")
                check=-1
                print(f"*** {roll_str} ***")
                return 
        if check ==1:
            return True
        else :
            return False     
                            


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
      
    def mock_roller(self,number_of_dice=6):
        rolls=[] 
        return rolls.pop(0) if rolls else self.roll_dice(number_of_dice)
    def play_dice(self, roller=roll_dice):
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
            self.play_dice(self.mock_roller)
            
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
                    if num_dice!=6 and self.calculate_score(roll)[0]==0:
                        unbanked_points=0
                        print('''
****************************************
**        Zilch!!! Round over         **
****************************************''')
                        print(f"You banked {unbanked_points} points in round {rounds}")
                        break
                    elif num_dice==6 and self.calculate_score(roll)[0]==0:
                        print(f"Starting round {rounds}")
                        print("Rolling 6 dice...")                        
                        roll = roller()
                        roll_str = " ".join(str(num) for num in roll)
                        print(f"*** {roll_str} ***")                        
                    else :
                           
                        print("Enter dice to keep, or (q)uit:")
                        choice = input("> ")
                        if choice == "q":
                            print(f"\nThanks for playing. You earned {total_score} points")
                            return
                        else:
                            digits = list(int(digit) for digit in str(choice))
                            roll_2=list(roll)
                            check=1
                            
                            if self.validate_keepers(digits,roll_2,roll_str)==  True:
                                dice = tuple(map(int, choice))
                                score = self.calculate_score(dice)[0]
                                count_check = self.calculate_score(dice)[1]
                                if score==0:
                                    print(
                                        f"You have {unbanked_points} unbanked points and {num_dice} dice remaining"
                                    )
                                else:
                                    unbanked_points += score
                                    num_dice -= len(dice)
                                    num_dice+= count_check
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
                                        print(f"Rolling {num_dice} dice...")
                                        roll = roller(num_dice)
                                        roll_str = " ".join(str(num) for num in roll)
                                        print(f"*** {roll_str} ***")
                                else:
                                    print(f"Starting round {rounds}")
                                    print("Rolling 6 dice...")
                                    roll = roller()
                                    roll_str = " ".join(str(num) for num in roll)
                                    print(f"*** {roll_str} ***")
                                    num_dice = 6
                                    print(
                                        f"You banked {unbanked_points} points in round {rounds}"
                                    )