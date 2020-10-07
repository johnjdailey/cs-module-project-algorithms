#sliding_window_max/sliding_window_max.py



'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    list_of_ints = []
    prev_max = None
    for i in range(1 + len(nums) - k):
        if i != 0 and prev_max != nums[i - 1]:
            prev_max = max((prev_max, nums[i + k - 1]))
        else:
            prev_max = max(nums[i: i + k])
        list_of_ints.append(prev_max)
    return list_of_ints


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
