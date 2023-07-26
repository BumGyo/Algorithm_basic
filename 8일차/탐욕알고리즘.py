"""
문제 : 지불해야 하는 값이 362원 일 때
1원 50원 100원 짜리 동전으로 동전의 수가 가장 적게 지불하는 예제.

동전 지불 문제는 그리디 알고리즘을 사용해서 풀 수 있는
아주 간단하고 직관적인 예제 중 하나
"""

def min_calc(value, coin):
    a = []
    for i in coin:
        a.append([value - i, i])
    res = a[0]
    for i in a:
        if res[0] > i[0] and i[0] > 0:
            res = i
    return res


coin = [1, 50, 100]
value = [362, 0]
dic = {}
for i in coin:
    dic[i] = 0

while True:
    value = min_calc(value[0], coin)
    if value[0] < 0:
        break
    else:
        dic[value[1]] += 1

print(dic)
