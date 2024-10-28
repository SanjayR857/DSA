#return indexs of the array if there sum is equal to target value it not return 0

nums = [2,7,11,15]
target =22


def get_two_sum_indexs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            print(i,j)
            if nums[i]+nums[j] == target:return [i,j]
    return -1

def get_two_sum_indexs_2(nums,target):
    seen ={}
    for i,num in enumerate(nums):
        complement = target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    

print(get_two_sum_indexs_2(nums,target))  

