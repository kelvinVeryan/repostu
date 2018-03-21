#!/usr/bin/python3
# -*- coding: utf-8 -*-
# fliter是个过滤的函数
# 求所有的素数
def _odd_iter():  #创立字符串
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


print ('=========================================================')

# 求所有的回数 919翻转过来还是919
'''
def is_palindrome(n):
    s = str(n)
    s1 = s[::-1]  #这里用了切片的翻转字符串的方法
    return s == s1  #这是个判断
'''
#另外一种方法
def is_palindrome(n):
    i = 0
    j = 0
    strn = str(n)
    num = int(len(str(n))/2)
    while i < num:
        if strn[i] == strn[len(str(n))-1-i]:
            j = j + 1
        i = i + 1
    return j == num
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
