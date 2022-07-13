def mateq(a, b):
    """
    check if two matrix have same elements
    """
    if len(a) != len(b):
        return False

    if len(a) != 0 and len(a[0]) != len(b[0]):
        return False

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False

    return True


def matmul(a, b):
    """
    Multiply the two given matrix
    """

    assert len(a[0]) == len(b), "Invalid dimentions"

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            print(i, j)
            for k in range(len(a[i])):
                result[i][j] += a[i][k] * b[k][j]

    return result
