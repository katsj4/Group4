def fibonacci_bottomup(n):
    """Bottom-up approach with tabulation"""
    if n <= 1:
        return n
    
    # Initialize table with base cases
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    
    # Fill the table iteratively
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]

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
    print("Fibonacci Sequence Calculator (Bottom-Up)")
    print("----------------------------------------")
    n = get_user_input()
    print(f"Fibonacci({n}) = {fibonacci_bottomup(n)}")