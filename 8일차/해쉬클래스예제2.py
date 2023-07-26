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

# 방금 만든 LinearMap 클래스를 사용하는 클래스
class BetterMap:
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


better_map = BetterMap()
better_map.add(1, 2)
better_map.add(1, 3)
result = better_map.get(1)
print("result: ", result)