def is_palindrom_v2(s):
    """
    reverse second half and compare with first
    """
    n = len(s)
    return s[:n // 2] == reverse(s[n - n // 2:])
    
def reverse(s):
    rev = ''
    for c in s:
        rev = c + rev
    return rev
