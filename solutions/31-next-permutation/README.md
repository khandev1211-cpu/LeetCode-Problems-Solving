# [Next Permutation](https://leetcode.com/problems/next-permutation/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to find the first decreasing element from the right, then swap it with the next greater element to its right, and finally reverse the elements to the right of the swapped pair. This approach was chosen over a brute-force one, such as generating all permutations and finding the next lexicographically greater one, because it is much more efficient. Here's a short walkthrough of the logic:
1. Start from the end of the array and find the first pair of elements where the left element is smaller than the right one.
2. If no such pair is found, the array is the last permutation, so we reverse it to get the first permutation.
3. Otherwise, we find the smallest element to the right of the left element of the pair that is greater than the left element and swap them.
4. Finally, we reverse the elements to the right of the swapped pair to get the next permutation.
## Complexity
Time complexity: The algorithm runs in O(n) time, where n is the number of elements in the array, because in the worst case, we need to traverse the entire array to find the first decreasing element from the right and then reverse the elements to the right of the swapped pair.
Space complexity: The algorithm uses O(1) space, because we only use a constant amount of space to store the indices of the elements to be swapped and the loop variables, and we modify the input array in-place.