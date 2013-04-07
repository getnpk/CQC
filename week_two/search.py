"""
Checking the worst case seanarios for a 10000000 records on my machine.

Binary Search
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 search.py:30(binary_search)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Linear Search
         10000005 function calls in 31.644 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   31.644   31.644 <string>:1(<module>)
        1   16.877   16.877   31.644   31.644 search.py:1(linear_search)
 10000002   14.767    0.000   14.767    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Linear Search Improved
         4 function calls in 1.541 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.541    1.541 <string>:1(<module>)
        1    1.541    1.541    1.541    1.541 search.py:15(linear_search_improved)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

def linear_search(L, v):
    """
    (list, object) -> int
    """
    i =0
    
    while i != len(L) and v != L[i]:
        i = i +1

    if i == len(L):
        return -1
    else:
        return i

def linear_search_improved(L, v):
    """
    (list, object) -> int
    """
    i =0
    length = len(L)
    while i != length and v != L[i]:
        i = i +1

    if i == length:
        return -1
    else:
        return i


def binary_search(L, v):
    """
    works only on sorted list
    (list, object) -> int
    >>> binary_search([1,2,3,4,5], 4)
    3
    """
    b = 0
    e = len(L) - 1

    while b <= e:
        middle = ( b + e ) // 2
        if L[middle] == v:
            return middle
        elif L[middle] < v:
            b = middle + 1
        else:
            e = middle - 1

    if b>e:
        return -1


if __name__ == '__main__':
    import doctest
    import cProfile

    doctest.testmod()
    
    l = range(10000000)

    #worst case searnarios
    print 'Binary Search'
    cProfile.run('binary_search(l, 10000000)')

    print 'Linear Search'
    cProfile.run('linear_search(l, 10000000)')

    print 'Linear Search Improved'
    cProfile.run('linear_search_improved(l, 10000000)')
