# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def matrix_sum(nums):
    i = len(nums)
    j = 0
    ret = 0
    while j < i:
        ret += nums[j][j]
        j += 1
    return ret


def matrix_search(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == target:
                return True
    return False

def recursive_search(nums,target):
    if nums[0] == target:
        return True
    elif len(nums) == 1:
        return False
    recursive_search(nums[1:], target)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(recursive_search([1,2,3,4,5,6],0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
