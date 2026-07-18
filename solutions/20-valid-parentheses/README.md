# [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
Easy, Python3
## Approach
The key insight here is to use a stack data structure to keep track of the opening brackets encountered so far. This approach was chosen over a naive brute-force approach, such as checking all possible combinations of brackets, because it allows for an efficient solution with a linear time complexity. Here's a short walkthrough of the logic:
1. Initialize an empty stack to store the opening brackets.
2. Iterate over each character in the input string.
3. If the character is an opening bracket, push it onto the stack.
4. If the character is a closing bracket, check if the stack is empty or if the top of the stack does not match the current closing bracket. If either condition is true, return False.
5. After iterating over the entire string, return True if the stack is empty (i.e., all brackets were matched correctly) and False otherwise.
## Complexity
The time complexity is O(n) because we are scanning the string once, where n is the length of the input string. The space complexity is O(n) because in the worst case, we might need to push all characters onto the stack.