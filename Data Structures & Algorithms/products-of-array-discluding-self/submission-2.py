class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        for i in range(len(nums) - 1):
            pre.append(pre[i] * nums[i])
            post.append(post[i] * nums[len(nums) -1 - i])
        post = post[::-1]
        
        return [i * j for i, j in zip(pre, post)]

        