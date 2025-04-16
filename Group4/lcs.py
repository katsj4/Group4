# lcs_interactive.py
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruction
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(lcs))

if __name__ == "__main__":
    print("\nLongest Common Subsequence Finder")
    print("--------------------------------")
    text1 = input("Enter first string: ").strip()
    text2 = input("Enter second string: ").strip()
    
    if not text1 or not text2:
        print("Error: Both strings must be non-empty!")
        exit()
    
    length, sequence = longest_common_subsequence(text1, text2)
    print(f"\nLCS Length: {length}")
    print(f"LCS Sequence: {sequence if sequence else '<empty>'}")