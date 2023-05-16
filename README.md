# subway-route
이 코드는 수도권 지하철에서 A역에서 B역으로 최소 환승으로 이동하는 모든 경우의 수에 대하여, 거치는 노선의 수의 최댓값이 "4"임을 증명합니다.

증명 순서는 다음과 같습니다.
1. `crawling.py`: 위키백과의 '수도권 전철역 목록'을 크롤링 및 파싱하여 `station_line.py`로 저장
2. `main.py`: BFS(너비 우선 탐색)를 수행하여 결과값을 `result.txt`로 저장
> `station_line_new.py`: 인천공항 자기부상열차 (휴업 중) 및 역명이 확정된 개통 예정 노선 (별내선, 대곡소사선, 동북선, 안산선, GTX-A/B/C)을 추가한 역명 정보

가능한 경우의 수를 나열하면 다음과 같습니다.
* 1개 노선: $18146$
* 2개 노선: $123728$
* 3개 노선: $59397$
* 4개 노선: $3209$
* 합계: $204480$

전체 역 수는 $640$개이므로, 검산해보면 이론상 가능한 조합의 수 ${}_{640}\mathrm{C}_2 = 204480$ 와 동일함을 알 수 있습니다.