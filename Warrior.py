from Fight import Fight
from Fighter import Fighter
import random
import KnightErrant


class Warrior(Fighter):
    """This is a class that defines a Warrior.

    Attributes:
        name(str): The name of the Warrior.
        age(int): The age of the Warrior.
        wealth(int): The wealth of the Warrior.
        'adult'(bool): Whether or not the Warrior is an adult. Is automatically true.
        'skills'(list): The list of skills that the Warrior has.
        requests_sent(list): Is a list of Fight objects that contain the challenges that this Warrior has sent.
        requests_received(list): Is a list of Fight objects that contain the challenges that this Warrior has received.
        challenge_accepted(bool): Tells you whether or not this Warrior has engaged in combat or not. Changes
            the overall control flow of the challenge method.
    """
    # Initializing
    def __init__(self, name: str, age: int, wealth: int, spear: int, unarmed_combat: int, mace: int, broadsword: int):
        """The constructor for the Warrior class.

        Parameters:
            name(str): The name of the Warrior.
            age(int): The age of the Warrior.
            wealth(int): The wealth of the Warrior.
            spear(int): The skill of this Warrior with the spear.
            unarmed_combat(int): The skill of this Warrior in unarmed combat.
            mace(int): The skill of this Warrior with the mace.
            broadsword(int): The skill of this Warrior with the broadsword.
        """
        if age < 18:
            print("This person cannot be a fighter! They are too young!")
        else:
            super().__init__(name, age, wealth, spear, unarmed_combat, mace, broadsword)
            self.requests_sent = []
            self.requests_received = []
            self.challenge_accepted = None

    def challenge(self, b: "KnightErrant", skill: str) -> None:
        """This is the challenge method from Warrior to Fighter, Warrior to Warrior, and Warrior to Knight.
        Follows the specifications in the Homework.

        Parameters:
            b('KnightErrant'): The Fighter apparent type that is being fought. Type annotations are weird, so I set it to a
             Knight.
            skill(str): The skill that will be utilized in the fight.
        """
        # Imports
        from KnightErrant import KnightErrant
        # Error Checking
        if self.error_checking(b):
            return None
        # Error checking. If the challenged is a fighter and a request was already sent to the challenger... error.
        # Warrior to Fighter
        if type(b) is Fighter:
            fight = Fight(b, self, skill)
            if fight in self.requests_received:
                print(str(self) + " already has a formal challenge between them and " + str(b) + "!")
            else:
                winner = fight.winner()
                print(str(winner) + ' has won the fight!')
                # Special warrior to fighter rules if fighter wins
                if type(winner) is Fighter:
                    # Rule # 1 and 2
                    if winner.get_skill_value(skill) < 10:
                        new_value = winner.get_skill_value(skill) + 1
                        winner.set_skill_value(skill, new_value)
                    winner.wealth += 25
                    if self.wealth <= 25:
                        self.wealth = 0
                    else:
                        self.wealth -= 25
                # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
        # Warrior to Warrior
        if type(b) is Warrior:
            if b.challenge_accepted is not None:
                winner = b.challenge_accepted.winner()
                print(str(winner) + ' has won the fight!')
                self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)
        # Warrior to KnightErrant
        if type(b) is KnightErrant:
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
                    if b.wealth <= 20:
                        b.wealth = 0
                    else:
                        b.wealth -= 20
                # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)

    def decline_random(self) -> None:
        """A method used for declining a random challenge request."""
        if not self.requests_received:
            print("There is nothing to decline for " + str(self) + ".")
            return None
        fight = random.choice(self.requests_received)
        self.requests_received.remove(fight)
        fight.fighter_challenger.requests_sent.remove(fight)
        print("The " + str(fight) + " has been declined by " + str(self) + ".")

    def decline_first(self) -> None:
        """A method used for declining the first challenge request in their inbox."""
        fight = next(iter(self.requests_received or []), None)
        if fight is None:
            print("There is nothing to decline for " + str(self) + ".")
            return None
        else:
            self.requests_received.remove(fight)
            fight.fighter_challenger.requests_sent.remove(fight)
            print("The " + str(fight) + " has been declined by " + str(self) + ".")

    def accept_random(self) -> None:
        """A method used for accepting a random challenge request in their inbox."""
        # Imports
        from KnightErrant import KnightErrant
        if type(self) is KnightErrant:
            if self.traveling:
                print("The Knight Errant " + str(self) + " is traveling! They cannot accept a challenge.")
                return None
        if not self.requests_received:
            print("There is nothing to accept " + str(self) + ".")
            return None
        print(self.name + " is accepting a random challenge.")
        fight = random.choice(self.requests_received)
        self.requests_received.remove(fight)
        fight.fighter_challenger.requests_sent.remove(fight)
        print("The " + str(fight) + " has been accepted by " + str(self) + ".")
        self.challenge_accepted = fight
        fight.fighter_challenger.challenge(fight.fighter_challenged, fight.skill)
        self.challenge_accepted = None

    def accept_first(self: 'KnightErrant') -> None:
        """A method used for accepting the first challenge request in their inbox."""
        # Imports
        from KnightErrant import KnightErrant
        if type(self) is KnightErrant:
            if self.traveling:
                print("The Knight Errant " + str(self) + " is traveling! They cannot accept a challenge.")
                return None
        fight = next(iter(self.requests_received or []), None)
        if fight is None:
            print("There is nothing to accept for " + str(self) + ".")
            return None
        else:
            self.requests_received.remove(fight)
            fight.fighter_challenger.requests_sent.remove(fight)
            print("The " + str(fight) + " has been accepted by " + str(self) + ".")
            self.challenge_accepted = fight
            fight.fighter_challenger.challenge(fight.fighter_challenged, fight.skill)
            self.challenge_accepted = None
