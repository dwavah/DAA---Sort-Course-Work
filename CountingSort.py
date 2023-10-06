def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    counting_arr = [0] * range_val
    output_arr = [0] * len(arr)

    for num in arr:
        counting_arr[num - min_val] += 1

    for i in range(1, range_val):
        counting_arr[i] += counting_arr[i - 1]

    for num in arr:
        output_arr[counting_arr[num - min_val] - 1] = num
        counting_arr[num - min_val] -= 1

    return output_arr
