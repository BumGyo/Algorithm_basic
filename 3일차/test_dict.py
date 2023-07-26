# 사전(Dictionary) 자료 구조를 사용해서 데이터를 키와 값의 쌍으로 메모리에 보관하기

# 영한 사전 예제에 사용할 딕셔너리 변수를 선언
my_eh_dict = {}

# 한영 사전 예제에 사용할 딕셔너리 변수를 선언
my_he_dict = {}

# 1. 키와 값의 쌍으로 새로운 사전 변수를 선언
my_dict1 = {"key1":"value1", 2:"홍길동", "key3":"김길동"}
# 키 : 변하는 자료 구조는 사용할 수 없습니다!! -> 리스트를 사용할 수 없음
# 튜플은 사용할 수 있습니다!!

# 2. 키와 값을 지정하지 않은 빈 딕셔너리 변수를 선언
my_dict2 = {}

# 3. dict 클래스 이름을 사용해서 빈 딕셔너리 변수를 선언
my_dict3 = dict()

# 4. my_dict1 딕셔너리 변수가 갖고 있는 모든 "키"들을 읽어와서 화면에 출력하기
# -> keys( ) 함수를 호출
for k in my_dict1.keys():
    print(k)

# 5. my_dict1 딕셔너리 변수가 갖고 있는 모든 "값"들을 읽어와서 화면에 출력하기
# -> values( ) 함수를 호출
for value in my_dict1.values():
    print(value)

# 6. 키와 값을 한번에 출력(딕셔너리 변수에서 가져오기)하고 싶은 경우에는 items( ) 함수를 호출
for k, v in my_dict1.items():
    print("키는 ",k,", 값은 ",v)

# 7. len( ) 함수를 호출해서 키의 갯수를 알아오기
len_my_dict1 = len(my_dict1)
print("my_dict1 딕셔너리 변수가 갖고 있는 키의 갯수는 ", len_my_dict1)

# 새로운 함수를 만든 다음에 영한 사전 딕셔너리 변수에 저장될 키와 값들을 사용자로부터 입력 받기
def  input_eh_func(dict1_p):
    print("영한 사전 입력 함수가 호출됨")
    print("키를 입력하세요: ", end="")
    key1 = input()
    print("값을 입력하세요: ", end="")
    value1 = input()
    dict1_p[key1] = value1
    print("사용자가 입력한 키는 ",key1, " 값은 ", value1)
    len_dict1_p = len(dict1_p)
    print("현재까지 입력된 데이터 갯수는 ", len_dict1_p)

# 사용자가 입력한 키를 영한 사전 딕셔너리 변수에서 검색해주는 함수 만들기
def  search_eh_func(dict1_p, find_key_p):
    print("영한 사전 딕셔너리 변수에서 특정 키를 검색해주는 함수")
    if len(dict1_p) == 0:
        print("현재 영한 사전에 등록된 키가 하나도 없습니다!!")
        return False

    # 사용자가 입력한 키가 있는지를 검색하기
    if find_key_p == "":
        print("사용자가 입력한 키가 없습니다!!")
        return False

    print("사용자가 찾을 키는 ", find_key_p, " 입니다!!")
    # 검색한 결과를 보관할 변수를 선언 : 비교 전이므로 거짓(False) 값으로 지정
    result_find = False
    for k, v in dict1_p.items():
        print("반복문 안입니다!!")
        if k == find_key_p:
            print("키를 찾았습니다!!")
            print("값은 ", v, " 입니다!!")
            result_find = True
            break
    print("for 반복문을 벗어났습니다!!")
    if result_find == False:
        print(find_key_p, " 키를 영한 사전에서 찾지 못했습니다!!")
    return True

# 위에서 만든 input_eh_func( ) 함수를 호출하기 : 한 번만 실행되는 함수
input_eh_func(my_eh_dict)

# 여러 번 input_eh_func( ) 함수를 실행하기 위해서 while 반복문을 함께 사용하기
# -> 사용자로부터 y 또는 n 문자를 입력 받아서 반복 여부를 결정하기
while True:
    print("영한 사전에 저장될 키와 값들을 사용자로부터 입력 받습니다!!")
    input_eh_func(my_eh_dict)
    print("계속하려면 y를 중단하시려면 n을 입력하세요: ", end="")
    y_n = input()
    if y_n == 'y' or y_n == 'Y':
        print("계속해서 키와 값들을 입력받습니다!!")
        continue
    elif y_n == 'n' or y_n == 'N':
        print("키와 값 입력을 중단합니다!!")
        break
    else:
        print("입력 오류!!")
        while True:
            print("다시 꼭!! y 또는 n 문자 중에서 하나를 입력하세요: ", end="")
            y_n = input()
            if y_n == 'y' or y_n == 'Y' or y_n == 'n' or y_n == 'N':
                print("사용자가 입력한 문자는 y 또는 Y 또는 n 또는 N 입니다!!")
                print("입력을 중단합니다!!")
                break
        print("while True 반복문을 벗어났습니다!!")
        if y_n == 'n' or y_n == 'N':
            print("첫 번째 while True: 반복문을 벗어납니다!!")
            break

# 방금 만든 search_eh_func( ) 함수를 호출합니다!!
# 사용자로부터 찾을 키를 입력 받아야 합니다!!
print("영한 사전에서 찾을 키를 입력하세요: ", end="")
find_key = input()
result_find_key = search_eh_func(my_eh_dict, find_key)
if find_key == True:
    print("search_eh_func() 함수 실행 성공")
else:
    print("search_eh_func() 함수 실행 실패")

# is 연산자를 사용해서 논리 값을 비교할 수 있습니다!!
if find_key is True:
    print("search_eh_func() 함수 실행 성공")
else:
    print("search_eh_func() 함수 실행 실패")





















































