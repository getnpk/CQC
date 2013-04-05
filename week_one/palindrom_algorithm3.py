def is_palindrom_v3(s):
    """
    compare the first and last element of string.
    odd ends at i == j
    even ends at j < i
    
    """
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1
        
    return j <= i
        
