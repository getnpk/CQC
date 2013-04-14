class CashRegister():
    """
    Simple cash register
    """
    def __init__(self, loonies, toonies, fives, tens, twenties):
        """
        (CashRegister, int, int, int, int, int) -> NoneType

        >>> register = CashRegister(5,5,5,5,5)
        >>> register.loonies
        5
        >>> register.toonies
        5
        >>> register.fives
        5
        >>> register.tens
        5
        >>> register.twenties
        5
        """
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __eq__(self, other):
        """
        (CashRegister, CashRegister) -> bool
        >>> reg1 = CashRegister(2,0,0,0,0)
        >>> reg2 = CashRegister(0,1,0,0,0)
        >>> reg1 == reg2
        True
        
        """
        return self.getTotal() == other.getTotal()

    def __str__(self):
        return 'CashRegister: ' + \
                '${0} ($1x{1} $2x{2} $5x{3} $10x{4} $20x{5}'\
                     .format(self.getTotal(), self.loonies, self.toonies, \
                             self.fives, self.tens, self.twenties)
        
    def getTotal(self):
        """
        (CashRegister) -> int
        >>> register = CashRegister(5,5,5,5,5)
        >>> register.getTotal()
        190

        """
        return self.loonies + self.toonies * 2 + self.fives * 5 + \
               self.tens * 10 + self.twenties * 20

    def add(self, count, denomination):
        """
        (CashRegister, int, string) -> NoneType
        """
        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':
            self.twenties += count
        

    def remove(self, count, denomination):
        """
        (CashRegister, int, string) -> NoneType
        """
        if denomination == 'loonies':
            self.loonies -= count
        elif denomination == 'toonies':
            self.toonies -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':
            self.twenties -= count
            
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    register = CashRegister(5,5,5,5,5)
    print register.getTotal()

    register.add(3, 'toonies')
    register.remove(2, 'twenties')
    
    regone = CashRegister(1,1,1,1,1)
    regtwo = CashRegister(1,1,1,1,1)
    print regone == regtwo

    print(register)
    print(regone)
    
        
