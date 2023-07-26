# 순차 검색 알고리즘1
def sequential_search(list_p, key):
    i = 0
    while i < len(list_p):
        if list_p[i] == key:
            return i
        i += 1
    return -1

# 순차 검색 알고리즘2
def sequential_search2(list_p, key):
	for idx, val in enumerate(list_p):
		if val == key:
			return idx
	return -1