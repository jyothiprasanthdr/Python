def selection_sort(arr, n):
    for i in range(0, n - 1):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
        print(i)


if __name__ == "__main__":
    arr = [6, 7, 2, 4, 8, 3, 1]
    selection_sort(arr, len(arr))
    print(arr)
