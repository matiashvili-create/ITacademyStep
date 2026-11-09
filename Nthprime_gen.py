def prime_generator():

    num = 2

    while True:
        is_prime =True
        for i in range(2,num):
            if num  %   i == 0:
                is_prime =False
                break
        if is_prime:
            yield num
        num +=1

primes=prime_generator()

for i in range(20):
    print(next(primes))




