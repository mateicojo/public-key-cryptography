import time
import random

#euclidean algorithm using subtractions
def gcd_1(a,b):
    if a ==0 or b==0:
        return 0
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

#recursive euclidean algorithm - may lead to stack overflow with large inputs
def gcd_2(a,b):
    if(b==0 or a == 0):
        return a
    else:
        return gcd_2(b,a%b)

#euclidean algorithm using division
def gcd_3(a,b):
    if (a==0 or b==0):
        return 0
    while b==0:
        a=b
        b=a%b
    return a

test_cases = [(random.randint(1, 10**12), random.randint(1, 10**12)) for _ in range(10)]
for pair in test_cases:
    print("\n\n\n")
    start_t_1=time.time()
    gcd_1(pair[0],pair[1])
    end_t_1=time.time()
    dur_1=end_t_1-start_t_1
    print(f"time for euclidean algorithm using subtractions: "+ str(dur_1) + " for the pair "+ str(pair) +"")
    start_t_2=time.time()
    gcd_2(pair[0],pair[1])
    end_t_2=time.time()
    dur_2=end_t_2-start_t_2
    print(f"time for recursive euclidean algorithm using subtractions: "+ str(dur_2) + " for the pair "+ str(pair) +"")
    start_t_3=time.time()
    gcd_3(pair[0],pair[1])
    end_t_3=time.time()
    dur_3=end_t_3-start_t_3
    print(f"time for euclidean algorithm using division: "+ str(dur_3) + " for the pair "+ str(pair) +"")