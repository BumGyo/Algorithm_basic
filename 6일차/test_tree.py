"""
트리 중에서도 이진 트리 : 자식 노드의 갯수가 최대 2개인 트리
"""
# 노드 클래스 정의하기
class MyTreeNodeClass:
    # 초기화 함수 정의하기
    def __init__(self, data_p, left_child_p = None, right_child_p = None):
        print("새로운 트리 노드 객체를 메모리에 만듭니다!!")
        self.data = data_p
        self.left_child = left_child_p
        self.right_child = right_child_p
        print("모든 인스턴스 변수에 처음 값을 지정했습니다!!")
        print("데이터의 처음 값은 ", self.data)

# 이진 검색 트리 클래스를 새로 정의하기
class MyTreeClass:
    # 초기화 함수
    def __init__(self):
        print("__init__() 함수가 호출됨")
        self.root_ptr = None
        print("루트 노드의 초기값을 None으로 지정함")

    # 무조건 하나의 새로운 트리 노드 객체를 만들고 반환하는 함수
    def  create_new_node(self, value_p):
        print("create_new_node() 함수가 호출됨")
        # 새로운 트리 노드 객체를 생성하기
        new_node = MyTreeNodeClass(value_p)
        # return 명령어를 사용해서 호출한 함수로 새로 만든 노드 객체를 반환
        return new_node

    # 위에서 만든 create_new_node( ) 함수를 호출하는 insert_new_node( ) 함수를 정의
    def insert_new_node(self, value_p):
        print("insert_new_node() 함수가 호출됨")
        # 위에서 만든 create_new_node( ) 함수를 호출
        new_node = self.create_new_node(value_p)
        # create_new_node( ) 함수의 실행 결과를 검사하기
        if new_node is None:
            print("새로운 트리 노드 만들기 실패!!")
        else:
            print("새로운 트리 노드 만들기 성공!!")
            # 현재 루트 노드에 연결되어 있는 노드가 있는지를 검사하기
            if self.root_ptr is None:
                print("현재 루트 노드에 연결되어 있는 노드가 없습니다!!")
                self.root_ptr = new_node
                print("새로 만든 노드를 첫 번째 노드로 지정!! 루트 노드로 지정!!")
            else:
                print("현재 루트 노드에 연결되어 있는 노드가 있습니다!!")
                # _insert_new_node(self.root_ptr) : 왼쪽 또는 오른쪽 자식 노드에
                # 서브 트리의 루트 노드
                # _insert_new_node( ) 함수의 최종값을 가져와서 루트 노드에 저장
                self.root_ptr = self._insert_new_node(self.root_ptr, new_node)

    # 재귀호출 방법을 사용한 새로운 노드를 현재 트리 자료 구조에 추가해주는 함수를 정의
    # 1. 매개 변수 : self, node 새로 만든 노드의 주소를 갖게될 변수
    def  _insert_new_node(self, node_p, new_node_p):
        print("새로 만든 _insert_new_node() 함수가 호출됨!!")
        if node_p is not None:
            print("현재 트리 자료 구조에 추가될 노드가 갖고 있는 데이터는 ", node_p.data)

        """
        재귀호출 방법을 사용하기
        1. 종료 조건을 만들기 : node_p 매개 변수가 None 값을 받는 경우에는 현재
           함수를 종료할 수 있도록 return 명령어를 작성
        """
        if node_p is None:
            print("현재 함수를 탈출하기!!")
            # node_p 변수에 새로운 노드의 주소를 저장
            # node_p 변수는 루트 노드로 시작해서 왼쪽 자식 노드 또는 오른쪽 자식 노드로 이동
            node_p = new_node_p
            # node_p 변수가 갖고 있는 값을 반환 : self.root_ptr 변수에서 받는 값
            return node_p
        else:
            print("외부로부터 받은 노드의 주소는 None이 아님!!")
            """
            노드가 갖고 있는 데이터와 현재 루트 노드가 갖고 있는 데이터를 비교하기
            -> 작은 경우에는 현재 트리에서 왼쪽 자식 노드에 새로운 노드가 추가될 수 있도록 해야 함
            -> 큰 경우에는 현재 트리에서 오른쪽 자식 노드에 새로운 노드가 추가될 수 있도록 해야 함
            """
            if node_p.data > new_node_p.data:
                print("새로운 노드가 갖고 있는 데이터가 더 작습니다!!")
                print("새로운 노드는 현재 트리에서 왼쪽 자식 노드에 추가되어야 합니다!!")
                node_p.left_child = self._insert_new_node(node_p.left_child, new_node_p)
                return node_p
            elif node_p.data < new_node_p.data:
                print("새로운 노드가 갖고 있는 데이터가 더 큽니다!!")
                print("새로운 노드는 현재 트리에서 오른쪽 자식 노드에 추가되어야 합니다!!")
                node_p.right_child = self._insert_new_node(node_p.right_child, new_node_p)
                return node_p


    # 중위 탐색 방법을 사용해서 현재 트리 자료 구조에 연결되어 있는 모든 노드들을 방문하기
    def in_order_trav(self, node_p):
        print("in_order_trav() 함수가 호출됨")
        if node_p is not None:
            print("현재 탐색할 노드가 남아있습니다!!")
            self.in_order_trav(node_p.left_child)
            print("현재 방문한 노드가 갖고 있는 데이터는 ", node_p.data)
            self.in_order_trav(node_p.right_child)

    # 전위 탐색 방법을 사용해서 트리 자료 구조 방문하기
    def pre_order_trav(self, node_p):
        print("pre_order_trav() 함수가 호출됨")
        if node_p is not None:
            print("현재 탐색할 노드가 남아있습니다!!")
            print("현재 방문한 노드가 갖고 있는 데이터는 ", node_p.data)
            self.pre_order_trav(node_p.left_child)
            self.pre_order_trav(node_p.right_child)

    # 후위 탐색 방법을 사용해서 트리 자료 구조 방문하기
    def post_order_trav(self, node_p):
        print("post_order_trav() 함수가 호출됨")
        if node_p is not None:
            print("현재 탐색할 노드가 남아 있습니다!!")
            # 왼쪽 자식 노드 먼저 방문하기
            self.post_order_trav(node_p.left_child)
            # 오른쪽 자식 노드 방문하기
            self.post_order_trav(node_p.right_child)
            # 화면에 데이터를 출력 : 루트 노드 방문
            print("현재 방문한 노드가 갖고 있는 데이터는 ", node_p.data)
    ####################################################################
    # MyTreeClass 클래스 안 입니다!!
    # 레벨 오더 방법으로 트리를 탐색하는 함수
    def level_order(self, root_node_p):
        q = []
        q.append(root_node_p)

        while len(q) != 0:
            t = q.pop(0)
            print(str(t.data), ' ', end='')
            if t.left_child is not None:
                q.append(t.left_child)
            if t.right_child is not None:
                q.append(t.right_child)


