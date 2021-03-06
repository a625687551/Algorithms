# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
重复的访问要排序的数列，一次比较两个元素，重复进行直到排序完成，是一个稳定的排序
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- 如果能在内部循环第一次运行时,使用一个旗标来表示有无需要交换的可能,可以把最优时间复杂度降低到O(n)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''


def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i + 1, count):
            print(lists)
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    l = [50, 10, 30, 20, 60, 40, 1]
    # l = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    # l = [29, 10, 14, 37, 14]
    f = bubble_sort(l)
    print("finally {}".format(f))
