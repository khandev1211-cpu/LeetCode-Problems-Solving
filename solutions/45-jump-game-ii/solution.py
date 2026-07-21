class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        max_reach, step, jumps = nums[0], nums[0], 1
        for i in range(1, n):
            if i == n - 1:
                return jumps
            max_reach = max(max_reach, i + nums[i])
            step -= 1
            if step == 0:
                jumps += 1
                if i >= max_reach:
                    return -1
                step = max_reach - i
        return jumps