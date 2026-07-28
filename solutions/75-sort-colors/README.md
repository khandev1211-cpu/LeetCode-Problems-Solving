# [Sort Colors](https://leetcode.com/problems/sort-colors/)
Medium, Python3
## Approach
The key insight here is to use three pointers (low, mid, high) to track the positions where the next 0, 1, and 2 should be placed, respectively. This approach was chosen over a naive sorting algorithm because it allows us to solve the problem in one pass and without using extra space. Here's a short walkthrough:
1. Initialize low and mid to 0, and high to the end of the array.
2. When mid encounters a 0, swap it with the element at low and increment both low and mid.
3. When mid encounters a 1, simply increment mid.
4. When mid encounters a 2, swap it with the element at high and decrement high.
## Complexity
The time complexity is O(n) because we're doing a single pass through the array, where n is the number of elements in the array. The space complexity is O(1) because we're only using a constant amount of extra space to store the pointers.