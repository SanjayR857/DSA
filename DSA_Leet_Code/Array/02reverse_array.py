class Solution:
    def reverseArray(self,arr):
        len_arr = len(arr)
        temp = arr[::-1]
        for i in range(len_arr):
            arr[i] = temp[i]
        return temp

    def reverseArray_1(self, arr):
        right = 0
        left = len(arr) - 1
        while right < left:
            arr[right], arr[left] = arr[left], arr[right]
            right += 1
            left -= 1
        return arr

    def reverse_array(self):
        n = len(arr)
        for i in range(n // 2):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        print(arr)


arr = [1,2,3,4]
sol = Solution()
sol.reverseArray(arr)
for i in arr:
    print(i)


def recussion(arr,l,r):
    if l>=r:return

    arr[l],arr[r] = arr[r],arr[l]
    recussion(arr,l+1,r-1)

recussion(arr,0,len(arr)-1)
print(arr)