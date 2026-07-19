# [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
Hard, Python3
## Approach
The key insight here is to use a stack to track the indices of unmatched opening parentheses. This approach is chosen over a naive brute-force one, such as checking all possible substrings, because it allows us to efficiently skip over invalid substrings and focus on valid ones. Here's a short walkthrough of the logic:
1. Initialize a stack with -1 to handle edge cases where the longest valid substring starts at the beginning of the string.
2. Iterate through the string, pushing the index of each opening parenthesis onto the stack.
3. When a closing parenthesis is encountered, pop the corresponding opening parenthesis from the stack.
4. If the stack is empty after popping, push the current index onto the stack to mark the start of a new potential valid substring.
5. Otherwise, calculate the length of the current valid substring and update the maximum length if necessary.
## Complexity
Time complexity: The algorithm runs in O(n) time, where n is the length of the string, because each character is visited at most once. 
Space complexity: The algorithm uses O(n) space, where n is the length of the string, because in the worst case, the stack can grow up to the length of the string.