def anagramMappings(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    P = []
    for i,v in enumerate(A):
        for k,j in enumerate(B):
            if v == j:
                P.append(k)
                break
    return P

print(anagramMappings([40,40],[40,40]))