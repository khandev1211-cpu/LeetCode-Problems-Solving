class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        if not t or not s:
            return ""
            
        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1
            
        required = len(dict_t)
        formed = 0
        window_counts = defaultdict(int)
        
        left, right = 0, 0
        min_len = float('inf')
        result = ""
        
        while right < len(s):
            char = s[right]
            window_counts[char] += 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                    
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                    
                left += 1
                
            right += 1
            
        return result