from audioop import mul
import random
import math


def get_non_zero_random_number():
    rnd = random.random()

    while rnd == 0:  # exclue zero to be a share
        rnd = random.random()

    return rnd


def generate_shares(n, scale=100000):
    return [get_non_zero_random_number() * scale for _ in range(n)]


def generate_random_shares_mul(number, n, scale=100000):
    """
    return n shares of the given number
    with the this property:
        product of all shares is equal to the number
    """

    shares = generate_shares(n - 1, scale)

    partial_product = math.prod(shares)
    shares.append(number / partial_product)
    return shares


def generate_random_shares_sum(number, n, scale=100000):
    """
    return n shares of the given number
    with the this property:
        sum of all shares is equal to the number
    """

    shares = generate_shares(n - 1, scale)

    partial_sum = sum(shares)
    shares.append(number - partial_sum)
    return shares
