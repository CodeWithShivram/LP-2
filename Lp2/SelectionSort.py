def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
# Example array
arr = [64, 25, 12, 22, 11]

# Perform selection sort
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:")
print(sorted_arr)
