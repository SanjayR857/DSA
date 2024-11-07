#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
res = nums[0]
sub_array = []
for i in range(len(nums)):
    for j in range (i+1,len(nums)+1):
        print(nums[i:j])
        if res<sum(nums[i:j]):
            res = sum(nums[i:j])
            sub_array = nums[i:j]
print(res)
print(sub_array)

class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            if total <0:
                total = 0
            total+=n
            res = max(res,total)
        return res