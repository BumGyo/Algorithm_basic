# 여러 명 학생의 국어 점수 중에서 최고 점수의 리스트 위치 번호를 화면에 출력하는 예제
def getIndexMaxScore(kor_list):
    # 첫 번째 학생의 국어 점수를 최고 점수로 가정하기
    max_kor_score = kor_list[0]
    # 첫 번째 학생의 국어 점수의 위치 번호를 변수에 저장하기
    index_max_kor_score = 0
    # while 반복문을 사용해서 기준 점수와 비교 점수들을 비교한 다음에
    # 최고 점수의 리스트 변수 내의 위치 번호를 index_max_kor_score 변수에 저장하기
    # 비교할 국어 점수의 위치 번호
    j = index_max_kor_score + 1
    while j <= (len(kor_list)-1):
        if max_kor_score < kor_list[j]:
            index_max_kor_score = j
            max_kor_score = kor_list[j]
        j += 1

    return index_max_kor_score

# 총 5명 학생의 국어 점수들을 보관할 리스트 변수를 선언
kor_score_list = [70, 100, 50, 60, 90]
# 위에서 만든 함수를 호출해서 최고 국어 점수의 위치 번호를 얻어오기
index_max_score = getIndexMaxScore(kor_score_list)
print("최고 국어 점수를 얻은 학생의 리스트 변수 위치 번호는 ", index_max_score)