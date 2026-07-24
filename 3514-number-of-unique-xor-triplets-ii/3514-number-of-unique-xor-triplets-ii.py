class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:

        update = lambda x: num^x

        pairs, trips = set([0]), set(nums),  
        digits = 2** max(nums).bit_length()

        while nums:
            num = nums.pop()
            trips|= set(map(update, pairs))
            pairs|= set(map(update, nums))
            if len(trips) == digits: break
 
        return len(trips)