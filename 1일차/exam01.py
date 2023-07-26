# 한 줄 주석 명령어
'''
여러 줄 주석 명령어(문자열 표현)
'''
"""
여러 줄 주석 명령어(문자열 표현)
"""

print("하나의 정수를 입력하세요: ", end="")
input_number = int(input())
if input_number == 0:
    print("0을 입력했습니다!", end="")
elif input_number < 0:
    print("0보다 작은 정수를 입력했습니다", end="")
elif input_number > 0:
    print("0보다 큰 정수를 입력했습니다", end="")
    if input_number > 1:
        print("사용자가 입력한 정수는 1보다 큽니다")
        sum = 1
        i = 2
        while i <= input_number:
            print("현재 변수 i의 값은 ", i)
            print("현재 변수 sum의 값은" ,sum)
            sum += i
            i = i + 1
        print("최종 결과는 ", sum)


        "공식을 사용해서 덧셈 계산을 누적하기"
