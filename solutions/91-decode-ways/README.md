# [Decode Ways](https://leetcode.com/problems/decode-ways/)
Medium, python3
## Approach
The key insight here is to use dynamic programming to store the number of ways to decode the string up to each position. This approach was chosen over a naive recursive approach because it avoids redundant calculations and thus improves efficiency. The logic can be broken down as follows:
1. Initialize a dynamic programming array `dp` where `dp[i]` represents the number of ways to decode the string up to the `i-th` position.
2. For each position `i` starting from the second character, check if the current character can be decoded independently (i.e., it is not '0'). If so, add the number of ways to decode the string up to the previous position (`dp[i-1]`) to `dp[i]`.
3. Then, check if the current and previous characters can be decoded together (i.e., they form a number between 10 and 26). If so, add the number of ways to decode the string up to the position two characters before (`dp[i-2]`) to `dp[i]`.
## Complexity
The time complexity is O(n), where n is the length of the string, because we are scanning the string once. The space complexity is also O(n), because we are using a dynamic programming array of size n+1 to store the number of ways to decode the string up to each position.