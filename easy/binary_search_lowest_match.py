# =============================================================================
# BINARY SEARCH - FIND LOWEST (LEFTMOST) MATCH
# =============================================================================
#
# WHAT IS BINARY SEARCH?
# Binary search is an efficient algorithm for finding a value in a SORTED array.
# Instead of checking every element one by one (linear search, O(n)), binary
# search repeatedly divides the search space in half, achieving O(log n) time.
#
# KEY INSIGHT: Each comparison eliminates HALF of the remaining elements.
# For 1,000,000 elements: linear search = up to 1,000,000 checks
#                         binary search = at most 20 checks!
#
# THIS VARIANT: Finds the LOWEST (leftmost/first) index where target appears.
# This is useful when you have duplicates and want the first occurrence.
#
# =============================================================================


def binary_search(nums, target):
    """
    Find the FIRST (lowest index) occurrence of target in a sorted array.

    Args:
        nums: A sorted list of numbers
        target: The value to find

    Returns:
        The lowest index where target is found, or -1 if not found
    """

    # STEP 1: Define the search boundaries
    # We'll narrow this range until we find our answer
    start = 0
    end = len(nums) - 1

    # STEP 2: Keep searching while we have a valid range
    # The loop ends when start > end (no more elements to check)
    while start <= end:

        # STEP 3: Calculate the middle index
        # Integer division (//) ensures we get a whole number
        # Example: (0 + 5) // 2 = 2
        mid = (start + end) // 2

        # STEP 4: Decide which half to search next
        #
        # KEY DIFFERENCE FROM STANDARD BINARY SEARCH:
        # When target == nums[mid], we DON'T return immediately!
        # Instead, we keep searching LEFT to find an earlier occurrence.

        if target <= nums[mid]:
            # Target is less than OR EQUAL to middle element
            # The first occurrence must be at mid or to its LEFT
            # So we discard the right half by moving 'end' left
            end = mid - 1

        elif target > nums[mid]:
            # Target is greater than middle element
            # The first occurrence must be to the RIGHT
            # So we discard the left half by moving 'start' right
            start = mid + 1

    # STEP 5: After the loop, 'start' points to where target SHOULD be
    # (the smallest index where nums[index] >= target)
    # But we need to verify it's actually our target!
    if start < len(nums) and nums[start] == target:
        return start
    else:
        return -1  # Target not found


# =============================================================================
# WALKTHROUGH EXAMPLE
# =============================================================================
# nums = [1, 3, 5, 5, 5, 7, 9]    target = 5
#         0  1  2  3  4  5  6    (indices)
#
# Round 1: start=0, end=6, mid=3
#          nums[3]=5, target=5
#          5 <= 5? YES → end = 3-1 = 2
#          (We found a 5, but keep searching LEFT for earlier ones)
#
# Round 2: start=0, end=2, mid=1
#          nums[1]=3, target=5
#          5 <= 3? NO
#          5 > 3? YES → start = 1+1 = 2
#
# Round 3: start=2, end=2, mid=2
#          nums[2]=5, target=5
#          5 <= 5? YES → end = 2-1 = 1
#
# Loop ends: start=2 > end=1
# Check: nums[2]=5 == target? YES!
# Return 2 ✓ (the FIRST occurrence of 5)
# =============================================================================


# =============================================================================
# TIME & SPACE COMPLEXITY
# =============================================================================
# Time:  O(log n) - We halve the search space each iteration
# Space: O(1)     - Only a few variables, regardless of input size
# =============================================================================


# Test case with duplicates
nums = [5, 5, 5]
target = 5

# Output will be 0 (the LOWEST/FIRST index where 5 appears)
# Note: If you wanted the HIGHEST index (2), you'd use a different variant
print(f"Array: {nums}")
print(f"Target: {target}")
print(f"Lowest index found: {binary_search(nums, target)}")
