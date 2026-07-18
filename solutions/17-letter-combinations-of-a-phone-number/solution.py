from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        combinations = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                combinations.append(''.join(current_combination))
                return
            
            for letter in digit_to_letters[digits[index]]:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
        
        backtrack(0, [])
        return combinations