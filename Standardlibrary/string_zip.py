# -*- coding: utf-8 -*-
# @Time    : 2019-11-29 16:49
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : string_zip.py
# @Software: PyCharm


from itertools import product

def zipzip(*iterables):#zip source code
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


slist = [1, 2, 3, 5, 8, 4, 2]
llist = ["a", "b", "c", "d"]
flist = ["hello", "python", "world", "good"]
for i in zipzip(slist, llist, flist):
    print(i)


for i,j in product(llist,flist):
    print (i,j)