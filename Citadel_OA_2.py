"""
Citadel OA from leetcode
Question 1: Subarray with a Specific Property

Problem Statement:
Given an array of length (10^5), we had to find the number of subarrays that satisfied the condition:
arr[i] == arr[j] == sum(arr[i+1 : j-1])
where (i) and (j) are indices of the array.

To solve this problem, I used a prefix array combined with hashing.
"""

def count_special_subarrays(arr):

    from collections import defaultdict

    prefix = 0 
    ans = 0 
    mp = defaultdict(lambda: defaultdict(int))

    mp[arr[0]][0] = 1 
    prefix += arr[0]

    for j in range(1, len(arr)): 
        b = arr[j]
        target = prefix - 3 * b
        ans += mp[b].get(target, 0)

        mp[b][prefix] += 1 
        prefix += b

    return ans 

"""
Question 2: Minimum Operations to Reduce Array Elements to Zero

Problem Statement:
Given an array and two integers (x) and (y), in one operation, we can pick one element and subtract (x) from it, and subtract (y) from all other elements. The goal is to determine the minimum number of operations needed to reduce all elements of the array to zero.
"""
from math import ceil 


def can_k(arr, x, y, k): 
    need_bigHits = 0 
    diff = x - y 
    for v in arr: 
        left = v - k*y 
        if left > 0: 
            need_bigHits += ceil(left / diff)
            if need_bigHits > k: 
                return False
    return need_bigHits <= k 


def min_operations(arr, x, y): 
    left, right = 0, max(arr) // min(x, y) + 5 
    # +5 or anything small for room for binary search 

    while left < right: 
        mid = (left + right ) // 2 
        if can_k(arr, x, y, mid): 
            right = mid 
        else: 
            left = mid + 1 
    return left 