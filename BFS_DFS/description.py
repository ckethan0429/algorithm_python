N, M, V = map(int, input().split())
#print(N,M,V)

matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    # 인접행렬 만들기 
    link = list(map(int,input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

# bfs와 다르게 row와 foot_prints를 매개변수로 받는이유는
# 재귀함수를 이용하여 다시 dfs함수를 호출하기 떄문
def dfs(current_node, row, foot_prints):
    # foot_prints에 현재 노드를 추가시켜준다.
    foot_prints += [current_node]
    # 매트릭스에 현재노드에 링크되어있는 개수만큼 반복해서
    for search_node in range(len(row[current_node])):
        # 만약 연결이 되어있고 foot_prints에 없다면 
        # 재귀함수를 통해 search_node를 현재노드로 하여 다시 dfs를 호출한다.
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

def bfs(start):
    # queue에 처음 시작 노드를 넣어주고
    queue = [start]
    foot_prints = [start]
    # queue가 없어질때까지 반복함
    while queue:
        # 큐에서 팝하고
        current_node = queue.pop(0)
        # 매트릭스에 현재노드에 링크되어있는 개수만큼 반복해서
        for search_node in range(len(matrix[current_node])):
            # search_node를 foot_prints에 추가하고 queue에 집어넣는다. 
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints

print(*dfs(V, matrix, []))
print(*bfs(V))