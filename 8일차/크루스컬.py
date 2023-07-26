"""
크루스컬 알고리즘 :
최소 신장 트리(MST) 를 만드는 방법중 하나
모든 정점을 연결하는 간선들의 가중치 합의 최소가 되는 트리
"""
"""
아래 gif animation도 있습니다.
https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/MST_kruskal_en.gif/200px-MST_kruskal_en.gif
"""

"""
순서는 아래와 같습니다.
1. 모든 간선을 가중치에 따라 오름차순으로 정렬
2. 가중치가 낮은 간선부터 선택하면서 트리를 만듭니다. 
만약 사이클이 존재하면 다음 가중치가 낮은 간선을 선택
3. N개의 정점이 있다고 가정할때 N-1개의 간선이 선택될때까지 2를 반복
   (정점의 갯수는 간선-1 이기 때문)
"""

"""
모든 정점을 독립적인 집합으로 만든다.

모든 간선을 비용을 기준으로 정렬하고,
비용이 작은 간선부터 양 끝의 두 정점을 비교한다.

두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.
"""

parent = {}
rank = {}


# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0


# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = []

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return mst


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]
}

print(kruskal(graph))
