# Your code here
import math
import random
import datetime

cache = {}
pow_cache = {}
fact_cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def get_pow(x,y):
    if (x,y) not in pow_cache:
        pow_cache[(x,y)] = math.pow(x,y)

    return pow_cache[(x,y)]

def get_fact(x):
    if x not in fact_cache:
        fact_cache[x] = math.factorial(x)

    return fact_cache[x]

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x,y) not in cache:
        v = get_pow(x, y)
        v = get_fact(v)
        v //= (x + y)
        v %= 982451653
        cache[(x,y)] = v

    return cache[(x,y)]



# Do not modify below this line!
time1 = datetime.datetime.now()
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

time2 = datetime.datetime.now()
print('time taken:', time2-time1)
