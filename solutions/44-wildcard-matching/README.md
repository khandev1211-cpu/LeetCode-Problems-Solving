# [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to use dynamic programming to track whether the input string matches the pattern up to certain points. This approach was chosen over a naive recursive one (which would involve trying all possible matches for '*' and '?' and checking if any of them lead to a full match) because it avoids redundant computation and thus has much better performance. Here's a short walkthrough of the logic:
1. Initialize a 2D array `dp` where `dp[i][j]` is `True` if the first `i` characters of the input string match the first `j` characters of the pattern.
2. Handle the base case where the input string is empty, which can match a pattern that consists entirely of '*' characters.
3. Fill in the rest of the `dp` array based on whether the current characters in the input string and pattern match (for '?' or exact matches) or if the pattern character is '*', in which case we consider two possibilities: the '*' matches zero characters or one or more characters.
## Complexity
The time complexity is O(m*n) because we need to fill in the `dp` array, where `m` and `n` are the lengths of the input string and pattern, respectively. The space complexity is also O(m*n) because we need to store the `dp` array.