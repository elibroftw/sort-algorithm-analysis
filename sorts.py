def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_value
    return array


def selection_sort(array):
    for i in range(len(array) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, i + 1):
            if array[location] > array[position_of_max]:
                position_of_max = location

        temp = array[i]
        array[i] = array[position_of_max]
        array[position_of_max] = temp
    return array


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
    return array


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    r = 2 * i + 2

    if left < n and array[i] < array[left]: largest = left
    if r < n and array[largest] < array[r]: largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1): heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot: less.append(x)
            if x == pivot: equal.append(x)
            if x > pivot: greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else: return array


def bubble_sort(array):
    for num in range(len(array) - 1, 0, -1):
        for i in range(num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array


def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2
    return array


def comb_sort(array):
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(array) - gap):
            j = i + gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True
    return array


def counting_sort(array):
    m = max(array) + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array
