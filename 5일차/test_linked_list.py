"""
연결 리스트 예제를 작성하기
"""
# 데이터와 주소를 보관하는 노드 클래스를 정의하기
class MyNodeClass:
    # 초기화 함수 만들기 : 멤버 변수를 생성해서 시작값을 지정
    def __init__(self, data_p, next_p = None):
        print("초기화 함수가 실행되었습니다!!")
        print("외부로부터 받은 데이터를 멤버 변수에 저장하기")
        self.data = data_p
        print("주소를 멤버 변수에 저장하기")
        self.next = next_p
        print("저장 완료")
        print("저장된 데이터는 ", self.data)

# 위에서 만든 노드 클래스를 멤버로 사용하는 새로운 클래스 정의하기
class MyLinkedListClass:
    # 초기화 함수
    def __init__(self):
        print("헤드 포인터 변수를 생성해서 None 값으로 초기화")
        self.head_ptr = None
        print("초기화 완료")

    # 새로운 노드를 메모리에 만들고 반환하는 함수
    # 함수 이름 : create_new_node
    def  create_new_node(self):
        print("새로운 노드를 메모리에 생성해주는 함수")
        print("새로운 노드에 저장할 데이터를 입력하세요: ", end=" ")
        input_data = int(input())
        print("사용자가 입력한 데이터는 ", input_data)
        # 새로운 객체를 메모리에 생성 : __init__( ) 함수를 호출하면서 사용자가 입력한 데이터를 전달
        new_object = MyNodeClass(input_data)
        print("새로운 객체를 생성하였습니다!!")
        return new_object

    # 위에서 만든 create_new_node( ) 함수를 호출해서 메모리에 데이터를 보관할 수 있는
    # 노드 객체를 생성하기 + 기본 값으로 무조건 다음에 연결될 노드의 주소는 None
    # 함수 이름은 insert_new_node
    def insert_new_node(self):
        print("새로운 노드를 생성하고 헤드 포인터 변수에 연결하는 함수")
        print("create_new_node( ) 함수를 호출해서 새로운 노드 객체를 만들기")
        new_object = self.create_new_node()
        if new_object is None:
            print("새로운 노드 객체 생성 실패")
            return None
        else:
            print("새로운 노드 객체 생성 성공")
            print("새로 만든 노드 객체를 헤드 포인터 변수와 연결하기")
            if self.head_ptr is None:
                print("현재 헤드 포인터 변수에 연결된 노드 객체가 없는 상태!!")
                print("방금 만든 노드 객체가 첫 번째 노드가 됩니다!!")
                self.head_ptr = new_object
                print("새로 만든 노드 객체의 주소를 헤드 포인터 변수에 할당")
            else:
                print("현재 헤드 포인터 변수와 연결된 노드 객체가 있는 상태!!")
                print("헤드 포인터 변수와 연결되어 있는 많은 노드 객체 중에서 마지막 노드 찾기")
                # 현재 헤드 포인터 변수가 갖고 있던 첫 번째 노드의 주소를 임시로 보관하기
                current_node_ptr = self.head_ptr
                """
                while 반복문을 사용해서 마지막 번째 노드의 주소를 찾기
                """
                while current_node_ptr.next is not None:
                    print("현재 특정 노드의 주소로 이동 중에 있습니다!!")
                    print("현재 방문(접근)한 노드가 갖고 있는 데이터는 ", current_node_ptr.data)
                    # 두 번째 이후의 노드 주소로 이동하기
                    current_node_ptr = current_node_ptr.next
                print("마지막 노드의 주소를 찾았습니다!!")
                print("마지막 노드의 다음 노드로 새로운 노드를 연결하기!!")
                current_node_ptr.next = new_object
                print("연결 완료")
            return self.head_ptr

    # 새로운 함수를 정의하기 : 기능은 모든 노드들을 방문하여 데이터를 화면에 출력
    def show_all_nodes(self):
        print("모든 노드들을 방문한 후에 데이터들을 화면에 출력하기")
        current_node_ptr = self.head_ptr
        if current_node_ptr is None:
            print("현재 노드가 없습니다!!")
        else:
            print("현재 노드가 존재합니다!!")
            while current_node_ptr is not None:
                print("특정 노드의 주소로 이동했습니다!!")
                print("현재 방문한 노드가 갖고 있는 데이터는 ", current_node_ptr.data)
                print("다음 노드의 주소로 이동하기")
                current_node_ptr = current_node_ptr.next
            print("출력 완료!!")

    # 찾기 함수를 새로 만들기
    def find_node(self, input_find_data_p):
        print("데이터 찾기 함수가 호출됨")
        current_node_ptr = self.head_ptr
        if current_node_ptr is None:
            print("현재 연결 리스트에 보관되어 있는 데이터가 하나도 없습니다!!")
            return None
        else:
            print("사용자가 입력한 데이터와 노드가 갖고 있는 데이터를 차례대로 하나씩 비교!!")
            # 데이터 찾기 결과를 보관할 변수
            result_find = False
            while current_node_ptr is not None:
                print("특정 노드의 주소로 이동했습니다!!")
                if current_node_ptr.data == input_find_data_p:
                    result_find = True
                    break
                print("다음 노드의 주소로 이동하기!!")
                current_node_ptr = current_node_ptr.next
            if result_find is True:
                print(input_find_data_p, " 데이터를 찾았습니다!!")
            else:
                print(input_find_data_p, " 데이터를 찾지 못했습니다!!")
            return self.head_ptr

    # 현재 헤드 포인터 변수와 연결되어 있는 모든 노드들을 방문한 후에 노드를 삭제하는 함수
    def delete_all_nodes(self):
        print("모든 노드들을 삭제하는 함수가 호출됨")
        current_node_ptr = self.head_ptr
        if current_node_ptr is None:
            print("삭제할 노드가 하나도 없습니다!!")
        else:
            print("노드들을 방문한 다음에 특정 노드 하나씩 삭제하기")
            # 첫 번째 노드 먼저 삭제 예정
            delete_node_ptr = current_node_ptr
            while current_node_ptr is not None:
                print("삭제할 노드가 갖고 있는 데이터는 ", current_node_ptr.data)
                delete_node_ptr = current_node_ptr
                print("다음 노드의 주소로 이동합니다!!")
                current_node_ptr = current_node_ptr.next
                delete_node_ptr = None
                print("삭제 완료!!")
            print("모든 노드들을 삭제했습니다!!")
            self.head_ptr = None

