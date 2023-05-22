# Ten Thousand version01:

## question to Chatgpt:

- Define a GameLogic class in ten_thousand/ game_logic.py file.
- Handle calculating score for dice roll
  - Add calculate_score static method to GameLogic class.
  - The input to calculate_score is a tuple of integers that represent a dice roll.
  - The output from calculate_score is an integer representing the roll’s score according to rules of game.

## Chatgpt answer:

Sure! Here's an example implementation of the GameLogic class in the ten_thousand/game_logic.py file that handles scoring and dice rolling according to the given requirements:

```

import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = [0] * 7  # Initialize counts for each dice face (1 to 6)
        for dice in dice_roll:
            counts[dice] += 1

        # Calculate score based on counts
        if counts[1] >= 3:
            score += 1000
            counts[1] -= 3
        elif counts[1] > 0:
            score += 100 * counts[1]

        for i in range(2, 7):
            if counts[i] >= 3:
                score += i * 100
                counts[i] -= 3

        score += counts[1] * 100  # Add remaining 1's
        score += counts[5] * 50  # Add remaining 5's

        return score

```

### In this implementation, the calculate_score method takes a tuple of integers representing a dice roll and calculates the score based on the rules of the game.

## question to Chatgpt:

- Handle rolling dice
  - Add roll_dice static method to GameLogic class.
  - The input to roll_dice is an integer between 1 and 6.
  - The output of roll_dice is a tuple with random values between 1 and 6.
  - The length of tuple must match the argument given to roll_dice method.

## Chatgpt answer:

Sure! Here's an example dice rolling according to the given requirements:

```
dice_roll = []
for x in range(number_of_dice):
    dice_roll.append(random.randint(1, 6))
return  tuple (dice_roll)
```

### The roll_dice method takes an integer between 1 and 6, representing the number of dice to roll, and returns a tuple with random values between 1 and 6.

</br>

## \* Afterward, we analyzed and dissected the code, making modifications to align it with the test files. We also added docstrings.

</br></br>

# Ten Thousand version02:

## question to Chatgpt :

i have this code :

```
import random
class GameLogic:
    """
    A class representing game logic for a dice game.
    Attributes:
        None
    Methods:
        calculate_score(dice): Calculates the score based on the dice values.
        roll_dice(number_of_dice): Rolls a specified number of dice and returns the values.
    """
    @staticmethod
    def calculate_score(dice):
        """
        Calculates the score based on the dice values.
        Args:
            dice (list): A list of dice values.
        Returns:
            int: The calculated score.
        Example:
            calculate_score([1, 2, 3, 3, 3])  # Returns 300
        """
        score = 0
        counts = [0] * 7  # Initialize counts for each possible dice value
                #  dice(5,1,5)
                #  die            {1,2,3,4,5,6}
                #  counts[die]    (0,0,0,0,0,0)
        # Count the occurrences of each dice value
        for die in dice:
            counts[die] += 1
        # Check if all six dice have different values
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
        # Calculate score for ones
        if counts[1] >= 3:
            score += (counts[1] - 2) * 1000
        elif counts[1] > 0:
            score += counts[1] * 100
        # Score for three fives
        if counts[5] == 3:
            score += 500
            counts[5] = 0
        # Score for individual fives
        if counts[5] > 0 and counts [5]<3  :
            score += counts[5] * 50
            counts[5] = 0
        # Calculate score for other values (excluding ones)
        for die in range(2, 7):
            # Score for three of a kind
            if counts[die] >= 3:
                score += (counts[die] - 2) * 100* die
                counts[die] -= 3
        return score
    @staticmethod
    def roll_dice(number_of_dice):
        """
        Rolls a specified number of dice and returns the values.
        Args:
            number_of_dice (int): The number of dice to roll.
        Returns:
            list: A list of dice values.
        Example:
            roll_dice(3)  # Returns [2, 4, 6]
        """
        dice_roll = []
        for x in range(number_of_dice):
            dice_roll.append(random.randint(1, 6))
            # print (tuple (dice_roll))
        return  tuple (dice_roll)
    def play_dice(self,roller=roll_dice):
        while True:
            choice = input("> ")
            if choice == "n":
                print("OK. Maybe another time")
                break
            elif choice == "y":
                print("""
Starting round 1
Rolling 6 dice...""")
                choice = input("> ")
                roll = roller()
                roll_str = ""
                for num in roll:
                    roll_str += str(num) + " "
                print(f"*** {roll_str}***")
                # choice = input("> ")
                # roll = self.roll_dice(int(choice))
                # roll_str = ""
                # for num in roll:
                #     roll_str += str(num) + " "
                # print(f"*** {roll_str}***")
if __name__ == "__main__":
    test =GameLogic()
    rolls = [(3,2,5,4,3,3)]
    print('''
Welcome to Ten Thousand
(y)es to play or (n)o to decline
''')
    def mock_roller():
        return rolls.pop(0) if rolls else test.roll_dice(int(6))
    test.play_dice(mock_roller)
```

