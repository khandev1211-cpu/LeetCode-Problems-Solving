# Simplify Path
[https://leetcode.com/problems/simplify-path/](https://leetcode.com/problems/simplify-path/)
Medium, Python3
## Approach
The key insight here is to use a stack to keep track of the directories in the simplified path. This approach is chosen over a naive one, such as string manipulation, because it allows for efficient handling of the '..' and '.' cases. Here's a short walkthrough of the logic:
1. Split the input path into components by the '/' character.
2. Iterate over each component, ignoring empty strings and '.'.
3. When encountering '..', pop the last directory from the stack if it's not empty.
4. For any other component, add it to the stack.
## Complexity
The time complexity is O(n), where n is the number of components in the path, because we're doing a constant amount of work for each component. The space complexity is also O(n), because in the worst case, we might need to store all components in the stack.