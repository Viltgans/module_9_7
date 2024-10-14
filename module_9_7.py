def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    print('Составное')
                    break
                print('Простое')
                break
        return x
    return wrapper

@is_prime
def sum_three(*number):
    return sum(number)


result = sum_three(2, 3, 6)
print(result)