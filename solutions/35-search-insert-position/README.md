# [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
Easy, Python3
## Approach
The key insight here is to use a binary search algorithm, which allows us to achieve the required O(log n) runtime complexity. A naive approach would be to simply iterate through the array, checking each element until we find the target or reach the end, but this would result in a linear O(n) complexity. Instead, by repeatedly dividing the search interval in half, we can efficiently find the target or its insertion point. Here's a short walkthrough:
1. Initialize two pointers, `left` and `right`, to the start and end of the array.
2. Calculate the midpoint `mid` and compare the value at this index to the target.
3. If the target is found, return its index; if the target is greater than the midpoint value, move the `left` pointer to `mid + 1`; otherwise, move the `right` pointer to `mid - 1`.
4. Repeat steps 2-3 until `left` is greater than `right`, at which point `left` will be the index where the target should be inserted.
## Complexity
The time complexity is O(log n) because with each iteration, we effectively halve the size of the search space. The space complexity is O(1) because we only use a constant amount of space to store the pointers and the midpoint, regardless of the input size.