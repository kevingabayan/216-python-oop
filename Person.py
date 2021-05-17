class Person:
    """This is a class that defines a Person.

    Attributes:
        name(str): The name of the Person.
        age(int): The age of the Person.
        wealth(int): The wealth of the Person.
        adult(bool): Whether or not the Person is an adult.
    """
    # Constructor
    def __init__(self, name: str, age: int = 0, wealth: int = 0) -> None:
        """The constructor for the Person class.

        Parameters:
            name(str): The name of the Person.
            age(int): The age of the Person.
            wealth(int): The wealth of the Person.
        """
        self.name = name
        self.age = age
        self.wealth = wealth
        if self.age >= 18:
            self.adult = True
        else:
            self.adult = False

    # Name plus age combination
    def __str__(self) -> str:
        """The function that returns the name and age when the Person object is called.

        Returns:
            Name, Age
        """
        return self.name + ", " + str(self.age)

    # Equality check
    def __eq__(self, other: 'Person') -> bool:
        """The function that redefines the equality function to allow == to be used.

        Returns:
            Whether or not the two Persons are equal.
            """
        return self.__dict__ == other.__dict__
