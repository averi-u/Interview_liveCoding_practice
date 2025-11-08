# -----------------------------------------------------------
# Citadel OA Question from Rednote(Reconstructed)
#
# You are given an array layer[] of size n.
#
# Each generation you may choose ONE layer index:
#   - If the generation number is ODD:     add +1 to that layer
#   - If the generation number is EVEN:    add +2 to that layer
#
# You want all layers to eventually have the same number of neurons.
#
# Goal: find the MINIMUM number of generations G needed.
#
# Notes:
# - You may only increment one element per generation.
# - Final equal value T is not necessarily max(layer); it might be larger.
# - You must choose T and G such that:
#       total odd ops  needed <= number of odd generations  (ceil(G/2))
#       total even ops needed <= number of even generations (floor(G/2))
# - Solve using binary search on T and binary search on G.
#
# -----------------------------------------------------------


def solve(layer):
    import math

    arr = layer
    n = len(arr)
    mx = max(arr)

    # Check if a given target T is achievable in <= G generations.
    def can_finish(T, G):
        total_odd = 0     # number of +1 ops needed
        total_even = 0    # number of +2 ops needed

        for x in arr:
            d = T - x
            if d < 0:
                return False  # can't decrease values
            total_odd += d % 2
            total_even += d // 2

        # available operations in G generations
        odd_available = (G + 1) // 2     # ceil(G/2)
        even_available = G // 2          # floor(G/2)

        return total_odd <= odd_available and total_even <= even_available

    # For a fixed T, binary search to find the minimum G needed.
    def min_G_for_T(T):
        low, high = 0, 10**18
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_finish(T, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    # Binary search on final target T
    left, right = mx, mx + 10**18
    best = right

    while left <= right:
        mid = (left + right) // 2
        G_for_mid = min_G_for_T(mid)
        best = min(best, G_for_mid)

        # heuristic: if increasing T reduces G, keep searching higher
        # else search lower
        if G_for_mid > best:
            left = mid + 1
        else:
            right = mid - 1

    return best


# -----------------------------------------------------------
# Example Usage
# -----------------------------------------------------------
layer = [1, 1, 2, 4]
print(solve(layer))     # expected output: 5
