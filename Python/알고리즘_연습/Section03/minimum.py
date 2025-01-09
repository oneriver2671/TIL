'''
최솟값 구하기
'''

# 방법 1
arr = [5, 3, 7, 9, 2, 10, 6, 1]
arrMin = arr[0]

for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)


# 방법 2
arr = [5, 3, 7, 9, 2, 10, 6, 1]
arrMin = float('inf')

for x in arr:
    if x < arrMin:
        arrMin = x

print(arrMin)
