from Fighter import Fighter
from Warrior import Warrior
import random


class KnightErrant(Warrior):
    """This is a class that defines a Knight Errant.

        Attributes:
            name(str): The name of the Knight.
            age(int): The age of the Knight.
            wealth(int): The wealth of the Knight.
            'adult'(bool): Whether or not the Knight is an adult. Is automatically true.
            'skills'(list): The list of skills that the Knight has.
            requests_sent(list): Is a list of Fight objects that contain the challenges that this Knight has sent.
            requests_received(list): Is a list of Fight objects that contain the challenges that this Knight has received.
            challenge_accepted('Fight'): Tells you whether or not this Knight has engaged in combat or not. Changes
                the overall control flow of the challenge method.
            traveling(bool): Tells you whether or not the Knight is traveling or not.
        """
    def __init__(self, name: str, age: int, wealth: int, spear: int, unarmed_combat: int, mace: int, broadsword: int):
        """The constructor for the Knight Errant class.

        Parameters:
            name(str): The name of the Knight.
            age(int): The age of the Knight.
            wealth(int): The wealth of the Knight.
            spear(int): The skill of this Knight with the spear.
            unarmed_combat(int): The skill of this Knight in unarmed combat.
            mace(int): The skill of this Knight with the mace.
            broadsword(int): The skill of this Knight with the broadsword.
        """
        if age < 18:
            print("This person cannot be a fighter! They are too young!")
        else:
            super().__init__(name, age, wealth, spear, unarmed_combat, mace, broadsword)
            self.requests_sent = []
            self.requests_received = []
            self.challenge_accepted = None
            self.traveling = False

    def challenge(self, b: "KnightErrant", skill: str) -> None:
        """This is the challenge method from KnightErrant to Fighter, KnightErrant to Warrior, and KnightErrant to
            KnightErrant. Follows the specifications in the Homework.

            Parameters:
                b('KnightErrant'): The Fighter apparent type that is being fought. Type annotations are weird, so I set
                    it to a Knight.
                skill(str): The skill that will be utilized in the fight.
        """
        # Imports
        from Fight import Fight
        # Error Checking
        if self.error_checking(b):
            return None
        # KnightErrant to Fighter
        if type(b) is Fighter:
            if self.traveling:
                print("The Knight Errant " + str(self) + " is traveling! They cannot challenge anyone.")
                return None
            fight = Fight(b, self, skill)
            if fight in self.requests_received:
                print(str(self) + " already has a formal challenge between them and " + str(b) + "!")
            else:
                winner = fight.winner()
                print(str(winner) + ' has won the fight!')
                # Special warrior to fighter rules if fighter wins
                if type(winner) is Fighter:
                    # Rule # 1 and 2
                    if winner.get_skill_value(skill) < 9:
                        new_value = winner.get_skill_value(skill) + 2
                        winner.set_skill_value(skill, new_value)
                    elif winner.get_skill_value(skill) == 9:
                        new_value = 10
                        winner.set_skill_value(skill, new_value)
                    winner.wealth += 40
                    if self.wealth <= 40:
                        self.wealth = 0
                    else:
                        self.wealth -= 40
                    # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
                return None
        # KnightErrant to Warrior
        if type(b) is Warrior:
            if self.traveling:
                print("The Knight Errant " + str(self) + " is traveling! They cannot challenge anyone.")
                return None
            if b.challenge_accepted is not None:
                winner = b.challenge_accepted.winner()
                print(str(winner) + ' has won the fight!')
                # Special Warrior to KnightErrant/KnightErrant to warrior rules if fighter wins
                if type(winner) is Warrior:
                    # Rule # 1 and 2
                    if winner.get_skill_value(skill) < 10:
                        new_value = winner.get_skill_value(skill) + 1
                        winner.set_skill_value(skill, new_value)
                    winner.wealth += 20
                    if self.wealth <= 20:
                        self.wealth = 0
                    else:
                        self.wealth -= 20
                # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)
        # KnightErrant to KnightErrant
        if type(b) is KnightErrant:
            if self.traveling:
                print("The Knight Errant " + str(self) + " is traveling! They cannot challenge anyone.")
                return None
            if b.challenge_accepted is not None:
                winner = b.challenge_accepted.winner()
                print(str(winner) + ' has won the fight!')
                self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)

    def travel(self) -> None:
        """This is the function for when the Knight goes traveling."""
        print("The Knight Errant " + str(self) + " has started their travels!")
        self.traveling = True

    def return_from_travel(self) -> None:
        """This is the function for when the Knight is finished traveling."""
        print("The Knight Errant " + str(self) + " has returned from travel!")
        treasure_or_no = random.randint(1, 11)
        treasure = random.randint(1, 101)
        # 20% chance of finding treasure.
        if treasure_or_no >= 3:
            print("The Knight Errant " + str(self) + " didn't find any treasure!")
            self.traveling = False
            return None
        else:
            print("The Knight Errant " + str(self) + " found treasure worth " + str(treasure) + "!")
            self.traveling = False
            self.wealth += treasure
