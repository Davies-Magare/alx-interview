#!/usr/bin/python3
"""Prime Number game"""
def isWinner(x, nums):
    def sieve_of_eratosthenes(max_n):
        """Generate a list of primes up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    def count_primes_up_to(n, prime_list):
        """Count the number of primes up to n using the prime list."""
        return sum(prime_list[:n + 1])

    if x <= 0 or not nums:
        return None

    max_n = max(nums)  # Find the maximum value of n in the rounds
    prime_list = sieve_of_eratosthenes(max_n)  # Generate primes up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, prime_list)
        if prime_count % 2 == 1:
            # If the number of primes is odd, Maria wins
            maria_wins += 1
        else:
            # If the number of primes is even, Ben wins
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
