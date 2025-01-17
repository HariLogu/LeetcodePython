# Two Pointers Algorithm (squeezing Algo)
"""
basically it includes two variables left and right
l=left end
r=right end

then we have to compare it between them ,if the condition
satisfies then we have to move the pointer towards center (basically
like we are doing in BS)

to move the both pointers towards center we have to increment
l by one ,and decrement r by one

it all happens within teh while loop with the con. of l<=r
"""

# for ex square of a sorted array

# it can be easily achieved by the map method and some inbuilt
# sorted methods

def fun(arr):
    res = list(map(lambda x: x * x, arr))
    return sorted(res)

a = [-3, -1, 0, 7, 10]
print(fun(a))



def fun(arr):
    l = 0  # first index
    r = len(arr) - 1  # last index
    res = []
    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            res.append(arr[l] ** 2)
            l += 1
        else:
            res.append(arr[r] ** 2)
            r -= 1
    res.reverse()
    return res

a = [-3, -1, 0, 7, 10]
print(fun(a))
