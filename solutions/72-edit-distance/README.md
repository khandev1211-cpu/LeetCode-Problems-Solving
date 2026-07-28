# [Edit Distance](https://leetcode.com/problems/edit-distance/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to use dynamic programming to build up a 2D table `dp` where `dp[i][j]` represents the minimum number of operations required to convert the first `i` characters of `word1` to the first `j` characters of `word2`. This approach was chosen over a naive brute-force approach (e.g., trying all possible sequences of operations) because it avoids redundant computation and has a much lower time complexity. Here's a short walkthrough of the logic:
1. Initialize the base cases where one of the strings is empty.
2. Fill in the rest of the table by comparing characters from `word1` and `word2` and choosing the operation that results in the minimum number of operations.
3. The final result is stored in `dp[m][n]`, where `m` and `n` are the lengths of `word1` and `word2`, respectively.
## Complexity
The time complexity is O(m * n) because we need to fill in a 2D table of size (m + 1) x (n + 1), where m and n are the lengths of the input strings. The space complexity is also O(m * n) because we need to store the 2D table `dp`.