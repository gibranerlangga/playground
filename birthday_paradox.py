def _factorial(n):
    if n == 1:
        return 1
    else:
        return n * _factorial(n-1)

def probability_of_same_birthday(n=23):
    return 1 - _factorial(365)/(_factorial(365-n)*365**n)

for i in range(2, 50):
    print(i, probability_of_same_birthday(i))
