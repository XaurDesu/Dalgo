"""
#longest increasing subsequence
def lis(array):
    l = len(array)
    # Inside LIS we want to record the subproblem LIS[i]
    # i.e LIS[i] contains the longest increasing subsequence
    # that ends at i. LIS is initialized with all records in 1
    # because an unary array has lis 1
    LIS = [1] * l
    for i in range(1,l):
        subproblems = []
        # The idea is to test each increasing subsequence ending at i
        for k in range(i):
            # if the k element keeps the subsequence increasing
            # the recorded LIS at k should be store
            if array[k] < array[i]:
                subproblems.append(LIS[k])
        # The LIS at i should be the max of the LIS for the subproblems
        # plus one beacuse i is a new element of the sequence.
        # Notice tha if subproblems is empty LIS[i] don't change. 
        # subproblems empty means that there is no lower element that
        # array[i] for all j<i
        # In this case default means that max([],default=0) = 0
        LIS[i] = 1 + max(subproblems,default=0)
    #return the max longest increasing subsequence
    return max(LIS,default=0)

SACADO DE LAS DIAPOSITIVAS
"""

def maximum_sum_increasing_subsequence(nums):
    max_sum = 0
    ret = []

    

    return ret