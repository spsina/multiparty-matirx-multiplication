import math

from mat.mat import matmul, generate_shares_matrix
from mat.mat import mateq


def test_matmul():
    """
    [1, 2, 3]   [4, 5, 4, 3]   [13,15,18,32]
    [4, 5, 6] x [3, 2, 1, 1] = [37,42,45,71]
    [7, 8, 9]   [1, 2, 4, 9]   [61,69,72,110]

    3x3        3x4           = 3x4
    """

    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[4, 5, 4, 3], [3, 2, 1, 1], [1, 2, 4, 9]]
    true_result = [[13, 15, 18, 32], [37, 42, 45, 71], [61, 69, 72, 110]]

    result = matmul(a, b)

    assert mateq(true_result, result), "Invalid result"


def test_generate_shares_matrix():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    shares_matrix = generate_shares_matrix(a, 3)

    a_from_shares = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]

    for i in range(len(shares_matrix)):
        for j in range(len(shares_matrix[0])):
            a_from_shares[i][j] = math.prod(shares_matrix[i][j])

    assert mateq(a, a_from_shares), "Invalid shares matrix"
