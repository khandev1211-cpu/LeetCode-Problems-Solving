class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(end, path + [segment])
        result = []
        backtrack(0, [])
        return result