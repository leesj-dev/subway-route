from collections import deque
from station_line import lines

# 전처리
line_list = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "경강선", "경의·중앙선", "경춘선", "공항철도", "서해선", "수인·분당선", "신분당선", "김포 도시철도", "신림선", "용인 경전철", "우이신설선", "의정부 경전철", "인천 1호선", "인천 2호선"]
stations = {k: [] for k in line_list}
for k, v in lines.items():
    for item in v:
        stations[item].append(k)

# BFS 탐색
def bfs(START):
    global lines, line_list  # 전역변수화
    visit_station = {k: -1 for k in lines.keys()}  # 각 역마다 총 거친 노선 수
    visit_route = {k: False for k in line_list}  # 그 호선을 지나간 적이 있는지
    visit_station[START] = 0
    q = deque()  # popleft (0번째 item을 제거)하므로 속도를 위해 deque를 사용
    for line in lines[START]:
        q.append((START, line))
        visit_route[line] = True

    while q:  # do while q is not empty
        next_station, next_line = q.popleft()
        for adj_node in stations[next_line]:
            if visit_station[adj_node] != -1:
                continue
            visit_station[adj_node] = visit_station[next_station] + 1
            for connected_line in lines[adj_node]:
                if visit_route[connected_line]:
                    continue
                q.append((adj_node, connected_line))
    del visit_station[START]  # 시작역과 종착역이 같은 경우는 제거
    return visit_station

# make results
result = {k: set() for k in range(10)}  # 10은 임의로 잡은 것
for station in lines.keys():
    for k, v in bfs(station).items():
        if (station, k) not in result[v]:  # (k, station)와 (station, k) 중복 방지
            result[v].add((k, station))

# write to file
with open("result.txt", "w") as w:
    w.write(str(result))

