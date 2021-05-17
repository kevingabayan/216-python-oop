import Fighter
import random


class Fight:
    """
    This is a class that simulates the groundwork for a Fight between two apparent Fighters.

    Attributes:
        fighter_challenger(Fighter): The challenger for the fight.
        fighter_challenged(Fighter): The fighter being challenged.
        skill(str): The skill being used for the fight.
    """
    def __init__(self, a: Fighter, b: Fighter, skill: str):
        """A basic constructor method for a Fight."""
        self.fighter_challenger = a
        self.fighter_challenged = b
        self.skill = skill

    # String conversion
    def __str__(self) -> str:
        """The function that returns the challenge invitation details.

        Returns:
            The challenge invitation from challenged to challenger.
        """
        return "challenge invitation from " + str(self.fighter_challenger) + " to " + \
               str(self.fighter_challenged) + " with the skill " + self.skill

    def __eq__(self, other: "Fight") -> bool:
        """The function used for equality checking.
        Parameters:
            other(Fight): The object to be compared.

        Returns:
            Whether or not the two objects are equal.
            """
        return self.__dict__ == other.__dict__

    def winner(self) -> Fighter:
        """The function that determines the winner of the fight.

        Returns: The winner of the fight."""
        skill_challenger = self.fighter_challenger.get_skill_value(self.skill)
        skill_challenged = self.fighter_challenged.get_skill_value(self.skill)
        # If both and b have the same level, the winner is determined by luck.
        if skill_challenger == skill_challenged:
            luck = [self.fighter_challenger, self.fighter_challenged]
            return random.choice(luck)
        elif skill_challenger > skill_challenged:
            return self.fighter_challenger
        else:
            return self.fighter_challenged
