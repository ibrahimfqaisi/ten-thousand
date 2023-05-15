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
                #  counts[die]    (1,0,5,0,2,0)
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
                score += (counts[die] - 2) * 200
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
        return  tuple (dice_roll)
         
