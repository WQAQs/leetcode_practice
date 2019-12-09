class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 1. 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])

            # 2. 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

            # 3. 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
            max_l = nums[len(nums) // 2 - 1]
            tmp = 0
            for i in range(len(nums) // 2 - 1, -1, -1):
                tmp += nums[i]
                max_l = max(tmp, max_l)
            max_r = nums[len(nums) // 2]
            tmp = 0
            for i in range(len(nums) // 2, len(nums)):
                tmp += nums[i]
                max_r = max(tmp, max_r)

        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

nums = [-2,1,-3,4,-1,2,1,-5,4]
so = Solution()
out = so.maxSubArray(nums)
out