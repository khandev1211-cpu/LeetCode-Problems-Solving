# [Subsets](https://leetcode.com/problems/subsets/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to generate subsets iteratively by adding each new number to all existing subsets, thus avoiding the brute-force approach of generating all possible combinations of numbers. This approach is chosen because it efficiently builds upon previously computed subsets, reducing redundant computation. Here's a short walkthrough:
1. Initialize the result with an empty subset.
2. For each number in the input array, create new subsets by appending this number to all existing subsets.
3. Add these new subsets to the result.
## Complexity
Time complexity: The time complexity is O(2^n) because in the worst case, we are generating all possible subsets of the input array, where n is the number of elements in the array. This is justified because each element can either be included or excluded from a subset, resulting in 2^n possibilities.
Space complexity: The space complexity is also O(2^n) because we need to store all generated subsets in the result, and in the worst case, there are 2^n subsets for an array of n unique elements.