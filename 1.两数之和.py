from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 创建哈希表，存储数字到索引的映射(创建一个空字典)等同于hashtabel={}
        hashtable = dict()

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算补数（target - 当前数字）
            complement = target - num

            # 如果补数已经在哈希表中，说明找到了两个数的组合
            if complement in hashtable:
                # 返回两个索引（顺序与题目要求的升序一致）
                return [hashtable[complement], i]

            # 将当前数字(key)及其索引(value)存入哈希表,
            # 因为哈希表通过key读取value比较方便,所以使用数字当key,索引当作value;
            hashtable[num] = i

        # 如果没有找到符合条件的组合，返回空列表
        return []


# 使用示例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"nums: {nums1}, target: {target1}")
    print(f"结果: {result1}")  # 输出: [0, 1]

    # 测试用例2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"nums: {nums2}, target: {target2}")
    print(f"结果: {result2}")  # 输出: [1, 2]

    # 测试用例3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"nums: {nums3}, target: {target3}")
    print(f"结果: {result3}")  # 输出: [0, 1]

# 这个题目主要考察的是哈希表,
# 算法思路
# 核心思想：利用哈希表存储已经遍历过的数字及其索引
#
# 一次遍历：在遍历数组时，同时查找和存储，只需要遍历一次数组
#
# 查找逻辑：对于当前数字 num，检查 target - num 是否已经在哈希表中

# ------------------------------------------------------------------
# 知识点1:
# 哈希表
# 哈希表是一种高效的数据结构，它通过键（Key） 来直接访问存储的值（Value），实现了快速的查找、插入和删除操作。
# 哈希表是现代编程中最重要的数据结构之一，几乎所有的编程语言都内置了哈希表实现\
# （如Java的HashMap、Python的dict、JavaScript的Object/Map）。Python 的字典（dict）就是一个高度优化、工业级的哈希表实现。

# ------------------------------------------------------------------
# 知识点2:
# enumerate() 函数用于将一个可迭代对象（如列表、元组、字符串）转换为一个枚举对象，它会同时返回索引和元素值。
# 一般用在 for 循环当中。
# 例如:
# >>>seq = ['one', 'two', 'three']
# >>> for i, element in enumerate(seq):
# >>>     print i, element
# 输出:
# ...   0 one
# ...   1 two
# ...   2 three

# ------------------------------------------------------------------
# 知识点3:
# 字典相关操作

# 字典中获取指定键(key)的值(value)
# dict=[key1]

#添加键值对
# dict[key]=value

# ------------------------------------------------------------------
#知识点4:
# if语句与字典结合有多种常见用法:

# 检查字典的键（key）中是否存在某个值。
# if key in dict:

# 检查值是否存在:
# if value in dict.values():
#
# 检查键值对是否存在:
# if (key, value) in dict.items():
