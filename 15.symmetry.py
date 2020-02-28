"""
问题描述】

回文数：一个数从左向右与从右向左读是一样的，例如34543和1234321都是回文数

问题：输出所有200以内，平方是回文数的数。

例如：26 的平方是 676，为回文数。所以 26 满足我们的条件
"""

"""
def reverse_str(strg):
    rev_str = []
    for i in strg:
        rev_str.insert(0,i)
    return rev_str

rightnumber = []
for i in range(1, 201):
    square = str(i*i)
    square_sep = [char for char in square]
    square_rev = reverse_str(square)
    if square_sep == square_rev:
        rightnumber.append(i)
        print(f"number {i} and square: {i*i}")
    else:
        pass
print("rightnumber: ",rightnumber)
"""

for n in range(1, 200):
    #sq是n的平方
    sq = n * n
    #把平方值转为字符串
    str_sq = str(sq)
    for i in range(len(str_sq)):
        if str_sq[i] != str_sq[-(i+1)]:
            break
    else:
        print(n)