arr = [1, 2, 3, 4, 5]
i, j = 0, len(arr)-1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]   # swap
    i += 1
    j -= 1
print("Reversed Array:", arr)   # [5, 4, 3, 2, 1]
