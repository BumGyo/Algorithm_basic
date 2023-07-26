import random

def insertionSort(list_p):
    len_list_p = len(list_p)
    if len_list_p == 0:
        return False

    for i in range(1, len_list_p):
        value = list_p[i]
        j = i
        while j > 0 and list_p[j-1] > value:
            list_p[j] = list_p[j-1]
            j -= 1
        list_p[j] = value
    return True

list1 = []
for i in range(1, 100):
    rand_num = random.randint(1, 300)
    print("rand_num: ", rand_num)
    list1.append(rand_num)

for i, val in enumerate(list1):
    print(val)

result = insertionSort(list1)
if result is True:
    print("insertionSort(list1) 함수 실행 성공")
else:
    print("insertionSort(list1) 함수 실행 실패")

print("***정렬 완료***")

for i, val in enumerate(list1):
    print(val)
