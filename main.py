from collections import deque, defaultdict
from station_line import lines
# import time
# start_time = time.time()

# 전처리
line_list = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "경강선", "경의·중앙선", "경춘선", "공항철도", "서해선", "수인·분당선", "신분당선", "김포 도시철도", "신림선", "용인 경전철", "우이신설선", "의정부 경전철", "인천 1호선", "인천 2호선", "GTX-A"]
# line_list_new = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "경강선", "경의·중앙선", "경춘선", "공항철도", "서해선", "수인·분당선", "신분당선", "김포 도시철도", "신림선", "용인 경전철", "우이신설선", "의정부 경전철", "인천 1호선", "인천 2호선", "동북선", "신안산선", "GTX-A", "GTX-B", "GTX-C", "인천공항자기부상철도"]
stations = {k: [] for k in line_list}
for k, v in lines.items():
    for item in v:
        stations[item].append(k)

# BFS 탐색
def bfs(START):
    global lines, line_list  # 전역변수화
    visit_station = {k: -1 for k in lines.keys()}  # 각 역마다 총 거친 노선 수
    visit_line = {k: False for k in line_list}  # 그 호선을 지나간 적이 있는지
    visit_station[START] = 0
    q = deque()  # popleft (0번째 item을 제거)하므로 속도를 위해 deque를 사용
    for line in lines[START]:
        q.append((START, line))

    while q:  # do while q is not empty
        next_station, next_line = q.popleft()
        visit_line[next_line] = True
        for adj_node in stations[next_line]:
            if visit_station[adj_node] != -1:
                continue
            visit_station[adj_node] = visit_station[next_station] + 1
            for connected_line in lines[adj_node]:
                if visit_line[connected_line]:
                    continue
                q.append((adj_node, connected_line))
    del visit_station[START]  # 시작역과 종착역이 같은 경우는 제거
    return visit_station

# make results
result = defaultdict(set)
for station in lines.keys():
    for k, v in bfs(station).items():
        if (station, k) not in result[v]:  # (k, station)와 (station, k) 중복 방지
            result[v].add((k, station))

# write to file
with open("result.txt", "w") as f:
    x = []
    for k, v in result.items():
        y = [str(item).replace("'", "") for item in v]
        x.append(f"[{k}개 노선을 거치는 경우의 수]\n{', '.join(y)}")
    f.write("\n\n".join(x))
    # 한줄로 나타내면 아래와 같음.
    # f.write("\n\n".join([f'[{k}개 노선을 거치는 경우의 수]\n' + ', '.join([str(item).replace("'", "") for item in v]) for k, v in result.items()]))

# statistics
a, b, c, d = len(result[1]), len(result[2]), len(result[3]), len(result[4])
station_cnt = len(lines)
combinations = station_cnt * (station_cnt - 1) // 2
print(f"1개 노선: {a}가지\n2개 노선: {b}가지\n3개 노선: {c}가지\n4개 노선: {d}가지\n합계: {a+b+c+d}가지\n\n전체 역 수: {station_cnt}개\n가능한 조합 수: {combinations}가지")
# print("%s seconds" % (time.time() - start_time))