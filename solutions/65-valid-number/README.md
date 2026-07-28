# [Valid Number](https://leetcode.com/problems/valid-number/)
Hard, Python3
## Approach
The key insight here is to recognize that a valid number can be either an integer or a decimal number, both of which can optionally be followed by an exponent. A brute-force approach would involve manually checking each character in the string against the formal definition of a valid number, which would be cumbersome and error-prone. Instead, we can use a finite state machine to track the current state of the input string as we iterate through it. Here's a high-level walkthrough:
1. Initialize a set of states representing the possible components of a valid number (e.g., sign, integer part, decimal part, exponent).
2. Iterate through the input string, transitioning between states based on the current character.
3. If we reach the end of the string and are in a valid final state, return True; otherwise, return False.
## Complexity
Time complexity: The time complexity is O(n), where n is the length of the input string, because we make a single pass through the string. 
Space complexity: The space complexity is O(1), because we use a constant amount of space to store the current state and the input string.