# [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to explore all possible combinations of segments that could form a valid IP address. This is chosen over a naive brute-force approach of trying all possible segment lengths and positions because backtracking allows us to prune branches early when we encounter invalid segments (e.g., those starting with '0' and having more than one digit, or those exceeding '255'). Here's a short walkthrough:
1. Start with an empty path and the beginning of the string.
2. Explore all possible segment lengths (1 to 3 characters) from the current start position.
3. Validate each segment to ensure it doesn't start with '0' unless it's the only character, and its value doesn't exceed 255.
4. If a segment is valid, recursively backtrack with the updated path and the new start position.
5. If the path contains four segments and we've reached the end of the string, add the path as a valid IP address to the result.
## Complexity
Time complexity: The time complexity is O(3^L) where L is the length of the input string, because in the worst case, for each character, we might explore up to three different segment lengths. This is justified because each character can potentially be the start of a new segment, and we explore up to three possible segment lengths from each position.
Space complexity: The space complexity is O(L) due to the recursion stack and the space needed to store the result, where L is the length of the input string. This is justified because the maximum depth of the recursion tree is proportional to the length of the input string, and we also need to store all valid IP addresses found.