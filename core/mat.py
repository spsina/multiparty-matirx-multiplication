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

    assert len(a[0]) == len(b), "Invalid dimensions"

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            print(i, j)
            for k in range(len(a[i])):
                result[i][j] += a[i][k] * b[k][j]

    return result


# def generate_shares_matrix(a, n):
#     shares_matrix = [[ [0 for _ in range(n)] for _ in range(len(a[0])) ] for _ in range(len(a)) ]
    
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             shares_matrix[i][j] = generate_random_shares_mul(a[i][j], n)
    
#     print(shares_matrix)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(generate_shares_matrix(a, 3))
