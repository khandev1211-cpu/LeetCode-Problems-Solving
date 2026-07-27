class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        permutation = []
        k -= 1  # convert to 0-based index
        
        for i in range(n, 0, -1):
            fact = 1
            for j in range(1, i):
                fact *= j
            index = k // fact
            permutation.append(str(numbers.pop(index)))
            k %= fact
            
        return ''.join(permutation)