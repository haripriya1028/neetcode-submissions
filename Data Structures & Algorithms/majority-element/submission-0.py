class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=len(nums)//2
        freq={}
        for n in nums: 
            freq[n]=freq.get(n, 0)+1

        for key, val in freq.items():
            if val>k:
                return key