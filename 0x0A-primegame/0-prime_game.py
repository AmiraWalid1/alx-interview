#!/usr/bin/python3

def isPrime(num):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    int: 1 if the number is prime, 0 otherwise.
    """
    for i in range(2, num):
        if (num % i == 0):
            return 0
    return 1


def numOfPrime(num):
    """
    Count the number of prime numbers less than or equal to a given number.

    Args:
    num (int): The upper limit (inclusive) for counting primes.

    Returns:
    int: The count of prime numbers up to `num`.
    """
    cnt = 0
    for i in range(2, num + 1):
        cnt += isPrime(i)
    return cnt


def isWinner(x, nums):
    """
    Determine the winner of a game based on the number of primes
    in given ranges.
    Assuming Maria always goes first and both players play optimally.

    Args:
    x (int): The number of rounds to play.
    nums (list): A list of integers, where each integer is the upper limit
    for a round.

    Returns:
    str: The name of the winner ("Maria" or "Ben").
    """
    Maria, Ben = 0, 0
    for i in range(x):
        # If the number of primes is odd, Maria wins the round; otherwise,
        # Ben wins.
        if (numOfPrime(nums[i]) % 2):
            Maria += 1
        else:
            Ben += 1
    return "Maria" if Maria > Ben else "Ben"
