# [Valid Number](https://leetcode.com/problems/valid-number/)
Hard, Python3
## Approach
The key insight here is to track the state of the input string as we iterate through it, checking for valid number patterns. Unlike a naive approach that might involve complex regular expressions or multiple passes through the string, this solution iterates through the string once, keeping track of whether we've seen a digit, a dot (indicating a decimal number), or an exponent. This approach is chosen because it efficiently handles the various cases of valid numbers (integer, decimal, with or without exponents) in a single pass.
Here's a short walkthrough of the logic:
1. Initialize flags to track if we've seen a digit, a dot, or an exponent.
2. Iterate through each character in the string, updating the flags as necessary and checking for invalid patterns (like a sign not at the start or after an exponent, or multiple dots or exponents).
3. After iterating through the entire string, return whether we've seen at least one digit, indicating a valid number.
## Complexity
Time complexity: The solution has a time complexity of O(n), where n is the length of the input string, because it makes a single pass through the string.
Space complexity: The space complexity is O(1), because it uses a constant amount of space to store the flags, regardless of the input size.