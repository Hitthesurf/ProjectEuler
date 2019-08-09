import time
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


def prime_factors(num):
    print(num)
    prime_factors = []
    start_time = time.time()
    while not (is_prime(num) or num == 1):
        for i in range(1,num):
            if (num%i)==0:
                if is_prime(i):
                    print (num)
                    prime_factors.append(i)
                    num = int(num/i)
                    
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
    return prime_factors

print (prime_factors(13195))
print (prime_factors(131950))
#print (prime_factors(1319500))
#print (prime_factors(13195000))
#print (prime_factors(131950000))