i want the output to be like this:

```
Welcome to Ten Thousand
(y)es to play or (n)o to decline
> y
Starting round 1
Rolling 6 dice...
*** 3 2 5 4 3 3 ***
Enter dice to keep, or (q)uit:
> 3335
You have 350 unbanked points and 2 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 350 points in round 1
Total score is 350 points
Starting round 2
Rolling 6 dice...
*** 5 2 3 2 1 4 ***
Enter dice to keep, or (q)uit:
> 15
You have 150 unbanked points and 4 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 150 points in round 2
Total score is 500 points
Starting round 3
Rolling 6 dice...
*** 6 6 5 4 2 1 ***
Enter dice to keep, or (q)uit:
> q
Thanks for playing. You earned 500 points
```

## Chatgpt answer:

To achieve the desired output, you can modify the play_dice method in the GameLogic class. Here's an updated version of the code that produces the expected output:

```
class GameLogic:
    # ...existing code...

    def play_dice(self, roller=roll_dice):
        rounds = 0
        total_score = 0
        print('''
        Welcome to Ten Thousand
        (y)es to play or (n)o to decline
        ''')
        while True:
            choice = input("> ")
            if choice == "n":
                print("OK. Maybe another time")
                break
            elif choice == "y":
                rounds += 1
                print(f"\nStarting round {rounds}")
                print("Rolling 6 dice...")
                choice = input("> ")
                roll = roller()
                roll_str = ""
                for num in roll:
                    roll_str += str(num) + " "
                print(f"*** {roll_str}***")
                unbanked_points = 0
                num_dice = 6

                while True:
                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")
                    if choice == "q":
                        print(f"\nThanks for playing. You earned {total_score} points")
                        return
                    else:
                        # Calculate the score for the selected dice
                        dice = tuple(map(int, choice))
                        score = self.calculate_score(dice)
                        unbanked_points += score

                        num_dice -= len(dice)
                        print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")

                        if num_dice > 0:
                            print("(r)oll again, (b)ank your points or (q)uit:")
                            choice = input("> ")
                            if choice == "b":
                                total_score += unbanked_points
                                print(f"You banked {unbanked_points} points in round {rounds}")
                                print(f"Total score is {total_score} points")
                                break
                            elif choice == "q":
                                print(f"\nThanks for playing. You earned {total_score} points")
                                return
                            else:
                                print("Rolling remaining dice...")
                                roll = roller(num_dice)
                                roll_str = ""
                                for num in roll:
                                    roll_str += str(num) + " "
                                print(f"*** {roll_str}***")
                        else:
                            total_score += unbanked_points
                            print(f"You banked {unbanked_points} points in round {rounds}")
                            print(f"Total score is {total_score} points")
                            break

if __name__ == "__main__":
    test = GameLogic()
    rolls = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)]

    def mock_roller(number_of_dice=6):
        return rolls.pop(0) if rolls else test.roll_dice(number_of_dice)

    test.play_dice(mock_roller)
```

This modified code simulates the game rounds, keeps track of the total score, and handles user input for dice selection, banking points, and quitting the game. The loop continues until the user chooses to quit, and at the end of each round, the score is updated and displayed.
</br>

## \* Afterward, we analyzed and dissected the code, making modifications to align it with the test files. We also added docstrings and we also injected three questions to ask the user to enter the test he prefer to use.



 # Ten Thousand 3: 
 we didnt use chat gpt 