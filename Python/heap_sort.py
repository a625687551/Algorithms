# !/usr/bin/env python3
# -*- coding:utf-8 -*-


def heap_sort(lists, i, size):
    # 堆排序
    lchild = 2*i + 1
    rchild = 2*i + 2
    mt = i
    if i>size/2:
        if lchild < size and lists[lchild] > lists[mt]:
            mt = lchild
        if rchild < size and lists[rchild] > lists[mt]:
            mt = rchild
        if mt != i:
            lists[mt], lists[i] = lists[i], lists[mt]
            heap_sort(lists, mt, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        heap_sort(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        heap_sort(lists, 0, i)


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = heap_sort(l)
    print("finally {}".format(f))
