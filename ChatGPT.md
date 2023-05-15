## question to chatgpt :
- Define a GameLogic class in ten_thousand/ game_logic.py file.
- Handle calculating score for dice roll
    - Add calculate_score static method to GameLogic class.
    - The input to calculate_score is a tuple of integers that represent a dice roll.
    - The output from calculate_score is an integer representing the roll’s score according to rules of game.

## chatgpt answer

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


## question to chatgpt :
- Handle rolling dice
    - Add roll_dice static method to GameLogic class.
    - The input to roll_dice is an integer between 1 and 6.
    - The output of roll_dice is a tuple with random values between 1 and 6.
    - The length of tuple must match the argument given to roll_dice method.

## chatgpt answer

Sure! Here's an example dice rolling according to the given requirements:
```


dice_roll = []
for x in range(number_of_dice):
    dice_roll.append(random.randint(1, 6))
return  tuple (dice_roll)
```
### The roll_dice method takes an integer between 1 and 6, representing the number of dice to roll, and returns a tuple with random values between 1 and 6.


## * Afterward, we analyzed and dissected the code, making modifications to align it with the test files. We also added docstrings. 

