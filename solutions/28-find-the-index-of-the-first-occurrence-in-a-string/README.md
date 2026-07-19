# Find the Index of the First Occurrence in a String
[https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
Easy, Python3
## Approach
The key insight here is to utilize Python's built-in string method `index()` which returns the index of the first occurrence of the specified value. A naive approach would be to manually iterate through the haystack string and check for the occurrence of the needle string, but using `index()` simplifies this process and improves efficiency. Here's a short walkthrough:
1. Check if the needle string is empty. If it is, return 0 as per the problem's requirements.
2. Attempt to find the index of the needle string in the haystack string using `index()`. If found, return the index.
3. If `index()` raises a `ValueError`, it means the needle string is not found in the haystack string, so return -1.
## Complexity
The time complexity is O(n) because in the worst-case scenario, `index()` has to scan through the entire haystack string. The space complexity is O(1) because no additional space is used that scales with input size.