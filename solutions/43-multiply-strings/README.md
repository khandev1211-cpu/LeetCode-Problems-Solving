# [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
Medium, python3
## Approach
The key insight here is to treat the multiplication of two numbers as a series of multiplications of single digits, similar to how we manually multiply numbers. This approach avoids the naive method of converting the strings to integers and then multiplying, which is not allowed. Instead, we iterate through each digit of both numbers from right to left, multiply them, and then add the results to the corresponding positions in the result array, handling any carry-over values. Here's a brief walkthrough:
1. Initialize a result array with zeros, with a length equal to the sum of the lengths of the two input numbers.
2. Iterate through each digit of both numbers from right to left, multiplying them and adding the results to the corresponding positions in the result array.
3. Handle any carry-over values by adding them to the next position in the result array.
## Complexity
Time complexity: The time complexity is O(n*m), where n and m are the lengths of the two input numbers, because we are iterating through each digit of both numbers once. 
Space complexity: The space complexity is O(n+m), where n and m are the lengths of the two input numbers, because we need to store the result in an array of length n+m.