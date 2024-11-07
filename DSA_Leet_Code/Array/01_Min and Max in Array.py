class Solution:
    def get_min_max(self, arr):
        min_num = arr[0]
        max_num = arr[0]

        for i in arr:
            if max_num < i:
                max_num = i
            if min_num > i:
                min_num = i
        return min_num, max_num

sol = Solution()

res = sol.get_min_max([1,56,34,4])
print(res)