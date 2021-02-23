def decrement_at(vector, i):
    while min(vector) == 0:
        [decrement_at(vector.remove(v).append(v-1), i+1)]
        return i
    

def pathND(vector):
    """
    >>> pathND([3, 2])
    10
    >>> pathND([3, 1, 2])
    60
    """
    if decrement_at(vector, 0) == 1:
        return 1
    else:
        return decrement_at(vector,0)
