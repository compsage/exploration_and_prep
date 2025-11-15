"""
Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

Example

Input

responseTimes = [100, 200, 150, 300]
Output

2
Explanation

- Day 0: 100 (no previous days, skip)
- Day 1: 200 > average(100) = 100 → count = 1
- Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1
- Day 3: 300 > average(100, 200, 150) = 150 → count = 2
Return 2.

Input Format

The first line contains an integer n (0 ≤ n ≤ 1000), the number of days.
If n > 0, the next n lines contains an integer representing responseTimes[i].
If n = 0, the second line is omitted or empty.
Example

4
100
200
150
300
here 4 is the length of array, followed by the elements of array on each line.

Constraints

0 <= responseTimes.length <= 1000
1 <= responseTimes[i] <= 10^9 for 0 <= i < responseTimes.length

Output Format

A single integer depicting the count of days.

Sample Input 0

0
Sample Output 0

0
Sample Input 1

1
100
Sample Output 1

0
"""

def count_greater_original(response_times):
    """
    Your original solution - uses running sum and index for efficiency.
    Time: O(n), Space: O(1)
    """
    aa = 0  # running sum
    count = 0

    for i, v in enumerate(response_times):
        if i > 0 and v > aa/i:
            count += 1
        aa += v

    return count


def count_greater_slice(response_times):
    """
    Using array slicing - more readable but less efficient.
    Time: O(n^2), Space: O(n) per iteration
    """
    count = 0

    for i in range(1, len(response_times)):
        previous_elements = response_times[:i]
        avg = sum(previous_elements) / len(previous_elements)
        if response_times[i] > avg:
            count += 1

    return count


def count_greater_itertools(response_times):
    """
    Using itertools.accumulate to track running sums.
    Time: O(n), Space: O(n)

    How accumulate works:
    - accumulate takes an iterable and returns running totals
    - Example: accumulate([100, 200, 150, 300]) produces:
      [100, 300, 450, 750]
      where:
        100 = 100
        300 = 100 + 200
        450 = 100 + 200 + 150
        750 = 100 + 200 + 150 + 300
    - So running_sums[i] contains the sum of all elements from index 0 to i (inclusive)
    - To get avg of elements BEFORE index i, we use running_sums[i-1] / i

    Similar functions to accumulate:
    - functools.reduce(): Reduces entire sequence to single value
      Example: reduce(lambda x,y: x+y, [1,2,3,4]) -> 10
    - itertools.chain(): Flattens multiple iterables into one
      Example: chain([1,2], [3,4]) -> [1,2,3,4]
    - itertools.groupby(): Groups consecutive items by key
      Example: groupby([1,1,2,2,3]) -> [(1,[1,1]), (2,[2,2]), (3,[3])]
    - itertools.islice(): Slices an iterator
      Example: islice([1,2,3,4,5], 2, 4) -> [3,4]
    - itertools.takewhile(): Takes items while condition is true
      Example: takewhile(lambda x: x<3, [1,2,3,4]) -> [1,2]
    - numpy.cumsum(): Like accumulate but returns numpy array (if using numpy)
      Example: np.cumsum([1,2,3,4]) -> array([1,3,6,10])
    """
    from itertools import accumulate

    if len(response_times) <= 1:
        return 0

    # Get running sums: [100, 300, 450, 750] for input [100, 200, 150, 300]
    running_sums = list(accumulate(response_times))
    count = 0

    for i in range(1, len(response_times)):
        # running_sums[i-1] contains sum of all elements before index i
        avg = running_sums[i-1] / i
        if response_times[i] > avg:
            count += 1

    return count


def count_greater_functional(response_times):
    """
    Functional programming style using list comprehension.
    Time: O(n^2), Space: O(n)
    """
    return sum(
        1 for i in range(1, len(response_times))
        if response_times[i] > sum(response_times[:i]) / i
    )


def count_greater_explicit(response_times):
    """
    Most explicit version - shows every step clearly.
    Time: O(n), Space: O(1)
    """
    if len(response_times) <= 1:
        return 0

    count = 0
    running_sum = response_times[0]

    for i in range(1, len(response_times)):
        current_value = response_times[i]
        average_of_previous = running_sum / i

        if current_value > average_of_previous:
            count += 1

        running_sum += current_value

    return count


# Test with examples
if __name__ == "__main__":
    test_cases = [
        ([100, 200, 150, 300], 2),
        ([], 0),
        ([100], 0),
        ([100, 50], 0),
        ([100, 200], 1),
    ]

    functions = [
        count_greater_original,
        count_greater_slice,
        count_greater_itertools,
        count_greater_functional,
        count_greater_explicit
    ]

    for func in functions:
        print(f"\n{func.__name__}:")
        for inputs, expected in test_cases:
            result = func(inputs)
            status = "✓" if result == expected else "✗"
            print(f"  {status} {inputs} -> {result} (expected {expected})")
