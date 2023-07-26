def binary_search(key_p, data_p):

    # 무조건 정렬
    data_p.sort()

    start = 0

    len_data = len(data_p)

    if len_data == 0:
        return False

    end = len_data - 1

    while start <= end:
        mid = (start + end) // 2

        if data_p[mid] == key_p:
            return mid # 함수를 끝내버린다.
        elif data_p[mid] < key_p:
            start = mid + 1
        else:
            end = mid -1

    return False


li = [30, 100, 80, 25, 9, 45]
key = 9
idx = binary_search(key, li)

if idx:
    print(li[idx])
else:
    print("찾으시는 ", key, " 이 없습니다")


# data는 오름차순으로 정렬된 리스트
def binary_search_recursion
    (key_p, start_p, end_p, data_p):

    if start_p > end_p:
        return False

    mid = (start_p + end_p) // 2

    if data_p[mid] == key_p:
        return mid
    elif data_p[mid] > key_p:
        end_p = mid - 1
    else:
        start_p = mid + 1

    return 
      binary_search_recursion(
       key_p, start_p, end_p, data_p)


li = [30, 100, 80, 6, 9, 45]
target = 6
idx = binary_search_recursion(target, 0, len(li)-1, li)

print(li)
print(idx)