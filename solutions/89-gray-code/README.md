# [Gray Code](https://leetcode.com/problems/gray-code/)
Medium, Python3
## Approach
The problem requires generating an n-bit gray code sequence. A naive approach would be to generate all possible binary sequences and check each one to see if it meets the gray code criteria. However, this approach would be inefficient due to its brute-force nature. Instead, we can use a recursive approach to generate the gray code sequence. The key insight is that an n-bit gray code sequence can be generated from an (n-1)-bit gray code sequence by prefixing the (n-1)-bit sequence with 0 and the reversed (n-1)-bit sequence with 1. Here's a short walkthrough of the logic:
1. Base case: if n is 1, return the list [0, 1].
2. Recursive case: generate the (n-1)-bit gray code sequence.
3. Prefix the (n-1)-bit sequence with 0 and the reversed (n-1)-bit sequence with 1.
## Complexity
Time complexity: O(2^n) because we are generating a sequence of length 2^n. 
Space complexity: O(2^n) because we need to store the generated sequence of length 2^n.