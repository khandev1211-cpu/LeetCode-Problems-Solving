# [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)
Easy, Python3
## Approach
The key insight here is to find the smallest and largest numbers in the array and then calculate their greatest common divisor (GCD). A naive approach could involve checking every possible divisor from 1 up to the smaller number, but this is inefficient. Instead, we use the Euclidean algorithm to find the GCD, which is more efficient. Here's a short walkthrough:
1. Define a helper function `gcd(a, b)` that calculates the GCD of two numbers using the Euclidean algorithm.
2. Find the smallest and largest numbers in the input array `nums`.
3. Call the `gcd` function with the smallest and largest numbers as arguments and return the result.
## Complexity
Time complexity: The time complexity is O(log min(n, m)) because the Euclidean algorithm reduces the problem size roughly by half with each iteration, where n and m are the smallest and largest numbers in the array. This is justified because the algorithm only needs to iterate until the remainder is 0, which happens quickly for relatively prime numbers.
Space complexity: The space complexity is O(1) because we only use a constant amount of space to store the smallest and largest numbers and the GCD, regardless of the input size.