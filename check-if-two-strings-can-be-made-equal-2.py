class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        LEN = len(s1)
        t1, t2, t3, t4 = "", "", "", ""

        for i in range(0, LEN, 2):
            t1 += s1[i]
            t2 += s2[i]

        for i in range(1, LEN, 2):
            t3 += s1[i]
            t4 += s2[i]

        return sorted(t1) == sorted(t2) and sorted(t3) == sorted(t4)


if __name__ == '__main__':
    s = Solution()
