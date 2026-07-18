# [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all possible combinations of letters that a given phone number could represent. This approach was chosen over a naive brute-force one (which would involve generating all possible combinations and then filtering them based on the input digits) because it allows us to efficiently prune branches that do not lead to valid combinations. Here's a short walkthrough of the logic:
1. Define a mapping of digits to letters.
2. Initialize an empty list to store the combinations.
3. Define a recursive backtracking function that takes an index and a current combination as arguments.
4. If the index is equal to the length of the input digits, append the current combination to the list of combinations.
## Complexity
The time complexity is O(4^n) because in the worst case, each digit can map to 4 letters (as in the case of digits 7 and 9), and there are n digits. The space complexity is O(n) because the maximum depth of the recursion tree is n, where n is the length of the input digits.