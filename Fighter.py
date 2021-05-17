from Person import Person
from Fight import Fight
import random
import KnightErrant


class Fighter(Person):
    """This is a class that defines a Fighter.

    Attributes:
        name(str): The name of the Fighter.
        age(int): The age of the Fighter.
        wealth(int): The wealth of the Fighter.
        'adult'(bool): Whether or not the Person is an adult. Is true.
        __skills(list): The list of skills that the Fighter has.
        requests_sent(list): Is a list of Fight objects that contain the challenges that this Fighter has sent.
    """
    # Initializing
    def __init__(self, name: str, age: int, wealth: int, spear: int, unarmed_combat: int, mace: int, broadsword: int)\
            -> None:
        """The constructor for the Fighter class.

        Parameters:
            name(str): The name of the Fighter.
            age(int): The age of the Fighter.
            wealth(int): The wealth of the Fighter.
            spear(int): The skill of this Fighter with the spear.
            unarmed_combat(int): The skill of this Fighter in unarmed combat.
            mace(int): The skill of this Fighter with the mace.
            broadsword(int): The skill of this Fighter with the broadsword.
        """
        if age < 18:
            print("This person cannot be a fighter! They are too young!")
        else:
            super().__init__(name, age, wealth)
            self.__skills = {'spear': spear, 'unarmed combat': unarmed_combat, 'mace': mace, 'broadsword': broadsword}
            self.requests_sent = []

    # Getter for skill value
    def get_skill_value(self, skill: str) -> int:
        """The getter function for the corresponding skill value.

        Parameters:
            skill(str): The skill that is being retrieved.

        Returns:
            The skill value.
            """
        return self.__skills[skill]

    def set_skill_value(self, skill: str, value: int) -> None:
        """This is a setter function for the skill value.

        Parameters:
            skill(str): The skill that is going to be set.
            value(int): The value that is going to be changed.
        """
        self.__skills[skill] = value

    # Challenge method
    def challenge(self, b: "KnightErrant", skill: str) -> None:
        """This is the challenge method from Fighter to Fighter, Fighter to Warrior, and Fighter to Knight.
        Follows the specifications in the Homework.

        Parameters:
            b('Warrior'): The Fighter apparent type that is being fought. Type annotations are weird, so I set it to a
            Knight.
            skill(str): The skill that will be utilized in the fight.
        """
        # Imports
        from Warrior import Warrior
        from KnightErrant import KnightErrant
        # Error Checking
        if self.error_checking(b):
            return None
        # Fighter to Fighter
        if type(b) is Fighter:
            fight = Fight(self, b, skill)
            winner = fight.winner()
            print(str(winner) + ' has won the fight!')
            self.normal_scenario(winner, b, skill)
            return None
        # Fighter to Warrior
        if type(b) is Warrior:
            if b.challenge_accepted is not None:
                winner = b.challenge_accepted.winner()
                print(str(winner) + ' has won the fight!')
                # Special warrior to fighter/fighter to warrior rules if fighter wins
                if type(winner) is Fighter:
                    # Rule # 1 and 2
                    if winner.get_skill_value(skill) < 10:
                        new_value = winner.get_skill_value(skill) + 1
                        winner.set_skill_value(skill, new_value)
                    winner.wealth += 25
                    if b.wealth <= 25:
                        b.wealth = 0
                    else:
                        b.wealth -= 25
                # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)
        # Fighter to KnightErrant
        if type(b) is KnightErrant:
            if b.challenge_accepted is not None:
                winner = b.challenge_accepted.winner()
                print(str(winner) + ' has won the fight!')
                # Special Fighter to KnightErrant to warrior rules if Fighter wins
                if type(winner) is Fighter:
                    # Rule # 1 and 2
                    if winner.get_skill_value(skill) < 9:
                        new_value = winner.get_skill_value(skill) + 2
                        winner.set_skill_value(skill, new_value)
                    elif winner.get_skill_value(skill) == 9:
                        new_value = 10
                        winner.set_skill_value(skill, new_value)
                    winner.wealth += 40
                    if b.wealth <= 40:
                        b.wealth = 0
                    else:
                        b.wealth -= 40
                # Normal scenario
                else:
                    self.normal_scenario(winner, b, skill)
                return None
            self.invitation(b, skill)

    def invitation(self, b: 'KnightErrant', skill: str) -> None:
        """This is the function that sends an invitation to the person that is being challenged and
        sends it into their inbox.

        Parameters:
            b('KnightErrant'): The Fighter apparent type that is being fought. Type annotations are weird, so I set it
                to a Knight.
            skill(str): The skill that will be utilized in the fight.
        """
        # Invitation
        fight = Fight(self, b, skill)
        if fight not in self.requests_sent:
            self.requests_sent.append(fight)
            b.requests_received.append(fight)
            print(str(self) + " has sent a fight request sent to " + str(b) + " with weapon " + skill +
                  ".")
            return None
        else:
            print(str(self) + " already has a formal challenge between them and " + str(b) + "!")
            return None

    def normal_scenario(self, winner: 'KnightErrant', b: 'KnightErrant', skill: str) -> None:
        """This is the function that acts as a normal Fighter/Fighter scenario.

        Parameters:
            b('KnightErrant'): The Fighter apparent type that is being fought.
            winner('KnightErrant'): The Fighter apparent type that won the fight.
            skill(str): The skill being used in the fight.
        """
        # Rule number 4
        winner.wealth += 10
        if b.__eq__(winner):
            if self.wealth > 10:
                self.wealth -= 10
            else:
                self.wealth = 0
        else:
            if b.wealth > 10:
                b.wealth -= 10
            else:
                b.wealth = 0
        # Rule number 5 for outside of fighter class
        increase_or_no = [0, 1]
        increase_challenged = random.choice(increase_or_no)
        increase_self = random.choice(increase_or_no)
        if b.get_skill_value(skill) < 10:
            new_value = increase_challenged + b.get_skill_value(skill)
            b.set_skill_value(skill, new_value)
        if self.get_skill_value(skill) < 10:
            new_value = increase_self + self.get_skill_value(skill)
            self.set_skill_value(skill, new_value)
        return None

    def error_checking(self, b: "KnightErrant") -> bool:
        """This is a function that checks if there are basic logical errors in the challenge methodology.

        Parameters:
            b('KnightErrant'): The object being compared.

        Returns:
            Whether or not there are logical errors in the challenge methodology.
        """
        if type(b) is Person:
            print("Why are you trying to fight a non-fighter?")
            return True
        if b.__eq__(self):
            print("Why are you trying to fight yourself?")
            return True
        if self.wealth == 0:
            print("You cannot fight! You have no money!")
            return True
        if b.wealth == 0:
            print("Your opponent has no money! They cannot fight!")
            return True
        return False

    def withdraw(self, b: 'KnightErrant', fight: 'Fight') -> None:
        """This is the function used to withdraw a challenge that a Fighter type has sent.

        Parameters:
            b('Person'): The other person that this person was supposed to fight.
            fight('Fight'): The fight that is going to be revoked.
        """
        if fight in self.requests_sent:
            self.requests_sent.remove(fight)
            b.requests_received.remove(fight)
            print(str(self) + " has revoked a fight request sent to " + str(b) + " with weapon " + fight.skill + ".")
            return None
        else:
            print("No formal challenge was ever dictated! There's nothing to withdraw.")
