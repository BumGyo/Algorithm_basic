# 큐(Queue) 메모리를 사용하는 예제를 작성
my_list1 = []
# append( ) 함수를 호출해서 정수 1, 2, 3을 리스트 변수에 저장하기
my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
# pop( ) 함수를 호출해서 맨 앞에 있는 정수 1부터 꺼내오기
value1 = my_list1.pop(0)
print("큐 메모리에서 꺼내온 첫 번째 정수는 ", value1)
# 위에서 삭제한 정수 1이 리스트 변수 안에 있는지를 검사하기
result = 1 in my_list1
if result == True:
    print("정수 1이 리스트 변수에 남아 있음")
else:
    print("정수 1이 리스트 변수에 없음")
# 리스트 변수가 갖고 있는 모든 데이터들을 삭제하기 위해서는 clear( ) 함수를 호출
# -> 리스트변수이름.clear( )
print("현재 리스트 변수가 갖고 있는 모든 값들을 삭제하기!!")
my_list1.clear()
len_my_list1 = len(my_list1)
if len_my_list1 == 0:
    print("현재 리스트 변수에는 값이 하나도 없음")
else:
    print("현재 리스트 변수에는 값이 ", len_my_list1, " 개 있음")