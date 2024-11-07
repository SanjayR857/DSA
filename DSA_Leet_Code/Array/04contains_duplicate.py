class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen_1 = set()
        for i in nums:
            if i in seen_1:
                return True
            else:
                seen_1.add(i)
        return False

sol = Solution()
res = sol.containsDuplicate([1,2,3,1])
print(res)