import random
class GameLogic:
    """
    A class representing game logic for a dice game.
    """
    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scorers.append(val)
        return tuple(scorers)

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
        
        # def get_scorers(self,dice):
            
        list_check = [2, 3, 4, 6]
        global count_check
        count_check = 0

        for x in list_check:
            if counts[x] < 3:
                count_check += counts[x]
            # else:
            #         for x in range(counts[x]):
            #             scorer.append(x)
            # return tuple(scoyrer)
        # get_scorers(dice)
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
        return score
    def mock_roller(self, number_of_dice=6):
        rolls = []
        return self.roll_dice(number_of_dice)
    @staticmethod
    def quitOrBank(total_score,unbanked_points,rounds):
        print("(r)oll again, (b)ank your points or (q)uit:")
        choice = input("> ")
        if choice == "b":
            total_score += unbanked_points
            print(f"You banked {unbanked_points} points in round {rounds}")
            print(f"Total score is {total_score} points")
        
            return "b",total_score
        elif choice == "r":
            return "r",total_score            
        elif choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            return "q",total_score
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
    @staticmethod
    def validate_keepers(roll_2, digits, roll_str=0):
        check = 1
        digits = list(digits)
        roll_2 = list(roll_2)
        if digits ==[]:
            print(f"*** {roll_str} ***")
            return False
        else:
            for x in digits:
                if x in roll_2:
                    roll_2.remove(x)
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    check = -1
                    print(f"*** {roll_str} ***")
                    return False
            if check == 1:
                return True


    def play_dice(self, roller=None):
        """
        Plays the Ten Thousand dice game.
        Args:
            roller (function): A function to roll the dice.
        Returns:
            None
        """
        rounds = 0
        total_score = 0
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        choice = input("> ")
        if choice == "n":
            print("OK. Maybe another time")
            count = "n"
        elif choice == "y":
            count = "y"
        else:
            self.play_dice(self.mock_roller)
            return
        while count == "y":
            rounds += 1
            # if rounds ==2:
            #     print(f"Thanks for playing. You earned {total_score} points")
                
            print(f"Starting round {rounds}")
            print("Rolling 6 dice...")
            roll = self.roll_dice(6)  # Call the static method with 6 dice
            roll_str = " ".join(str(num) for num in roll)
            print ("*** {} ***".format(" ".join(str(num) for num in roll)))
            # print(f"*** {roll_str} ***")
            unbanked_points = 0
            num_dice = 6
            while True:
                if num_dice <= 6 and self.calculate_score(roll) == 0:
                    unbanked_points = 0
                    print('''
****************************************
**        Zilch!!! Round over         **
****************************************''')
                    print(f"You banked {unbanked_points} points in round {rounds}")
                    break
                # elif num_dice == 6 and self.calculate_score(roll) == 0:
                #     print(f"Starting round {rounds}")
                #     print("Rolling 6 dice...")
                #     roll = self.roll_dice(6)
                #     roll_str = " ".join(str(num) for num in roll)
                #     print(f"*** {roll_str} ***")
                else:
                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")
                    if rounds >20:
                        choice="q"
                    if choice == "q":
                        print(f"Thanks for playing. You earned {total_score} points")
                        return
                    else:
                        roll_2 = list(int(digit) for digit in str(choice))
                        digits = list(roll)
                        check = 1
                        if self.validate_keepers(digits, roll_2, roll_str) is True:
                            dice = tuple(map(int, choice))
                            score = self.calculate_score(dice)
                            if score == 0:
                                print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
                            else:
                                unbanked_points += score
                                num_dice -= len(dice)
                                num_dice += count_check
                                if num_dice !=0 :
                                    
                                    print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
                            if num_dice > 0:
                                my_check=self.quitOrBank(total_score,unbanked_points,rounds)
                                total_score=my_check[1]
                                if my_check[0] =="b":
                                    break
                                elif my_check[0] =="q":
                                    return
                                
                                else:
                                    print(f"Rolling {num_dice} dice...")
                                    roll = self.roll_dice(num_dice)
                                    roll_str = " ".join(str(num) for num in roll)
                                    print(f"*** {roll_str} ***")
                            else:
                                num_dice = 6
                                print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
                                my_check=self.quitOrBank(total_score,unbanked_points,rounds)
                                if my_check[0] =="b":
                                    break
                                elif my_check[0] =="q":
                                    return
                                print("Rolling 6 dice...")
                                roll = self.roll_dice(6)
                                roll_str = " ".join(str(num) for num in roll)
                                print(f"*** {roll_str} ***")
if __name__ == "__main__":
    h=GameLogic()
    h.play_dice()


