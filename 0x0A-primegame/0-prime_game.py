#!/usr/bin/python3
''' Prime Game'''


def isWinner(x, nums):
    """
    Determine the winner of the prime game for x rounds.

    Args:
    x (int): Number of rounds.
    nums (list): List of integers, where each integer is the upper limit
    for a round.

    Returns:
    str: The winner of the game ("Maria" or "Ben"). If it's a tie, return None.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    Maria, Ben = 0, 0
    for i in range(x):
        if (prime_count[nums[i]] % 2):
            Maria += 1
        else:
            Ben += 1

    return "Maria" if Maria > Ben else "Ben"
