# [Next Permutation](https://leetcode.com/problems/next-permutation/)
Medium, Python3
## Approach
The key insight to solving this problem is to find the first pair of elements from the right that are in increasing order, and then swap the first element with the smallest element to its right that is greater than it. This approach was chosen over a brute-force one (which would involve generating all permutations and finding the next one) because it allows us to find the next permutation in linear time. Here's a short walkthrough of the logic:
1. Start from the second last element and move to the left until we find an element that is smaller than the one to its right.
2. If such an element is found, then find the smallest element to its right that is greater than it and swap them.
3. Finally, reverse the elements to the right of the swapped element to get the next permutation.
## Complexity
The time complexity is O(n) because in the worst case, we need to traverse the entire array to find the next permutation. The space complexity is O(1) because we are modifying the input array in-place and using a constant amount of extra memory.