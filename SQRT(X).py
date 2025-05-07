class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0, sqrt(1) = 1
        
        left, right = 1, x
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                res = mid  # this could be the answer
                left = mid + 1  # look for a bigger candidate
            else:
                right = mid - 1  # mid is too big

        return res
