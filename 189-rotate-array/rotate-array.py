class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # while (k != 0) :
        #     n = len(nums)

        #     last = nums[-1]
        #     for i in range(n-1 , -1 , -1):
        #         # print(nums[i])
        #         nums[i] = nums[i-1]
        #     nums[0] = last

        #     k -= 1

        # return nums




        # n = len(nums)
        # k %= n
        # nums.reverse()
        # num1 = (nums[ : k])
        # num2 = (nums[k : ])
        
        # num1.reverse()
        # num2.reverse()
        # # print(num1)
        # # print(num2)

        # nums[:] = num1 + num2


        n = len(nums)
        k = k % n
        nums1 = nums[ : n-k]
        nums2 = nums[n-k : ] + nums1
        nums[:] = nums2