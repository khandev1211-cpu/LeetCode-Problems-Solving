# [Plus One](https://leetcode.com/problems/plus-one/)
Easy, Python3
## Approach
The key insight here is to convert the array of digits into a single integer, increment it, and then convert it back into an array of digits. This approach was chosen over a naive approach of iterating through the array from right to left and handling carry-overs because it is simpler and more straightforward. Here's a short walkthrough of the logic:
1. Initialize a variable `num` to 0.
2. Iterate through the input array `digits` from left to right, and for each digit, multiply it by 10 raised to the power of the difference between the length of the array and the current index minus 1, and add the result to `num`.
3. Increment `num` by 1.
4. Convert `num` back into a string, and then into a list of integers, which is the resulting array of digits.
## Complexity
The time complexity is O(n) because we are iterating through the input array once, where n is the length of the input array. The space complexity is O(n) because we are creating a new list of integers of the same length as the input array.