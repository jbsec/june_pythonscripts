import math
def is_prime(n):
    # 1 = non prime
    if n == 1:
        return False

        # check divisors to the sqrt of n
        max_check = math.floor(math.sqrt(n))

        #loop to check divisors
        for d in range(2,max_check + 1):
            if n % d == 0:
                return False
             #if not divisible return true
                return True

#test
    for i in range (1,100):
         print(i , " is a prime: ", is_prime(i))

# tech read inspired
# prime numbers in python

# havent been able to fix this, if you can, go ahead and fork the fix. 