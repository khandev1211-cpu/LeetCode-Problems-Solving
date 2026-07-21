# [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to use a sorted version of each string as a key to group anagrams together, but instead of sorting, we use a character count array to avoid the overhead of sorting. This approach was chosen over the naive brute-force approach of comparing each string with every other string because it significantly reduces the time complexity. Here's a short walkthrough of the logic:
1. Initialize a hashmap to store the anagram groups.
2. For each string in the input array, count the frequency of each character.
3. Use the character count array as a key in the hashmap and append the string to the corresponding group.
## Complexity
Time complexity: O(NM) because we are iterating over each character in each string, where N is the number of strings and M is the maximum length of a string. 
Space complexity: O(NM) because in the worst case, we might need to store all strings in the hashmap.