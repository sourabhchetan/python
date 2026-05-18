arr = [10, 5, 20, 8]
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)  # 10
