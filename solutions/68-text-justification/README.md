# [Text Justification](https://leetcode.com/problems/text-justification/)
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
Difficulty: Hard, Language: python3
## Approach
The key insight here is to pack words in a greedy approach and distribute extra spaces evenly between words. A naive approach would be to try all possible combinations of words on each line, but this would be inefficient due to the large number of possible combinations. Instead, we iterate through the words and add them to the current line until adding the next word would exceed the maximum width. We then justify the current line by distributing the extra spaces and add it to the result. The last line is left-justified by joining the remaining words with a single space and padding with extra spaces to the maximum width.
Here is a short walkthrough of the logic:
1. Initialize an empty result list and an empty current line.
2. Iterate through each word in the input list.
3. If adding the current word to the current line would exceed the maximum width, justify the current line and add it to the result.
4. Add the current word to the current line.
5. After iterating through all words, justify the last line and add it to the result.
## Complexity
The time complexity is O(n * m), where n is the number of words and m is the maximum width, because we iterate through each word and potentially iterate through each character in the word to justify the line. The space complexity is O(n * m), because we store the justified lines in the result list, which can contain up to n words and m characters per line.