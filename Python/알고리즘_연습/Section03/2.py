'''
k번째 약수 출력하기
'''

# import sys
# sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: 
    print(-1)


# k번째 약수가 발견되지 않는 경우도 있음 (-> n: 6, k: 5)
# for~else 구문이 있다. break가 작동하지 않고 정상적으로 끝나면, else문이 실행됨.
