# [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to use a sliding window approach to find the minimum window substring of `s` that includes every character in `t`. A naive approach would be to generate all possible substrings of `s` and check if each one contains all characters in `t`, but this would be inefficient due to its O(m^2 * n) time complexity. Instead, we use a two-pointer technique (left and right pointers) to represent the sliding window. We also use two dictionaries (`dict_t` and `window_counts`) to keep track of the characters in `t` and the current window, respectively. Here's a short walkthrough of the logic:
1. Initialize the `dict_t` dictionary with the characters in `t` and their frequencies.
2. Initialize the `window_counts` dictionary to keep track of the characters in the current window.
3. Move the right pointer to the right and update `window_counts` accordingly.
4. If the current window contains all characters in `t`, move the left pointer to the right and update `window_counts` accordingly.
5. Keep track of the minimum window substring that contains all characters in `t`.
## Complexity
Time complexity: The time complexity is O(m + n) because we are potentially scanning the string `s` once and the string `t` once, where m and n are the lengths of `s` and `t`, respectively. This is because the while loop runs in total m times (m is the length of the string `s`), and the for loop to create `dict_t` runs in total n times.
Space complexity: The space complexity is O(m + n) because in the worst case, the size of `dict_t` and `window_counts` can be up to n and m, respectively, where m and n are the lengths of `s` and `t`, respectively.