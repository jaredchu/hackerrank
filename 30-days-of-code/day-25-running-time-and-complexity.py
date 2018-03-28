def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 is 0 or number % 3 is 0:
        return False

    i = 5
    while i ** 2 <= number:
        if number % i is 0 or number % (i + 2) is 0:
            return False
        i = i + 6
    return True


n = int(input().strip())
for _ in range(n):
    if is_prime(int(input().strip())):
        print('Prime')
    else:
        print('Not prime')
