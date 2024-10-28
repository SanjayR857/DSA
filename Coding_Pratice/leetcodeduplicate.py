import copy

def remove_duplicates(arr):
    new_list = []
    for i in range(len(arr)):
        if arr[i] not in arr[i+1:len(arr)]:
            new_list.append(arr[i])
    return sorted(new_list)
            
def remove_duplicates_1(arr):
    unique_list =[]
    seen=set()
    for i in arr:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
    return unique_list


list_num = [9,0,1,2,3,1,2,3,2,4,5,6,7,8,1,2,3,4]
print(remove_duplicates_1(list_num))