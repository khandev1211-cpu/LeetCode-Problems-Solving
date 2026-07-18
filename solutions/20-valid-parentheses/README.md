# [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
Easy, Python3
## Approach
The key insight here is to use a stack data structure to keep track of the opening brackets encountered so far. This approach is chosen over a naive brute-force one, such as generating all possible valid strings and checking if the input string matches any of them, because it allows for efficient checking of the input string's validity. Here's a short walkthrough of the logic:
1. Initialize an empty stack and a dictionary mapping closing brackets to their corresponding opening brackets.
2. Iterate over each character in the input string.
3. If the character is an opening bracket, push it onto the stack.
4. If the character is a closing bracket, check if the stack is empty or if the top of the stack does not match the current closing bracket. If either condition is true, return False.
## Complexity
The time complexity is O(n) because we make a single pass through the input string, where n is the length of the input string. The space complexity is O(n) because in the worst-case scenario, we might need to push all characters onto the stack.