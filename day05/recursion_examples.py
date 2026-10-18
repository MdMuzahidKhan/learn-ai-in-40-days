# Approach: Solve factorial and Fibonacci recursively, then optimize Fibonacci with memoization.

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_memo(number, memo=None):
    if memo is None:
        memo = {}

    if number in memo:
        return memo[number]

    if number <= 1:
        return number

    memo[number] = fibonacci_memo(number - 1, memo) + fibonacci_memo(number - 2, memo)
    return memo[number]


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fibonacci(6))
    print("Memoized Fibonacci of 30:", fibonacci_memo(30))