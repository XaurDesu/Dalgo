import heapq as hp
def largest_nth_element(array: list[int], n: int) -> int:
    nums = []
    for i in array:
        hp.heappush(nums, i)
        if len(nums) > n:
            hp.heappop(nums)
    return nums[0]
