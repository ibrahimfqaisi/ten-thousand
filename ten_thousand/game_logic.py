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
    

