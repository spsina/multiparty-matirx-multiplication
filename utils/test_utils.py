import math
from utils import (
    generate_random_shares_mul,
    generate_random_shares_sum,
    generate_shares,
)


def test_generate_shares():
    shares = generate_shares(10, 100)

    assert len(shares) == 10, "Invalid Number of shares"

    for s in shares:
        assert s <= 100, "Invalid share scale"


def test_generate_random_shares_sum():

    shares = generate_random_shares_sum(20, 100)

    assert len(shares) == 100, "Invalid share len"
    assert sum(shares) == 20, "Invalid shares"


def test_generate_random_shares_mul():

    shares = generate_random_shares_mul(20, 50)

    assert len(shares) == 50, "Invalid share len"
    assert math.prod(shares) == 20, "Invalid shares"
