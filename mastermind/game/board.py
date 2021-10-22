import random

class Board:
    """A board is the designated playing surface. The responsibility of Board
    is to display the guessed numbers and hints for all players.
    
    Stereotype: 
        Information Holder
    Attributes:
        self._items (dict): A dictionary containing the code, guess, and hint of
                            all the players.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        Attributes:
            items: dictionary
        """
        self._items = {}
        
        
    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            player (): contains player data
        Attributes:
            name: variable to store player input
            code(string): holds random number between 1000 - 10000 
        """
        name = player
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]


    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.
        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.
        Returns:
            string: A hint in the form [xxxx]
        """
        hint = ""
        for index, letter in enumerate(str(guess)):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint


    def apply_hint(self, player, hint):
        """The apply method applies a hint to the playing surface. 
        Args:
            self(Board): an instance of Board.
            player(string): contains player data
            hint (string): hint for the player
        """
        self._items[player][2] = hint
        
    
    def _is_same_code(self, player):
        """checks if the player data is the same
        Args:
            self(Board): an instance of board
            player(string): contains player data
        """                         

        if self._items[player][0] == self._items[player][1]:
            return True
        else:
            return False


    def to_string(self):
        """The to_string method converts the board data to its 
        string representation and returns it to the caller.
        Args:
            self (Board): an instance of Board.
        """
        line, text, board = "", "", ""
        for item in self._items:
            text += "Player " + item + ": " + \
                self._items[item][1] + ", " + self._items[item][2] + "\n"

        line += "-" * (len(text)//2) + "\n"
        board = line + text + line
                
        return board