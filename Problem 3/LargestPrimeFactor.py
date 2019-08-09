import time


class Primes:

    def __init__(self):
        self.prime_factors_array = []

    @staticmethod
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def old_prime_factors(self, num):
        print(num)
        prime_factors = []
        start_time = time.time()
        while not (self.is_prime(num) or num == 1):
            for i in range(1, num):
                if (num % i) == 0:
                    if self.is_prime(i):
                        print(num)
                        prime_factors.append(i)
                        num = int(num / i)

        end_time = time.time()
        duration = end_time - start_time
        print(duration)
        return prime_factors

    def prime_factors_rec(self, num):
        num = int(num)
        for i in range(2, num):
            if num % i == 0:
                t = int(num / i)
                if self.is_prime(t):
                    self.prime_factors_array.append(t)
                else:
                    self.prime_factors_rec(t)
                if self.is_prime(i):
                    self.prime_factors_array.append(i)
                else:
                    self.prime_factors_rec(i)
                break

    def prime_factors(self, num):
        self.prime_factors_array = []
        self.prime_factors_rec(num)
        return sorted(self.prime_factors_array)


prime_compute = Primes()
# print(prime_compute.prime_factors(13195))
# print(prime_compute.prime_factors(131950))
# print (prime_factors(1319500))
print(prime_compute.prime_factors(600851475143))
# print (prime_factors(131950000))
