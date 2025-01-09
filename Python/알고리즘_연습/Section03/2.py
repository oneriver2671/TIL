'''
K번째 수
'''

# import sys
# sys.stdin=open("input.txt", "rt")

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr[s-1:e])   # s번째 ~ e번째
    print('#' + str(i+1), arr[k-1])