# 위에서 만든 MyLinkedListClass 클래스를 사용하기
linked_list_object = MyLinkedListClass()
# insert_new_node( ) 함수를 호출하기
result_insert_new_node = linked_list_object.insert_new_node()
if result_insert_new_node is None:
    print("insert_new_node() 함수 실행 실패")
else:
    print("insert_new_node() 함수 실행 성공")

# insert_new_node( ) 함수를 호출하기
result_insert_new_node = linked_list_object.insert_new_node()
if result_insert_new_node is None:
    print("insert_new_node() 함수 실행 실패")
else:
    print("insert_new_node() 함수 실행 성공")

# MyLinkedListClass 클래스에서 새로 만든 find_node( ) 함수를 호출
# -> 사용자로부터 찾을 데이터를 입력 받아야 합니다!!
print("찾고자 하는 데이터를 정수로 입력하세요: ", end=" ")
input_data = int(input())
result_find_node = linked_list_object.find_node(input_data)
if result_find_node is None:
    print("find_node() 함수 실행 실패")
else:
    print("find_node() 함수 실행 성공")

# 방금 MyLinkedListClass 클래스에서 만든 delete_all_nodes( ) 함수를 호출하기
linked_list_object.delete_all_nodes()
print("delete_all_nodes() 함수 실행 완료!!")

# self + 점(.) + 변수이름 : 클래스 안에 있는 모든 함수에서 사용 가능한 전역 변수
# data_p, next_p : 지역 변수 : __init__( ) 함수에서만 사용 가능한 변수
# 위에서 만든 노드 클래스를 사용해서 변수를 선언(객체를 생성)
object1 = MyNodeClass( 1 ) # 1은 data_p 매개 변수에 전달됩니다.
object2 = MyNodeClass( 2 )
object3 = MyNodeClass( 3 )
# 위처럼 변수를 생성하면 next_p 매개 변수에는 None 기본 값을 사용
object4 = MyNodeClass( 4 , object1)
# 위처럼 명령어를 작성하고 실행하면 next_p 매개변수에는 object1 주소가 저장
object5 = MyNodeClass(5, None)

list1 = ["김길동","나길동","다길동","라길동","마길동"]
# "김길동" : list1[0]
# "나길동" : list1[1]
# -> 시작 주소(Base Address)가 같은 리스트 변수
# 주소가 규칙을 갖고 있습니다!!
# 연속적인 메모리 공간(배열)

"""
연결 리스트 : 
  하나의 노드 메모리 공간을 만들고  
  또 하나의 노드 메모리 공간을 만들고
  또 하나의 노드 메모리 공간을 만들고
  
  + 헤드 포인터 변수가 따로 필요합니다!! : 첫 번째 노드 메모리 공간의 주소를 보관할 변수
     -> 무조건 첫 번째 데이터가 저장되어 있는 노드의 주소를 보관
     
  head_ptr -> 첫 번째 노드의 주소 -> 두 번째 노드의 주소 -> 세 번째 노드의 주소 -> ... -> None
  
  
"""





























































