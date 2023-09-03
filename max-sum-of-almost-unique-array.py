from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        window_start, LEN = 0, len(nums)
        window_frequency_map = defaultdict(lambda:0)
        max_sum = 0
        current_sum = 0
        for window_end in range(LEN):
            current_sum += nums[window_end]
            window_frequency_map[nums[window_end]] += 1
            # window size should be k, should have atleast m distinct elements
            if window_end - window_start + 1 == k:
                if len(window_frequency_map) >= m:
                    max_sum = max( current_sum, max_sum )
                # upon reaching maximum size of window, lets shift the window by one number
                # but before doing that we would need to decrement from frequency, and decrement the sum
                current_sum -= nums[window_start]
                window_frequency_map[nums[window_start]] -= 1
                # if the frequency reached zero we can remove it.
                if window_frequency_map[nums[window_start]] == 0: window_frequency_map.pop(nums[window_start])
                window_start += 1

        return max_sum





if __name__ == '__main__':
    s = Solution()
    print(s.maxSum([2,6,7,3,1,7], 3, 4))
