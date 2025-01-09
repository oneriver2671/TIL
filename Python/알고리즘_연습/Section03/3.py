'''
K번째 큰 수
'''
# 3장을 뽑을 수 있는 모든 경우의 수를 기록. 그 3장의 합계 중 가장 큰 경우.

# import sys
# sys.stdin=open("input.txt", "rt")

'''
정답
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = set()   # 중복 제거 필요

# 삼중 for문
for i in range(n):   # 첫번째 뽑기
    for j in range(i+1, n):   # 두번째 뽑기
        for m in range(j+1, n):   # 세번째 뽑기
            ijm = arr[i] + arr[j] + arr[m]
            res.add(ijm)

# for문 돌려서 빼냐 vs list로 만들어서 빼냐.
# 1. list로 전환
res = list(res)
res.sort(reverse=True)
print(res[k-1])


'''
내가 쓴 답
- 합계 구할 때, value를 더한 것이 아니라 index 번호끼리 계산함.
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = set()   # 중복 제거 필요

# 삼중 for문
for i in range(n):   # 첫번째 뽑기
    for j in range(i+1, n):   # 두번째 뽑기
        for m in range(j+1, n):   # 세번째 뽑기
            ijm = i + j + m       # -> 여기서 실수.
            res.add(ijm)

# for문 돌려서 빼냐 vs list로 만들어서 빼냐.
# 1. list로 전환
res = list(res)
res.sort(reverse=True)
print(res[k-1])

