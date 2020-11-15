class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)
        both_list = [nums[:length//2], nums[length//2:]]
        list_tup = [(x,y) for x,y in zip(both_list[0], both_list[1])]
        return [item for x in list_tup for item in x ]
