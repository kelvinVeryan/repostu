#!/usr/bin/python3
# -*- coding: utf-8 -*-
def trim(s):
    if s == '':
        return s
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

# 利用递归思路的写法
def trim2(s):
    if s == '':
        return s
    if s[0] == ' ':
        return trim2(s[1:])
    if s[-1] == ' ':
        return trim2(s[:-1])
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
