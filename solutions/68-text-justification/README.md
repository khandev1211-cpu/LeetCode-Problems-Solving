# [Text Justification](https://leetcode.com/problems/text-justification/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to pack words in a greedy approach, distributing extra spaces as evenly as possible. We avoid a naive approach of trying all combinations of words on each line, which would be computationally expensive. Instead, we iterate through the words, adding them to the current line until adding the next word would exceed the maxWidth. We then distribute the extra spaces on the current line, handling the case where the number of spaces does not divide evenly between words. For the last line, we left-justify the text and do not add extra spaces between words.
Here is a short walkthrough of the logic:
1. Initialize variables to track the current line and its width.
2. Iterate through the words, adding each word to the current line if possible.
3. When adding a word would exceed the maxWidth, distribute extra spaces on the current line and add it to the result.
4. Handle the last line by left-justifying the text and not adding extra spaces between words.
## Complexity
Time complexity: The time complexity is O(n * m), where n is the number of words and m is the maximum width, because we are iterating through each word and potentially distributing spaces on each line. 
Space complexity: The space complexity is O(n * m), because in the worst case, we might need to store all words in the result, and each word can have up to m characters.