'''
대표값(4번 문제) 오류 수정
'''
from decimal import ROUND_HALF_EVEN

'''
round는 round_half_even 방식을 택한다.
ROUND_HALF_EVEN : 딱 중간값인 4.5 일 때. 짝수값으로 근사값을 처리한다. (e.g. 4.5 -> 4 / 5.5 -> 6)
-> 정확한 반올림이 아님.
'''

# round를 쓰지 말고 아래와 같이 처리.
a = 66.5
a = a + 0.5
a = int(a)



