from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        在数组中找到两个数，使它们的和等于目标值，并返回它们的索引。

        参数:
        nums (List[int]): 整数数组
        target (int): 目标值

        返回:
        List[int]: 两个数的索引列表

        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        # 创建哈希表，存储数字到索引的映射
        hashtable = dict()

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算补数（target - 当前数字）
            complement = target - num

            # 如果补数已经在哈希表中，说明找到了两个数的组合
            if complement in hashtable:
                # 返回两个索引（顺序与题目要求的升序一致）
                return [hashtable[complement], i]

            # 将当前数字及其索引存入哈希表
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
