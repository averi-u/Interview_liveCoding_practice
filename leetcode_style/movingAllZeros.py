"""
Given an array, we need to move all the zeros
to the end of the array. 
and move the nonzero elements to the end of 
array. 

[0, 23, 2, 1, 4, 0, 34, 2, 0] -> 
[23, 2, 1, 4, 34, 2, 0, 0]

approach: two pointer. the last non zero point
to the index to place a nonzero elemenet 
iterate with i, when nums[i] != 0, swap 
nums[i] num[last_non_zero] and increa last 
non-zero. 

edge_cases: all zeros, no zeros, empty, duplicates
really large number
"""

def move_zeros(self, data: list[int]):
    fill_index = 0

    for n in data: 
        if n != 0: 
            data[fill_index] = num 
            fill_index += 1

    for rem_index in range(fill_index, len(data)): 
        data[rem_index] = 0

    # return data 

#testing 
data1 = []
move_zeros(data1)
print(data1)

# print(move_zeros([0, 0]))
# print(move_zeros([1, 2, 5]))
# print(move_zeros([0, 2, 4, 1, 0, 3, 0]))
# print(move_zeros([2, 1, 1, 30, 0]))
# print(move_zeros([1, 1, 1, 1, 1]))
# print(move_zeros([1000000000000, 0, 2]))