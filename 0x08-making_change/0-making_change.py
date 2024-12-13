#!/usr/bin/python3
"""Solve the making change problem"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
        needed to meet a given total.
    Args:
        coins (list): Values of the coins available.
        total (int): Target total amount.
    Returns:
        int: Fewest number of coins needed to
            meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
