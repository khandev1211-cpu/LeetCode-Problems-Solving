class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) > maxWidth:
                total_spaces = maxWidth - line_length
                if len(line) == 1:
                    res.append(line[0] + ' ' * total_spaces)
                else:
                    space_per_gap = total_spaces // (len(line) - 1)
                    extra_spaces = total_spaces % (len(line) - 1)
                    line_str = line[0]
                    for i in range(1, len(line)):
                        spaces = space_per_gap + (1 if i <= extra_spaces else 0)
                        line_str += ' ' * spaces + line[i]
                    res.append(line_str)
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)
        
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res