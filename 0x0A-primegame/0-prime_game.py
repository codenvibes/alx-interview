#!/usr/bin/python3
"""
This script defines a function `isWinner` that determines the winner of a game
based on prime number counts.

The game involves Maria and Ben playing rounds, with each round specified by a
number. The winner of each round is determined by whether the count of prime
numbers up to that number is odd or even.

The function `isWinner` takes two parameters:
- `x`: The number of rounds played.
- `nums`: A list of integers, each representing the number for a round.

The function returns the name of the winner, either 'Maria' or 'Ben', based
on who won more rounds. If it's a tie, it returns `None`.
"""


def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben based on the count of prime
    numbers up to each number in the `nums` list.

    Args:
    x (int): The number of rounds played.
    nums (list of int): A list of integers where each integer represents a
    number for a round.

    Returns:
    str or None: Returns 'Maria' if Maria wins more rounds, 'Ben' if Ben wins
    more rounds, or None if there is a tie.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    n = max(nums)

    # Sieve of Eratosthenes to find all prime numbers up to n
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = sum(primes[0: n])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
