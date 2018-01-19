#!/usr/local/bin/python3

#第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/local/bin 下的 python3 解释

"""
    author: Steve Kore
    e-mail: haungke04@meituan.com
    github: https://github.com/KoreHuang 
"""


print("hello,world")


if True:
    print("answer true")
else:
    print("answer false")

# x="a"
# y="b"
# 换行输出
# print( x )
# print( y )
#
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )
# print()

print('---------')
print("argv 输出:")

import sys

for arg in sys.argv:
    print(arg)

print('---------')

print("path 输出:")

#  from ... import 导入特定的成员
from sys import path

for pathitem in path:
    print(pathitem)

print('---------')