"""
집합(Set) 자료 구조를 사용하는 예제를 작성
"""
# 학생 이름이 있는 리스트 변수에서 동명 이인을 찾아낸 후에 집합 변수에 이름을 저장하는 함수
def  getSameName(list_p1, set_p1):
    # list1_p1 : 학생 이름을 갖고 있는 리스트 변수의 주소를 받는 매개 변수
    # set_p1 : 동명 이인의 이름을 보관할 집합 변수의 주소를 받는 매개 변수
    print("getSameName(list_p1, set_p1) 함수가 호출됨")

    # 1. 학생 이름이 하나라도 있는지를 검사하기
    # -> 최소 2개의 데이터가 있는지를 검사하기
    len_name = len(list_p1)
    if len_name != 2:
        print("데이터 갯수(학생 수가)가 2가 아닙니다!!")
        print("더 이상 프로그램 실행을 진행할 수 없습니다!!")
        return False

    # 2. 학생 수를 화면에 출력하기
    print("학생 수는 ", len_name, " 입니다!!")

    # 3. 2개의 반복문을 작성해서 동명 이인을 가려냅니다!!
    for i in range(0, len(list_p1) - 1):
        # 비교 대상의 데이터들의 위치 번호를 제어하는 반복문
        for j in range(i + 1, len(list_p1)):
            if list_p1[i] == list_p1[j]:
                print("동명 이인을 발견함!!")
                print("이름은 ", list_p1[j], " 입니다!!")
                set_p1.add(list_p1[j])
    print("함수 종료!!")
    return True

def show_data_set(set_p):
    len_set_p = len(set_p)
    if len_set_p == 0:
        print("현재 집합 변수에 데이터가 없음")
        return False
    print(set_p)
    return True

# 빈(데이터가 하나도 없는) 집합 변수를 선언
set1 = set()
# 리스트 변수도 선언해 주세요!!
# 학생의 이름을 보관하는 변수를 선언
student_name_list = ["홍길동","김길동","나길동","홍길동","홍길동"]
# 위에서 선언한 리스트 변수에 저장되어 있는 학생 이름 중에서 동명 이인의 이름만을 저장하는
# 집합 변수를 선언
student_name_set = set()


"""
사용자로부터 데이터를 입력 받은 다음에 집합 변수에 저장하기
-> while True : 
        pass  # 무한 반복문
-> 사용자가 n을 입력하면 반복문을 탈출할 수 있도록 합니다!!
"""

while True:
    print("set(집합) 자료 구조를 사용하는 예제 입니다!!")
    print("set 집합에 저장할 데이터를 입력하세요: ", end=" ")
    temp_value = input()
    # add( ) 함수를 호출해서 집합 변수에 새로운 데이터를 저장
    set1.add(temp_value)
    print("사용자가 입력한 데이터는 ", temp_value, " 입니다!!")
    # 사용자로부터 하나의 문자를 입력받아서 반복 여부를 결정하기
    print("계속하시려면 y를 입력하시고, 중단하시려면 n을 입력하세요: ", end=" ")
    y_n = input()
    # lower() 함수를 호출하면 대문자를 입력한 경우에는 소문자로 바꾸어 줍니다!!
    y_n = y_n.lower()
    if y_n == 'y':
        print("계속해서 사용자로부터 데이터를 입력받습니다!!")
        continue # 위로 이동하게 합니다!! -> while 반복문의 조건으로 강제 이동
    elif y_n == 'n':
        print("데이터 입력을 중단합니다!!")
        break # while True: 무한 반복문 전체를 탈출(벗어납니다!!)
    else:
        print("다른 문자를 입력하셨습니다!!")
        # 다시 사용자에게 y 또는 n 문자를 입력받을 수 있는 반복문을 만듭니다!!
        while True:
            print("다시 y 또는 n 둘 중의 하나를 입력하세요: ", end=" ")
            y_n = input()
            y_n = y_n.lower()
            if y_n == 'y' or y_n == 'n':
                print("사용자가 입력한 문자는 y 또는 n 입니다!!")
                print("입력을 중단하기 위해서 break 명령어를 실행")
                break
        print("while 반복문을 탈출하였습니다!!")
        if y_n == 'n':
            break

print("입력 종료!!")
print("위에서 만들었던 show_data_set( ) 함수를 호출")
result = show_data_set(set1)
if result == True:
    print("show_data_set(set1) 함수 실행 성공")
else:
    print("show_data_set(set1) 함수 실행 실패(데이터가 없는 경우)")

# 위에서 만든 getSameName( ) 함수를 호출
result = getSameName(student_name_list, student_name_set)
if result == True:
    print("동명 이인 처리 성공!!")
else:
    print("동명 이인 처리 실패!!")

# 집합 변수가 갖고 있는 동명 이인의 이름을 화면에 출력하기
len_set1 = len(student_name_set)
if len_set1 == 0:
    print("화면에 출력할 동명 이인의 이름이 없습니다!!")
else:
    print("화면에 출력할 동명 이인의 이름이 있습니다!!")
    print(student_name_set)









































