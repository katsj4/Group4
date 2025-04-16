# fibonacci_interactive.py
def fibonacci(n, memo={}):
    """Top-down approach with memoization"""
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def get_user_input():
    while True:
        try:
            n = int(input("Enter a positive integer for Fibonacci sequence: "))
            if n < 0:
                print("Please enter a non-negative integer!")
                continue
            return n
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    print("Fibonacci Sequence Calculator")
    print("----------------------------")
    n = get_user_input()
    print(f"Fibonacci({n}) = {fibonacci(n)}")