# Remove Element
[https://leetcode.com/problems/remove-element/](https://leetcode.com/problems/remove-element/)
Easy, python3
## Approach
The key insight here is to use a two-pointer approach. The brute-force approach would be to remove all occurrences of val from the list, which would require shifting all elements after the removed one, resulting in a time complexity of O(n^2). Instead, we use a pointer k to keep track of the position where the next element not equal to val should be placed. We iterate through the list with pointer i, and whenever we find an element not equal to val, we place it at the k-th position and increment k. This approach allows us to avoid shifting elements and achieve a time complexity of O(n).
Here's a short walkthrough of the logic:
1. Initialize k to 0, which will keep track of the position where the next element not equal to val should be placed.
2. Iterate through the list with pointer i.
3. If the current element is not equal to val, place it at the k-th position and increment k.
## Complexity
The time complexity is O(n), because we only need to iterate through the list once to find all elements not equal to val and place them at the correct positions.
The space complexity is O(1), because we only use a constant amount of space to store the pointers k and i, and we modify the input list in-place.