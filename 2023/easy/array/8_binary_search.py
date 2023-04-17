def search (nums, target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (end+start)//2
        print(start, mid , end)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid+1
        if nums[mid] > target:
            end = mid-1
    return -1


nums = [-1,0,3,5,9,12]
target = 9
print(search (nums, target))


nums = [-1,0,3,5,9,12]
target = 2
print(search (nums, target))

nums = [5]
target = 5
print(search (nums, target))