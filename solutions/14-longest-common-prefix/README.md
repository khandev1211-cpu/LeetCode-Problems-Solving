# [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
Easy, Python3
## Approach
The key insight here is to start with the first string as the initial prefix and iteratively compare it with the rest of the strings, reducing the prefix until a match is found across all strings. This approach avoids the brute-force method of comparing all possible prefixes of the first string against the rest. Here's a short walkthrough:
1. Initialize the prefix as the first string in the array.
2. Iterate through the rest of the strings, comparing each string's prefix (of the same length as the current prefix) against the current prefix.
3. If a mismatch is found, reduce the prefix by one character and repeat the comparison until a match is found or the prefix becomes empty.
## Complexity
The time complexity is O(n * m) because in the worst case, we might need to compare each character of each string, where n is the number of strings and m is the maximum length of a string. The space complexity is O(1) because we only use a constant amount of space to store the prefix and do not use any data structures that scale with input size.