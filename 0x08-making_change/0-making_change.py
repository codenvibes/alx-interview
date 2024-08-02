#!/usr/bin/python3
"""
A module to determine the minimum number of coins needed to make a given total.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given total.

    Args:
        coins (list): A list of the values of the coins available.
        total (int): The total amount of money to make with the coins.

    Returns:
        int: The minimum number of coins needed to make the total,
        or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count
