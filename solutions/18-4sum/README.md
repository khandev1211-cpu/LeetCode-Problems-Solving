# [4Sum](https://leetcode.com/problems/4sum/)
Medium, Python3
## Approach
The key insight here is to use a two-pointer technique after sorting the array and fixing two elements. This approach was chosen over the naive brute-force approach of checking all possible quadruplets because it significantly reduces the number of operations. Here's a short walkthrough of the logic:
1. Sort the input array to enable the two-pointer technique.
2. Fix the first two elements and use two pointers, one starting from the next element of the second fixed element and one from the end of the array, to find a pair that sums up to the remaining target.
3. If the current sum is less than the target, move the left pointer to increase the sum.
4. If the current sum is greater than the target, move the right pointer to decrease the sum.
5. If the current sum equals the target, add the quadruplet to the result and move both pointers.
## Complexity
Time complexity: The time complexity is O(n^3) because in the worst case, we have three nested loops, one for fixing the first element, one for fixing the second element, and the two-pointer technique which can be considered as a loop. The sorting operation at the beginning also takes O(n log n) time but is dominated by the O(n^3) term.
Space complexity: The space complexity is O(n) because in the worst case, we might store all quadruplets in the result, and the space required for the input array and other variables is negligible compared to the space required for storing the result.