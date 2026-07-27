# [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to utilize the factorial number system to efficiently determine the kth permutation sequence. This approach was chosen over a naive brute-force approach, such as generating all permutations and selecting the kth one, due to its significantly improved efficiency. Here's a short walkthrough of the logic:
1. Initialize a list of numbers from 1 to n and an empty permutation list.
2. Iterate from n to 1, calculating the factorial of the current number minus one.
3. Determine the index of the current number in the permutation based on the factorial and the given k.
4. Append the number at the calculated index to the permutation list and remove it from the numbers list.
5. Update k to be the remainder of k divided by the factorial.
## Complexity
Time complexity: The time complexity is O(n), because we are iterating over the numbers from n to 1, performing a constant amount of work for each number. 
Space complexity: The space complexity is O(n), because we are storing the numbers and the permutation, both of which require O(n) space.