#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速排序算法实现
Quick Sort Algorithm Implementation
"""


def quicksort(arr):
    """
    快速排序主函数

    算法思想：
    1. 选择一个基准元素（pivot）
    2. 将数组分为两部分：小于基准的元素和大于基准的元素
    3. 递归地对两部分进行快速排序

    时间复杂度：
    - 平均情况：O(n log n)
    - 最坏情况：O(n²)
    - 最好情况：O(n log n)

    空间复杂度：O(log n)（递归栈）

    参数：
        arr: 待排序的列表

    返回：
        排序后的列表
    """
    # 基本情况：空数组或单元素数组已经有序
    if len(arr) <= 1:
        return arr

    # 选择基准元素（这里选择中间元素）
    pivot = arr[len(arr) // 2]

    # 将数组分为三部分：小于基准、等于基准、大于基准
    left = [x for x in arr if x < pivot]      # 小于基准的元素
    middle = [x for x in arr if x == pivot]   # 等于基准的元素
    right = [x for x in arr if x > pivot]     # 大于基准的元素

    # 递归排序并合并结果
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序（不使用额外空间）

    这个版本直接在原数组上进行排序，不创建新数组

    参数：
        arr: 待排序的列表
        low: 排序范围的起始索引
        high: 排序范围的结束索引
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 进行分区操作，返回基准元素的最终位置
        pivot_index = partition(arr, low, high)

        # 递归排序基准左边的子数组
        quicksort_inplace(arr, low, pivot_index - 1)

        # 递归排序基准右边的子数组
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数：将数组分为两部分

    选择最右边的元素作为基准，将小于基准的元素移到左边，
    大于基准的元素移到右边

    参数：
        arr: 数组
        low: 起始索引
        high: 结束索引

    返回：
        基准元素的最终位置索引
    """
    # 选择最右边的元素作为基准
    pivot = arr[high]

    # i 指向小于基准的区域的最后一个元素
    i = low - 1

    # 遍历数组，将小于基准的元素交换到左边
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素

    # 将基准元素放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# 测试代码
if __name__ == "__main__":
    print("=" * 50)
    print("快速排序算法测试")
    print("=" * 50)

    # 测试用例 1：普通数组
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n原始数组: {test_arr1}")
    sorted_arr1 = quicksort(test_arr1.copy())
    print(f"排序后（函数式）: {sorted_arr1}")

    test_arr1_inplace = test_arr1.copy()
    quicksort_inplace(test_arr1_inplace)
    print(f"排序后（原地）: {test_arr1_inplace}")

    # 测试用例 2：包含重复元素
    test_arr2 = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"\n原始数组: {test_arr2}")
    sorted_arr2 = quicksort(test_arr2.copy())
    print(f"排序后（函数式）: {sorted_arr2}")

    # 测试用例 3：已排序数组
    test_arr3 = [1, 2, 3, 4, 5]
    print(f"\n原始数组: {test_arr3}")
    sorted_arr3 = quicksort(test_arr3.copy())
    print(f"排序后（函数式）: {sorted_arr3}")

    # 测试用例 4：逆序数组
    test_arr4 = [9, 7, 5, 3, 1]
    print(f"\n原始数组: {test_arr4}")
    sorted_arr4 = quicksort(test_arr4.copy())
    print(f"排序后（函数式）: {sorted_arr4}")

    # 测试用例 5：单个元素
    test_arr5 = [42]
    print(f"\n原始数组: {test_arr5}")
    sorted_arr5 = quicksort(test_arr5.copy())
    print(f"排序后（函数式）: {sorted_arr5}")

    # 测试用例 6：空数组
    test_arr6 = []
    print(f"\n原始数组: {test_arr6}")
    sorted_arr6 = quicksort(test_arr6.copy())
    print(f"排序后（函数式）: {sorted_arr6}")

    print("\n" + "=" * 50)
    print("所有测试完成！")
    print("=" * 50)
