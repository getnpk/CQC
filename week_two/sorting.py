"""
Sorting done for a random list of 10000 integers between 1 and 9 inclusive.

Bubble sort
         10003 function calls in 13.561 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   13.561   13.561 <string>:1(<module>)
        1   13.225   13.225   13.561   13.561 sorting.py:1(bubble_sort)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     9999    0.336    0.000    0.336    0.000 {range}


Selection sort
         30005 function calls in 7.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.006    7.006 <string>:1(<module>)
        1    0.024    0.024    7.006    7.006 sorting.py:23(selection_sort)
    10000    6.374    0.001    6.982    0.001 sorting.py:39(get_smallest_index)
    10001    0.015    0.000    0.015    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10001    0.593    0.000    0.593    0.000 {range}


Insertion sort
         10005 function calls in 0.039 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
        1    0.019    0.019    0.039    0.039 sorting.py:50(insertion_sort)
    10000    0.020    0.000    0.020    0.000 sorting.py:64(insert)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}

"""

def bubble_sort(L):
    """

    the last element of the L becomes the highest value
    after each iteration, followed by the second biggest
    and so on.
    
    >>> L = [3,4,5,2,6,1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    """

    end = len(L) - 1

    while end != 0:
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i+1] = L[i+1], L[i]

        end = end - 1
    
def selection_sort(L):
    """

    the smallest element of L will be at the first postion
    after each iteration followed by next biggest as so on.
    
    >>> L = [3,4,5,2,6,1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    
    """
    for i in range(len(L)):
        smallest_value_index = get_smallest_index(L, i)
        L[i], L[smallest_value_index] = L[smallest_value_index], L[i]

def get_smallest_index(L, i):
    index_smallest = i
    length = len(L)
    for i in range(i+1, length):
        if L[i] < L[index_smallest]:
            index_smallest = i
    return index_smallest
        



def insertion_sort(L):
    """

    as i increase the values till i are sorted.
    
    >>> L = [3,4,5,2,6,1]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6]
    
    """
    for i in range(len(L)):
        insert(L,i)

def insert(L,i):
    #the value to be inserted
    value = L[i]

    #find j where value belongs.
    #make room by shifting, if greater than value.
    j = i
    while j != 0 and L[j-1] > value:
        #shift left by one position to right.
        L[j] = L[j-1]
        j = j - 1

    #insert the value at postion
    L[j] = value
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
    import cProfile
    import random
    
    
    
    l = []
    for i in range (10000):
        #Return and append a random integer N such that a <= N <= b.
        l.append(random.randint(1,9))

    print 'Bubble sort'
    cProfile.run('bubble_sort(l)')

    print 'Selection sort'
    cProfile.run('selection_sort(l)')

    print 'Insertion sort'
    cProfile.run('insertion_sort(l)')
