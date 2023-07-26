#리스트 자료 구조 사용
#총 5명 학생의 이름을 리스트 변수에 저장하기
student_name_list = ["가","나","다","라","마"]
print("첫 번째 학생의 이름은 ", student_name_list[0])
len_student = len(student_name_list)
print("학생 수는", len_student)
# append() 함수를 사용하기 : 새로운 데이터를 마지막 데이터 바로 뒤에 추가
# 1) 사용방법 : 리스트변수이름 + 점 + append("새로운 학생의 이름")
# 점(.) -> 참조(reference) -> 리스트 변수는 데이터들의 주소를 갖고 있는 상태에서 점 연산자를 만나면 자동으로 append()함수의 주소로 이동
student_name_list.append("이순신")
len_student = len(student_name_list)
print("현재 학생 수는", len_student)
last_student_name = student_name_list[len_student - 1]
print("가장 마지막에 추가된 학생이름은", last_student_name)
index_student = 0
while index_student <= (len_student - 1):
    print(student_name_list[index_student])
    index_student += 1

