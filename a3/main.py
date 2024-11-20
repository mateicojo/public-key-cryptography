import random
def miller_rabin_test(n, k=8):
    """
    false means n is not prime
    true means n is probably a prime.
    """
    if n in [0,1,4,6,8,9]:
        return False

    if n in [2,3,5,7]:
        return True

    #write n-1 as 2^s*d(and d is odd).
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1 #exponent
    #n-1 = 2^s * d

    def trial(a):
        #check a^d = 1 (%n)
        if pow(a, d, n) == 1:
            return False
        #check a^(2^i * d) = -1 (mod n) for any i in [0, s-1]
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)#rand a in [2, n-2]
        if trial(a):
            return False

    return True

test_values = [2, 3, 5, 7, 11, 13, 17, 19, 101, 103, 107, 109, 113, 131, 137,
               15485863, 32452843, 999999937, 4, 6, 8, 9, 10, 12, 15, 100, 102,
               104, 105, 110, 132, 15485864, 32452842, 999999936]

for n in test_values:
    print(f"{n}: {'Prime' if miller_rabin_test(n) else 'Not Prime'}")