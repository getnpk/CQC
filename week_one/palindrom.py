def is_palindrom(s):
    """
    Return True iff s is a palindrom
    
    (str) --> bool
    >>> is_palindrom("noon")
    True
    >>> is_palindrom("noons")
    False
    
    """
    return s == reverse(s)

def reverse(s):
    """
    Return reversed version of s
    """
    rev = ''
    
    for c in s:
        rev = c + rev
    return rev
