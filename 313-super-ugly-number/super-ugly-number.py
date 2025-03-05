class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n  # Array to store first n super ugly numbers
        index = [0] * len(primes)  # Pointers for each prime
        values = list(primes)  # Next potential ugly number from each prime

        for i in range(1, n):
            next_ugly = min(values)  # Find the next smallest super ugly number
            ugly[i] = next_ugly

            for j in range(len(primes)):  
                if values[j] == next_ugly:  # Update only if the prime created next_ugly
                    index[j] += 1
                    values[j] = ugly[index[j]] * primes[j]  

        return ugly[-1]

# Example test cases
sol = Solution()
print(sol.nthSuperUglyNumber(12, [2,7,13,19]))  # Output: 32
print(sol.nthSuperUglyNumber(1, [2,3,5]))       # Output: 1
