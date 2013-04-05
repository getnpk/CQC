def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    0   0 no bus required
    10  1
    50  1
    75  2
    100 2
    110 3
    
    >>> num_buses(75)
    2
    >>> num_buses(50)
    1
    >>> num_buses(10)
    1
    >>> num_buses(100)
    2

    """
    if n == 0:
        return 0
    t = n % 50 
    if t == 0:
        return i if n // 50 == 0 else n // 50
    else:
        return n // 50 + 1


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.
    []                 (0,0)
    [0]                (0,0)
    [1.0]              (1.0, 0)
    [-1.0]             (0,-1.0)
    [1.0,-1.0]         (1.0,-1.0)
    [1.0, 0]            (1.0,0)
    [-1.0, 0]           (0,-1.0)
    [1.0,1.0,-1.0]      (2.0, -1.0)
    [-1.0,1,-1.0]       (1, 1.0)
    
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    sum_gains = 0
    sum_loses = 0
    for i in price_changes:
        if i > 0:
            sum_gains += i
        else:
            sum_loses += i
    return (sum_gains, sum_loses)
            


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    Note: can't do much without return!
    [],0                  []
    [1],0                 [1]
    [1],1                 [1]
    [1,2],1               [2,1]
    [1,2],0               [1,2]
    [1,2,3],0             [1,2,3]
    [1,2,3],1             [3,2,1]
    [1,2,3,4],1           [4,2,3,1]
    [1,2,3,4],2           [3,4,1,2]
    [1,2,3,4,5],2         [4,5,3,1,2]
    
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4, 5, 6]
    
    """
    
    back = L[-k:]
    front = L[:k]
    middle = L[k:-k]
    L = back + middle + front
    
    
    
    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
