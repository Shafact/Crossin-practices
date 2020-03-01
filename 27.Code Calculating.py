"""
Plans:
1. 定义一个函数阅读每个文件的每一行,定义三个list存储空行，注释行，和代码行
    A. 空行很方便定义：就是看阅读的list里的元素是不是[]
    B. 注释行就是正则匹配开头是"#"
    C. 剩下的行就是代码行
   *D. 多行注释的情况：找到所有'\"""'的位置，每两个位置之间的行数都算是注释行
"""
import os
import re


# 定义一个函数，读取文件的总行数，空行，单行注释行，多行注释行，和代码行
def lines(path):
    with open(path) as f:
        allLines = [i.strip('\n') for i in f.readlines()]
        total_lines = len(allLines)
        blank_lines = len([i for i in allLines if i == ''])
        noted_lines = 0
        for i in allLines:
            if re.match(r"^#",i):
                noted_lines += 1
        #找到多行注释的开头和结尾的index
        multi_lines = [i for (i,j) in enumerate(allLines) if re.match(r'^\"\"\"',j)]
        count_multi = 0
        if multi_lines:
            start_multi = multi_lines[::2]
            end_multi = multi_lines[1::2]
            for i in range(len(start_multi)):
                count_multi += end_multi[i] - start_multi[i] + 1

        #注释行等于单行注释行数+多行注释行数
        noted_lines += count_multi

        #代码行等于总行数-空行-注释行
        coded_lines = total_lines - blank_lines - noted_lines
    return {"total lines": total_lines,
            # "all Lines": allLines,
            "blank lines": blank_lines,
            "noted lines": noted_lines,
            #"multiple lines": multi_lines,
            #"count of multi explanation": count_multi,
             "coded lines": coded_lines}


#test function
# print(lines("/Users/sharonzhou/PycharmProjects/码上行动/8-12.py"))


#定义一个函数输出某个目录下所有的.py文件的路径
def pyFile(path):
    # 先把所有文件名列成一个表
    allFiles = os.listdir(path)
    py_files = []
    for i in allFiles:
        # 正则匹配.py结尾， 找到所有.PY文件，匹配路径
        if re.match(r'^\w.*(\.py)$', i):
            #print("path + i: ", path + i)
            py_files.append(path + i)
    return py_files



path =input("Please enter the path that you would like to open: ")
# "/Users/sharonzhou/PycharmProjects/码上行动/"

#找出里面所有的.py文件，把他们的位置列成一个list：
allPys = pyFile(path)
# print("all python files: ", allPys)

#对每一个文件的line 计数，存在一个列表里
allCounts = []
for i in allPys:
    allCounts.append(lines(i))
# print(allCounts)

#把allCounts里每一个element里对应的total lines, blank lines,
# noted lines, 和coded lines 各自加起来，得到一个总数
finalCounts = {"total lines": 0, "blank lines": 0, "noted lines": 0, "coded lines":0}
for element in allCounts:
    finalCounts["total lines"] += element["total lines"]
    finalCounts["blank lines"] += element["blank lines"]
    finalCounts["noted lines"] += element["noted lines"]
    finalCounts["coded lines"] += element["coded lines"]

print("final counts: ", finalCounts)






