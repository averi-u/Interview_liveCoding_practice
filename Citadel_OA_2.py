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
    