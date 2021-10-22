class Check:
    """A code template for an object of the class Check. The responsibility of Check
    is to make sure the user's input is correct. 
    
    Stereotype: 
        Information Holder

    Attributes:
        self.__okay (boolean): Default to True, return False 
                                when conditions not met.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Check): an instance of Check.
        """
        self.__okay = True

    def _compare_codes(self, player, board):
        """Compares the secret code with the guess

        Args:
            self (Check): An instance of Check.
            player (Player): An instance of Player.
            board (Board): And instance of Board.

        Returns:
            __okay (boolean): True if both values match. False otherwise.
        """
        if board._items[player][0] == board._items[player][1]:
            return self.__okay
        else:
            return not self.__okay

    def _check_input(self, guess):
        """Checks if the input is a number of 4 digits.

        Args:
            self (Check): An instance of Check.
            guess (string): A string with user's guess.

        Returns:
            __okay (boolean): True if guess complies. False otherwise.
        """
        for digit in guess:
            if not digit.isdigit():
                print("\nHint: Only digits accepted.")
                return not self.__okay

        if len(guess) != 4:
            print(f"\nHint: You must enter 4 digits.")
            return not self.__okay

        return self.__okay
