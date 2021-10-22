class Player:
    """A person taking part in a game. The responsibility of Player 
    is to keep track of their identity and the number of tries.
    
    Stereotype: 
        Information Holder

    Attributes:
        Encapsulated 
        __name (string): The player's name.
        _counter (int): The player's tries.
        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self.__name = "" 
        self._counter = 0

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            self.__name = name           

        @property
        def counter(self):
            return self._counter

        @counter.setter
        def counter(self, counter):
            self._counter = counter