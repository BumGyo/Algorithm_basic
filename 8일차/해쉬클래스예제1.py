# 동일 해쉬 주소에 여러 데이터가 있을 때(심화)
class LinearMap:
    def __init__(self):
        self.items = list()

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        data = list()
        for key, val in self.items:
            if key == k:
                data.append(val)
        return data


linear_map = LinearMap()
linear_map.add(1, 2)
linear_map.add(1, 3)
result = linear_map.get(1)
print("result: ", result)