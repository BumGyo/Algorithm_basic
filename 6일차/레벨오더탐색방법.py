    # 레벨 오더 방법으로 트리를 탐색하는 함수
    # MyTreeClass 클래스에 넣고 테스트 해주세요
    def level_order(self, root_node_p):
	# 리스트 자료 구조를 사용 : 루트 노드를 보관
        # 1. 리스트 변수 생성 : 데이터는 없는 상태
        q = []
        # append( ) 함수를 호출해서 현재 데이터에 새로운
        # 새로운 데이터를 추가
        q.append(root_node_p)
	# len(q) : 리스트 변수에 보관되어 있는 데이터 갯수
        # len( ) : 내장 함수
        while len(q) != 0:
            # pop( ) 내장 함수를 호출해서
            # 리스트 변수에 보관되어 있는 여러 개의
            # 데이터 중에서 첫 번째 데이터를 꺼내오고 삭제
            t = q.pop(0)
	    # str( ) 내장 함수를 호출해서 문자로 변환한 후에
            # 화면에 출력
            print(str(t.data), ' ', end='')
            if t.left_child is not None:
                q.append(t.left_child)
            if t.right_child is not None:
                q.append(t.right_child)

