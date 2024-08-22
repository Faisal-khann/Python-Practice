def selection_sort(arr):
    n = len(arr)
    for i in range(n-1): # Iterates from 0 to n-2 (inclusive)
        min = i
        for j in range(i+1, n): #The inner loop iterates from i + 1 to n - 1 to find the minimum element in the unsorted portion of the list.
            if arr[j] < arr[min]:
                min = j

        # Swap
        arr[min], arr[i] = arr[i], arr[min]

    print("After Selection sort:")
    for i in range(n):
        print(arr[i], end=" ")
    print()


# Example usage:
arr = [35, 25, 15, 45, 5]
selection_sort(arr)