# [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
Difficulty: Easy, Language: python3
## Approach
The key insight here is to start from the end of the string and skip any trailing spaces, then count the length of the last word by moving backwards until a space is encountered. This approach was chosen over a naive brute-force approach of splitting the string into words and getting the length of the last word because it avoids the overhead of creating a list of words. Here's a short walkthrough:
1. Initialize a pointer at the end of the string and skip any trailing spaces.
2. Once a non-space character is found, start counting the length of the word by moving the pointer backwards.
3. Continue counting until a space is encountered, at which point the length of the last word has been found.
## Complexity
Time complexity: The time complexity is O(n) because in the worst case, we have to traverse the entire string, where n is the length of the string.
Space complexity: The space complexity is O(1) because we only use a constant amount of space to store the length and the pointer.