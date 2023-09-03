from collections import defaultdict


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        frequency_map = defaultdict(lambda: 0)
        for c in s:
            frequency_map[c] += 1



if __name__ == '__main__':
    s = Solution()
