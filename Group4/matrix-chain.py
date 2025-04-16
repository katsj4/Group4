# matrix_chain_interactive.py
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp[0][n-1]

def get_dimensions():
    while True:
        try:
            dims = list(map(int, input("Enter matrix dimensions (space-separated): ").split()))
            if len(dims) < 2:
                raise ValueError
            return dims
        except ValueError:
            print("Invalid input! Please enter at least 2 integers.")

if __name__ == "__main__":
    print("\nMatrix Chain Multiplication Optimizer")
    print("------------------------------------")
    print("Example: For matrices A(2×3), B(3×4), C(4×5), enter: 2 3 4 5")
    dimensions = get_dimensions()
    
    min_operations = matrix_chain_order(dimensions)
    print(f"\nMinimum scalar multiplications needed: {min_operations}")