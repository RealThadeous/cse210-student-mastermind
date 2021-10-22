class Intro():
    """A code template for data to display as an introduction.
    
    Stereotype:
        Information Holder

    Attributes:
        self.info (string): A string containing a description of the game.
    """
    def __init__(self) -> None:
        """The class constructor.

        Args:
            self (Intro): an instance of Intro.
        """
        self._info = "Mastermind is a game in which each player seeks to guess the secret\n\
code they've been assigned before the other players do.\n\n\
    Rules of the game:\n\
    1. The code is a randomly generated, four digit number between 1000 and 9999.\n\
    2. The players take turns registering themselves by entering their name.\n\
    3. The players take turns guessing the secret code based on the hint that is offered:\n\
        - An x means a correct number in a correct position.\n\
        - An o means a correct number in an incorrect position.\n\
        - An * means an incorrect number.\n\
    4. If the guess is correct, the current player wins and the game is over.\n\
    5. If the guess is incorrect, a new hint is generated and play continues.\n"

        @property
        def info(self):
            return self._info

        @info.setter
        def info(self, info):
            self._info = info