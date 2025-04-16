# coin_change_interactive.py
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def get_coin_input():
    while True:
        try:
            coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
            if not coins:
                raise ValueError
            return coins
        except ValueError:
            print("Invalid input! Please enter space-separated integers.")

if __name__ == "__main__":
    print("\nCoin Change Problem Solver")
    print("--------------------------")
    coins = get_coin_input()
    amount = int(input("Enter target amount: "))
    
    if amount < 0:
        print("Amount cannot be negative!")
        exit()
    
    result = coin_change(coins, amount)
    
    if result == -1:
        print("\nIt's not possible to make change for this amount with the given coins.")
    else:
        print(f"\nMinimum coins needed: {result}")