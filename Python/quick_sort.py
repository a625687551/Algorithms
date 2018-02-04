# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
插入排序就是讲一个数据插入到已排好的有序数据中，从而得到一个新的有序数列，算法适用于少量数据，时间复杂度O(n^2),是稳定的
一个排序方式
'''


def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


if __name__ == '__main__':
    l = [29, 10, 14, 37, 14]
    f = quick_sort(l, left=0, right=len(l) - 1)
    print("finally {}".format(f))
