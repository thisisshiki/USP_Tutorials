#!/bin/env python3
# Generate a random list of integers
# Starting with start from STDIN 
# Ending with end from STDIN 
# Size n from STDIN 

# Determine and show the prime numbers from the list

import random as ran  

def randomlist(start,end,n):
    return ran.sample(range(start,end+1),n) 

# Using the any-pattern
def is_prime(n):
    for e in range(2,n):
        if n%e == 0:
            return False
    return True

#Using the every=pattern
def primes_list(numbers):
    primes = []
    for e in numbers:
        if is_prime(e):
            primes.append(e)   
    return primes

def run():
    start = int(input('start: '))
    end = int(input('end: '))
    n = int(input('size: '))
    numbers = randomlist(start,end,n)
    primes = primes_list(numbers)
    print(numbers)
    print(primes)

run()














