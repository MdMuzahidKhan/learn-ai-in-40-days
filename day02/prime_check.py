# Approach: A number is prime if it is greater than 1 and has no divisors other than 1 and itself.

def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


sample_number = 17
print(sample_number, "is prime:", is_prime(sample_number))

edge_case_number = -5
print(edge_case_number, "is prime:", is_prime(edge_case_number))