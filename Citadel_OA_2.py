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
