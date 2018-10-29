# You are given a sorted array containing both negative and positive values. Resort the array taking absolute value of negative numbers. Your complexity should be O(n)
# Ex. A = {-8,-5,-3,-1,3,6,9} Expected Output: {-1,-3,3,-5,6,-8,9}

import array
arr = array.array('i', [-8,-5,-3,-1,3,6,9])

# res = sorted(arr, key=abs) # sorted in inbuilt python function to sort th given array
# print(res)

def resort(array):
    max =0 #absolute max
    for a in array:
        if max*max < a*a:
            max = a
    if max <= 0:
        max = -max

    # count = array.array('i', [0]*m)
    m = max+1
    count = [0]*m

    length = len(array)
    result = [0]*length

    new_arr = []
    for a in array:
        if a > 0:
            count[a] += 1
        else:
            count[-a] += 1

    # print('count1',count)
    for i in range(1,max+1):
        count[i] = count[i-1] + count[i]
        # print(i,'count3',count)

    # print('array',array)
    for i in range(len(array)-1,-1,-1):
        if array[i]>0:
            result[count[array[i]] -1] = array[i]
            count[array[i]] -= 1;
        else:
            result[count[-array[i]] -1] = array[i]
            count[-array[i]] -= 1;
    return result

# print(resort(arr))
user_input = [int(item) for item in input().split()]
print(user_input)
arr1 = array.array('i', user_input)
print(resort(arr1))
