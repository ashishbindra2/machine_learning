list = [2,0,1,2,2,2,1,1,1,0,0,0]

# Selection

# min = -1

# for i in range(len(list)):
#     min = i
#     for j in range(i+1,len(list)):
#         if list[j]< list[min]:
#             min = j
#     list[i], list[min] = list[min], list[i]

# print(list)

def merge(arr,low,mid,heigh):
    temp = []
    left = low
    right = mid+1
    
    while left < mid and right< heigh:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left < mid:
        temp.append(arr[left])
        left+=1
    while right < heigh:
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[i] = temp[i]
    return arr
def merge_sor(arr,low,heigh):
    if low == heigh:
        return
    mid = (low + heigh)//2
    
    merge_sor(arr,low,mid)
    merge_sor(arr,mid+1,heigh)
    merge(arr,low,mid,heigh)
    
    
merge_sor(list,0,len(list))
print(list)
    