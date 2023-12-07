#!/usr/bin/python3
"""Prime Game interview challenge"""



def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def remove_multiples(nums, prime):
        return [num for num in nums if num % prime != 0]

    def get_winner(nums):
        prime_turn = True
        while nums:
            primes = [num for num in nums if is_prime(num)]
            if not primes:
                return "Ben" if prime_turn else "Maria"
            selected_prime = min(primes)
            nums = remove_multiples(nums, selected_prime)
            prime_turn = not prime_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = get_winner(list(range(1, n + 1)))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
