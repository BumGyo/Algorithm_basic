# 3! 팩토리얼을 해결하는 예제를 작성

"""
재귀호출 방법을 사용해서 팩토리얼을 구해주는 함수를 구현
"""
def  my_fact(n):
    # 함수의 호출 여부를 확인하기 위해서 print( ) 함수를 호출
    print("my_fact(n) 함수가 호출됨!!")
    print("현재 변수 n의 값은 ", n)
    # if 명령어를 작성해서 자신의 함수를 탈출할 수 있는 명령어를 작성
    # -> 매개 변수 n으로 들어온 정수 값이 1 이하인 경우에는 무조건 1을 반환
    if n <= 1:
        print("n <= 1")
        return 1
    else:
        print("else:")
        return n * my_fact(n-1)

number = 3
result = 1
for i in range(1, number+1):
    result *= i
    print("현재 변수 i의 값은 ", i)
    print("현재 변수 result의 값은 ", result)
    # result = result * i

print("3! 결과는 ", result)

# 위에서 만든 my_fact( ) 함수를 호출해서 3! 팩토리얼을 구합니다!!
result = my_fact(3)
print("3! 결과는 ", result)











