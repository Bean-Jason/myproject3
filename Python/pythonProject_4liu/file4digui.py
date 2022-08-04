# 递归训练：1-100累加的和
# 非递归思想：
def sum1(start, end):
    acc = 0
    for n in range(start, end + 1):
        acc += n
    return acc


result = sum1(1, 100)
print("Non-Recursive:", result)

del sum1


# 递归思想，利用递归函数：
def sum1(start, end):
    if start < end:
        acc = start + sum1(start + 1, end)
        return acc
    else:
        return end


result = sum1(1, 100)
print("Recursive:", result)

del sum1


# 高斯算法suanfa
def sum1(start, end):

    return(start+end)*(end-start+1)/2


result = sum1(1, 100)
print("Gauss:", result)
