# knapsack_interactive.py
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Reconstruction
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected[::-1]

def get_input_list(prompt):
    while True:
        try:
            lst = list(map(int, input(prompt).split()))
            if not lst:
                raise ValueError
            return lst
        except ValueError:
            print("Invalid input! Please enter space-separated integers.")

if __name__ == "__main__":
    print("\n0/1 Knapsack Problem Solver")
    print("---------------------------")
    print("Enter weights of items (space-separated):")
    weights = get_input_list("Weights: ")
    print("Enter values of items (space-separated):")
    values = get_input_list("Values: ")
    
    if len(weights) != len(values):
        print("Error: Number of weights and values must match!")
        exit()
    
    capacity = int(input("Enter knapsack capacity: "))
    
    max_value, items = knapsack(weights, values, capacity)
    print(f"\nMaximum value: {max_value}")
    print(f"Selected items (0-based index): {items}")
    print(f"Selected weights: {[weights[i] for i in items]}")
    print(f"Selected values: {[values[i] for i in items]}")