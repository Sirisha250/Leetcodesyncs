class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0

        is_prime = [True] * n  # Assume all numbers are prime initially
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for i in range(2, int(n ** 0.5) + 1):  # Check up to sqrt(n)
            if is_prime[i]:  # Found a prime number
                for j in range(i * i, n, i):  # Mark multiples as non-prime
                    is_prime[j] = False

        return sum(is_prime)  # Count the True values (primes)
