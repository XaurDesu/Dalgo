# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def matrix_multiplication(nums):
    i = len(nums)
    j = 0
    ret = 0
    while j < i:
        ret *= nums[j][j]
        j += 1
    return ret


def matrix_search(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == target:
                return True
    return False


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
