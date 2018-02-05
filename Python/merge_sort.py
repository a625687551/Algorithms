# !/usr/bin/env python3
# -*- coding:utf-8 -*-


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    n = len(lists)
    num = n//2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = merge_sort(l)
    print("finally {}".format(f))
