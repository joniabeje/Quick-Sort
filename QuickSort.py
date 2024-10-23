# A) Quicksort: Partition Even and Odd Numbers, Even Ascending, Odd Descending

def custom_quick_sort(arr):
    even_nums = [x for x in arr if x % 2 == 0]
    odd_nums = [x for x in arr if x % 2 != 0]

    quicksort(even_nums, 0, len(even_nums) - 1)
    quicksort(odd_nums, 0, len(odd_nums) - 1, reverse=True)

    return even_nums + odd_nums

def partition(arr, left, right, reverse=False):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        if reverse:
            while i < right and arr[i] > pivot:
                i += 1
            while j > left and arr[j] <= pivot:
                j -= 1
        else:
            while i < right and arr[i] < pivot:
                i += 1
            while j > left and arr[j] >= pivot:
                j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if (arr[i] > pivot and not reverse) or (arr[i] < pivot and reverse):
        arr[i], arr[right] = arr[right], arr[i]

    return i

def quicksort(arr, left, right, reverse=False):
    if left < right:
        partition_pos = partition(arr, left, right, reverse)
        quicksort(arr, left, partition_pos - 1, reverse)
        quicksort(arr, partition_pos + 1, right, reverse)

List_1 = [2, 5, 6, 8, 9, 10, 7, 3]
sorted_list = custom_quick_sort(List_1)
print(sorted_list)



# B) Quicksort with First Element as Pivot

def quicksort_first_pivot(arr, left, right):
    if left < right:
        partition_pos = partition_first_pivot(arr, left, right)
        quicksort_first_pivot(arr, left, partition_pos - 1)
        quicksort_first_pivot(arr, partition_pos + 1, right)

def partition_first_pivot(arr, left, right):
    i = left + 1
    j = right
    pivot = arr[left]

    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

List_1 = [2, 5, 6, 8, 9, 10, 7, 3]
sorted_list = quicksort_first_pivot(List_1, 0, len(List_1) - 1)
print(List_1)



# C) Quicksort with Last Element as Pivot

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

List_1 = [2, 5, 6, 8, 9, 10, 7, 3]
quicksort(List_1, 0, len(List_1) - 1)
print(List_1)