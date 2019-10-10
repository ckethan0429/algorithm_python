# 노드수 받기
N = int(input())
# 인접 행렬 생성 (노드수 + 1) * (노드수 +1)
matrix = [[0] * (N+1) for _ in range(N+1)]
# 엣지수 받기
E_num = int(input())

# 엣지만큼 인접행렬 최신화
for _ in range(E_num):
    link = list(map(int,input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

# bfs와 다르게 row와 foot_prints를 매개변수로 받는이유는
# 재귀함수를 이용하여 다시 dfs함수를 호출하기 떄문
def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


print(len(dfs(1, matrix, []))-1)