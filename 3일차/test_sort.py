# 선택 정렬 알고리즘을 작성하고 실행하기

# 1. 난수를 사용해서 여러 개의 임의의 숫자를 만든 다음에 리스트 변수에 저장하겠습니다!!
# 난수(Random) : 확정되지 않은 임의의 수 예) 주사위 번호, 로또 번호, 가위/바위/보 ...
# 프로그램이 실행된 후에 결정
# -> 임의의 수를 만들 수 있는 제일 빠른 방법 : random 모듈을 사용
#  모듈 : module : 외부 파일 : random.py
# -> import 명령어를 작성해서 random.py 파일을 현재 파일 안으로 수입(연결: Link)
import  random

# 2. 리스트 변수를 선언
list1 = []
# -> 이름 : list -> 클래스 이름이기 때문에 실행 오류 발생

# 3. for 반복문을 사용해서 여러 개의 난수들을 만든 다음에
# 리스트 변수에 저장하기
for i in range(1, 101):
    print("현재 변수 i 값은 ", i)
    # randint( ) : 난수를 만들어 주는 함수
    rand_value = random.randint(1, 200)
    # append( ) 함수를 호출해서 새로 만든 난수를 리스트 변수에 저장
    list1.append(rand_value)

# 4. 현재 리스트 변수가 갖고 있는 난수들을 읽어와서 화면에 출력하는 반복문을 작성
len_list1 = len(list1)
if len_list1 == 0:
    print("현재 리스트 변수에 보관되어 있는 난수는 하나도 없습니다!!")
else:
    print("현재 리스트 변수가 갖고 있는 난수의 갯수는 ", len_list1, " 입니다!!")
    for i  in range(len_list1):
        print("현재 리스트 변수가 갖고 있는 난수를 화면에 출력")
        print("난수의 위치 번호는 ",i, "이고, 난수는 ", list1[i])

    # 리스트 변수가 갖고 있는 sort( ) 함수를 호출하기
    list1.sort()

    print("***정렬(Sorting) 기능을 수행하였습니다!!***")

    # 정렬된 리스트 변수의 모든 난수 값들을 다시 읽어와서 화면에 출력
    for i in range(len_list1):
        print("난수의 위치는 ", i, " 이고, 난수는 ", list1[i])






























