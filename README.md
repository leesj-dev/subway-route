# subway-route
이 코드는 수도권 지하철에서 A역에서 B역으로 최소 환승으로 이동하는 모든 경우의 수에 대하여, 거치는 노선의 수의 최댓값이 "4"임을 증명합니다.

증명 순서는 다음과 같습니다.
1. `crawling.py`: 위키백과의 '수도권 전철역 목록'을 크롤링 및 파싱하여 `station_line.py`로 저장
2. `main.py`: DFS(Depth First Search)를 수행하여 결과값을 `result.txt`로 저장