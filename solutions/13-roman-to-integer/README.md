# [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
Easy, Python3
## Approach
The key insight here is to iterate over the Roman numeral string from right to left, keeping track of the previous numeral's value. This approach allows us to handle cases where a smaller numeral appears before a larger one (indicating subtraction), such as IV for 4 or IX for 9, more efficiently than a brute-force approach that checks all possible combinations. Here's a short walkthrough:
1. Create a mapping of Roman numerals to their integer values.
2. Initialize variables to keep track of the total sum and the previous numeral's value.
3. Iterate over the input string from right to left, updating the total sum based on whether the current numeral's value is less than the previous one (indicating subtraction).
## Complexity
Time complexity is O(n), where n is the length of the input string, because we make a single pass through the string. Space complexity is O(1), because the space used does not grow with the size of the input string, as we only use a constant amount of space to store the mapping and variables.