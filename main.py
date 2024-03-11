from prime_test import prime_test
from  trial_division import trial_division
from pollard import pollard
from bm_method import bm_factorize

n = int(input('Enter number to factorize: '))


def full_factorize(n):
    factors = []

    while n != 1:
        if prime_test(n,5): 
            factors.append(n)
            return factors
        
        found, divisors = trial_division(n)
        if found:
            n = divisors[1]
            factors.append(divisors[0])
            continue
        else: break
        
    while n != 1:    
        found,divisors = pollard(n)
        if(found):
            n = divisors[1]
            factors.append(divisors[0])
        else:
            break
            
        if prime_test(n,5): 
            factors.append(n)
            return factors
        
    while n != 1:
        factor = bm_factorize(n)
        
        if factor == 1:
            print('BM method gave me 1')
            return factors
        
        factors.append(factor)
        n = n//factor
        
        if prime_test(n,5): 
            factors.append(n)
            return factors
    


print(full_factorize(n))
    