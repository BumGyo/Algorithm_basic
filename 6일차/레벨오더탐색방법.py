    # ���� ���� ������� Ʈ���� Ž���ϴ� �Լ�
    # MyTreeClass Ŭ������ �ְ� �׽�Ʈ ���ּ���
    def level_order(self, root_node_p):
	# ����Ʈ �ڷ� ������ ��� : ��Ʈ ��带 ����
        # 1. ����Ʈ ���� ���� : �����ʹ� ���� ����
        q = []
        # append( ) �Լ��� ȣ���ؼ� ���� �����Ϳ� ���ο�
        # ���ο� �����͸� �߰�
        q.append(root_node_p)
	# len(q) : ����Ʈ ������ �����Ǿ� �ִ� ������ ����
        # len( ) : ���� �Լ�
        while len(q) != 0:
            # pop( ) ���� �Լ��� ȣ���ؼ�
            # ����Ʈ ������ �����Ǿ� �ִ� ���� ����
            # ������ �߿��� ù ��° �����͸� �������� ����
            t = q.pop(0)
	    # str( ) ���� �Լ��� ȣ���ؼ� ���ڷ� ��ȯ�� �Ŀ�
            # ȭ�鿡 ���
            print(str(t.data), ' ', end='')
            if t.left_child is not None:
                q.append(t.left_child)
            if t.right_child is not None:
                q.append(t.right_child)

