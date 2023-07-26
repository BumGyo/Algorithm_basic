"""
리스트 변수를 사용해서 스택 메모리 구조를 표현하기

1. 프로그램 구조 : 무한 반복문
   예) while True:
            print("메뉴를 화면에 출력")

2. 화면에 출력할 메뉴 내용:
   1) 데이터 입력
   2) 데이터 검색
   3) 데이터 삭제
   4) 데이터 출력
   5) 프로그램 종료

"""
# 리스트 자료형을 사용해서 스택 변수를 선언
my_stack_list = []
# 위에서 선언한 스택 변수가 현재 갖고 있는 데이터 갯수를 보관할 변수
count_my_stack_list = 0

# 데이터 입력 함수를 새로 만들겠습니다!!
# my_stack_list 스택 변수를 받는 매개 변수를 선언 : my_stack_list_p(parameter)
# 사용자가 입력한 데이터를 받는 매개 변수를 선언 : value_p
def  input_func(my_stack_list_p,  value_p):
    # global 명령어를 사용해서 count_my_stack_list 전역 변수를 사용하기
    global  count_my_stack_list
    # 함수 호출 여부를 화면에 출력
    print("input_func() 함수가 호출되었습니다!!")
    # my_stack_list_p 스택 리스트 변수가 갖고 있는 append( ) 함수를 호출
    my_stack_list_p.append(value_p)
    # 현재 스택 리스트 변수에 저장되어 있는 데이터 갯수를 읽어와서 전역 변수에 저장
    count_my_stack_list = len(my_stack_list_p)
    # 데이터 저장 완료 메시지를 화면에 출력
    print("새로운 데이터를 스택 메모리에 저장함")
# 현재 스택 리스트 변수에 저장되어 있는 특정 데이터를 찾아주는 함수 만들기
# 매개 변수 : 스택 리스트 변수의 주소를 받는 매개 변수 : my_stack_list_p
# 사용자가 입력한 찾을 데이터를 받는 매개 변수 : find_data_p
# 함수의 결과는 사용자가 입력한 데이터를 찾은 경우에는 참(True)을 반환
# 데이터를 찾지 못한 경우에는 거짓(False)를 반환
def  find_func(my_stack_list_p, find_data_p):
    print("사용자가 원하는 데이터를 찾아주는 함수!!")
    print("find_func( ) 함수가 호출됨")
    result = find_data_p in my_stack_list_p
    if result == True:
        return True
    else:
        return False
# 현재 스택 리스트 변수에 저장되어 있는 특정 데이터를 삭제하는 함수 만들기
# -> del 함수를 사용 사용 방법) del  리스트변수이름[위치번호]
def  del_func(my_stack_list_p, del_data_p):
    # 데이터를 삭제하는 경우에는 전역 변수인 count_my_stack_list를 업데이트 해야 합니다!!
    global count_my_stack_list
    print("del_func() 함수가 호출됨")
    # 현재 스택 리스트 변수가 갖고 있는 데이터가 있는지를 검사
    if count_my_stack_list == 0:
        print("현재 스택 리스트 변수가 갖고 있는 데이터가 없습니다!!")
        return False
    else:
        # 먼저 삭제할 데이터가 현재 리스트 변수에 있는지를 검사하기
        # 위에서 만든 find_func( ) 함수를 호출해서 결과를 받아옵니다!!
        result = find_func(my_stack_list_p, del_data_p)
        if result == True:
            print("삭제할 데이터가 현재 스택 리스트 변수에 있습니다!!")
            # for 반복문을 작성해서 삭제하고자 하는 데이터의 위치 번호를 가져와서 임시 변수에 저장
            temp_index_del = -1
            for i in range(0, count_my_stack_list):
                if my_stack_list_p[i] == del_data_p:
                    print("삭제할 데이터의 위치 번호를 찾음")
                    temp_index_del = i
                    break
            print("for 반복문을 탈출!!")
            if temp_index_del != -1:
                print("del 함수를 호출해서 데이터를 삭제합니다!!")
                del my_stack_list_p[temp_index_del]
                # 다시 현재 스택 리스트 변수가 갖고 있는 데이터의 갯수를 읽어와서 전역 변수에 저장
                count_my_stack_list = len(my_stack_list_p)
                return True
            else:
                return False
        else:
            print("삭제할 데이터가 현재 스택 리스트 변수에 없습니다!!")
            return False
# 데이터 출력 함수 만들기
def  show_func(my_stack_list_p):
    global count_my_stack_list
    if count_my_stack_list == 0:
        print("현재 스택 리스트 변수가 갖고 있는 데이터가 하나도 없습니다!!")
    else:
        print("데이터 갯수는 ", count_my_stack_list, " 입니다!!")
        for i in range(0, count_my_stack_list):
            print(my_stack_list_p[i])
    print("함수 종료")

# 위에서 만든 함수들을 사용하는 메인 명령어들을 작성하기
while True :
    print("***스택 리스트 변수 사용 예제***")
    print("1. 데이터 입력")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 출력")
    print("5. 프로그램 종료")
    print("1~5 메뉴 번호를 하나만 입력하세요: ", end="")
    menu_no = int(input())
    if menu_no == 1:
        print("사용자가 메뉴 번호 1을 입력함!!")
        print("스택 메모리에 저장할 데이터를 입력하세요: ", end=" ")
        input_data = input()
        input_func(my_stack_list, input_data)
    elif menu_no == 2:
        print("사용자가 메뉴 번호 2를 입력함!!")
        print("검색할 데이터를 입력하세요: ", end=" ")
        find_data = input()
        result = find_func(my_stack_list, find_data)
        if result == True:
            print("사용자가 입력한 데이터가 스택 메모리에 존재!!")
        else:
            print("사용자가 입력한 데이터가 스택 메모리에 없음!!")
    elif menu_no == 3:
        print("사용자가 메뉴 번호 3을 입력함!!")
        print("삭제할 데이터를 입력하세요: ", end=" ")
        del_data = input()
        result = del_func(my_stack_list, del_data)
        if result == True:
            print("삭제 성공!!")
        else:
            print("삭제 실패!!")
    elif menu_no == 4:
        print("사용자가 메뉴 번호 4를 입력함!!")
        print("현재 스택 리스트 변수가 갖고 있는 모든 데이터들을 화면에 출력")
        show_func(my_stack_list)
    elif menu_no == 5:
        print("사용자가 메뉴 번호 5를 입력함!!")
        print("프로그램을 종료합니다!!")
        break
    else:
        print("메뉴에 없는 번호를 입력하셨습니다!!")
        # 사용자에게서 다시 메뉴 번호 입력을 요청하기
        while True:
            print("다시 메뉴 번호를 입력하세요: ", end=" ")
            menu_no = int(input())
            if menu_no >= 1 and menu_no <= 5:
                break
        print("while 반복문을 탈출")
        if menu_no == 5:
            break










































































