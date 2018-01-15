def anagramMappings(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    P = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                P.append(j)
    return P

print(anagramMappings([12, 28, 46, 32, 50],[50, 12, 32, 46, 28]))