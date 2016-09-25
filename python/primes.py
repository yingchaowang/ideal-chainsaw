def is_prime(n):
    """return true if *n* is prime"""
    for element in range(n/2):
        if n % element == 0:
            return False
    return True

def print_next_prime(n):
    """print the cloest prime number larger than *n*"""
    index = n
    while True:
        index +=1
        if is_prime(index):
            print index

