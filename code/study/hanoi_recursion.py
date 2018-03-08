#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 实际功能只需要move(n, a, b, c) 就可以。最后一个参数是为了看每行输出挪动的是哪层塔。
# 最后一个参数起作用的只有move(1,a,b,c,n) 命令而已。

def move(n, a, b, c, le):
    if n == 1:
            print(le , a,'--->',c)
    else:
            move(n-1,a,c,b,n-1)
            move(1,a,b,c,n)
            move(n-1,b,a,c,n-1)
move(4, 'A', 'B', 'C',3)
print ('=========================')
move(3, 'A', 'B', 'C',3)

# move(3, 'A', 'B', 'C')  期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C

