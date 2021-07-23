'''
question : Count of elements A[i] such that A[i] + 1 is also present in the Array
'''


def countElements(arr):
    count ={}
    result = 0
    for itm in arr:
        count[itm] = count.get(itm,0)+1
    print(count)
    for key in count:
        result =result+ count.get(key-1,0)
    return result

arr = [1,2,2,3]
res = countElements(arr)
print(res)

arr = [1,1,3,3,5,5,7,7]
print(countElements(arr))