# [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
Easy, Python3
## Approach
The key insight here is to use a binary search approach to find the integer square root. This is chosen over a naive brute-force approach of checking every integer up to x, as it significantly reduces the number of iterations required. Here's a short walkthrough of the logic:
1. If x is less than 2, we can return x directly since the square root of 0 or 1 is the number itself.
2. We then initialize two pointers, left and right, to 1 and x // 2 respectively, to start our binary search.
3. In each iteration, we calculate the mid value and check if its square equals x. If it does, we return mid as it's the exact square root.
4. If mid squared is less than x, we move the left pointer to mid + 1 to search in the right half; otherwise, we move the right pointer to mid - 1 to search in the left half.
## Complexity
The time complexity is O(log n) because with each iteration of the while loop, we effectively halve the search space, which is a characteristic of binary search algorithms.
The space complexity is O(1) because we only use a constant amount of space to store the variables left, right, and mid, regardless of the size of the input x.