# 위에서 만든 노드 클래스를 사용하는 명령어를 입력합니다.
#first_tree_node = MyTreeNodeClass(1)
#second_tree_node = MyTreeNodeClass(2)
#third_tree_node = MyTreeNodeClass(3)

# 사용자로부터 트리 노드에 저장할 데이터를 입력 받습니다!!
# 1) 새로 만든 MyTreeClass 클래스를 사용하기
my_tree_object = MyTreeClass()
# -> 새로운 변수 my_tree_object를 선언 : 이유는 create_new_node( ) 함수 insert_new_node() 함수를
# -> 사용하기 위함 클래스 안에 들어 있는 멤버 함수이기 때문에 직접 사용은 불가능
print("트리 노드에 저장할 데이터를 정수로 입력하세요: ", end=" ")
input_data = int(input())
# insert_new_node( ) 함수를 호출
# -> 접근(호출) 방법은 변수이름 + 점(.) 연산자 + 함수이름( 매개 변수에 전달할 데이터 )
my_tree_object.insert_new_node(input_data)
# 데이터는 서로 다른게 입력!!
#  두 번째로 insert_new_node( ) 함수를 호출
print("트리 노드에 저장할 데이터를 정수로 입력하세요: ", end=" ")
input_data = int(input())
my_tree_object.insert_new_node(input_data)
# 세 번째로 insert_new_node() 함수를 호출
print("트리 노드에 저장할 데이터를 정수로 입력하세요: ", end=" ")
input_data = int(input())
my_tree_object.insert_new_node(input_data)

# 인오더 방법으로 현재 트리에 연결되어 있는 모드 노드들을 방문 : 왼쪽 노드 -> 루트 -> 오른쪽 노드
# 데이터 입력이 중요 : 총 3번의 데이터 입력에서 첫 번째 데이터는 2(루트 노드가 보관)
# 두 번째 데이터는 1(왼쪽 자식 노드), 세 번째 데이터는 3(오른쪽 자식 노드)
# my_tree_object.in_order_trav(my_tree_object.root_ptr)

# 프리 오더 방법으로 현재 트리에 연결되어 있는 모든 노드들을 방문 :
# 먼저 루트 -> 왼쪽 자식 노드 -> 오른쪽 자식 노드
# my_tree_object.pre_order_trav(my_tree_object.root_ptr)

# 포스트 오더 방법으로 현재 트리에 연결되어 있는 모든 노드들을 방문:
# 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 루트 노드
#my_tree_object.post_order_trav(my_tree_object.root_ptr)

# 레벨 오더 방법으로 트리 자료 구조 탐색하기
my_tree_object.level_order(my_tree_object.root_ptr)








