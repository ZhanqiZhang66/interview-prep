class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        pre_product = [1]
        post_product = [1]
        for i in range(len(nums) - 1):
            pre_product.append(pre_product[i] * nums[i])
            post_product.append(post_product[i] * nums[len(nums) - i - 1])
        post_product.reverse()
        return [a * b for a, b in zip(pre_product, post_product)]

        