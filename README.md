# subway-route

## TL;DR
이 코드는 수도권 지하철에서 A역에서 B역으로 최소 환승으로 이동하는 모든 경우의 수에 대하여, 거치는 노선의 수의 최댓값이 “$\,4\,$”임을 증명합니다. (참고로 현재 휴업 중인 인천공항 자기부상열차를 포함하면 최댓값은 “$\,5\,$”입니다.)
증명 순서는 다음과 같습니다.
1. `crawling.py`: 위키백과의 '수도권 전철역 목록'을 크롤링 및 파싱하여 `station_line.py`로 저장
2. `main.py`: BFS(너비 우선 탐색)를 수행하여 결과값을 `result.txt`로 저장
> `station_line_new.py`: 현재 휴업 중인 인천공항 자기부상열차 및 역명이 확정된 개통 예정 노선 (별내선, 대곡소사선, 동북선, 안산선, GTX-A/B/C)을 추가한 역명 정보

가능한 경우의 수를 나열하면 다음과 같습니다.
* 1개 노선: $18146$
* 2개 노선: $123728$
* 3개 노선: $59397$
* 4개 노선: $3209$
* 합계: $204480$

전체 역 수는 $640$개이므로, 검산해보면 이론상 가능한 조합의 수 ${}_{640}\mathrm{C}_2 = 204480$ 와 동일함을 알 수 있습니다.

<br>

## For those of you who are interested..

알고리즘을 수학적으로 설명하자면 다음과 같습니다. 현재 우리는 임의의 출발역이 정해졌을 때, 그 출발역으로부터 노선도에 존재하는 모든 역 각각에 최소환승으로 도착할 때 몇 개의 노선을 거쳐야 하는지를 구하고 싶습니다.

$f : X = \left\\{ x \\: | \\: x\textrm{ 는 수도권 지하철역}\right\\} \rightarrow  Y = \left\\{ y \\: | \\: y\textrm{ 는 역을 통과하는 노선들의 집합}\right\\}$
$g : X = \left\\{ x \\: | \\: x\textrm{ 는 수도권 지하철 노선}\right\\}  \rightarrow  Y = \left\\{ y \\: | \\: y\textrm{ 는 그 노선을 통과하는 역들의 집합}\right\\}$

여기서 헷갈리지 말아야 할 점은 $f$ 와 $g$ 의 <b>공역의 원소 각각이 하나의 '집합'</b>이라는 것입니다. 예컨대 $f(\textrm{교대}) = \\{2,\\:3\\}$ 이고, $g(8) = \\{\textrm{암사},\\:\textrm{천호},\\:\cdots,\\:\textrm{모란}\\}$ 입니다.

$h : X = \left\\{ x \\: | \\: x\textrm{ 는 수도권 지하철역}\right\\} \rightarrow  Y = \left\\{ y \\: | \\: y\textrm{ 는 출발역으로부터 그 역까지 최소환승으로 갔을 때 거친 노선 수}\right\\}$

$Q = \\{x \\: | \\: x\textrm{ 는 (역명, 노선명) 형태의 순서쌍}\\}$

$V = \\{x \\: | \\: x\textrm{ 는 지금까지 거쳐간 노선들}\\}$

출발역을 $S_1$ 이라고 하겠습니다. 출발역과 도착역이 같을 경우 한 개의 노선도 거칠 필요가 없으므로 $h(S_1)=0$ 으로 정의합니다. $f(S_1)=\\{l_1,\\:l_2,\\:\cdots l_n\\}$ 라 하고 $Q$ 에 $(S_1,\\:l_1),\\:(S_1,\\:l_2),\\:\cdots,\\:(S_1,\\:l_n)$ 을 추가합니다. 그리고 아래를 시행합니다.

(i) $Q$ 의 첫째 항 $(S_k,\\:L_m)$ 에 해당하는 노선 $m$ 이 $V$의 원소가 아니라면 $V$ 에 $m$ 을 추가합니다. 만약 $m$ 이 $V$ 의 원소라면 마지막 단계로 넘어갑니다.

(ii) $m$ 을 지나는 역을 $g(m)$ 을 통해 구합니다. $g(m)$ 의 원소 $s_{1},\\:s_{2},\\:\cdots,\\:s_{i}$ 에 대하여 $s_{i}$ 를 이미 지나가지 않았다면 $h\left(x_i\right) = h\left(S_k\right) + 1$ 로 구하고, 이미 지나갔다면 마지막 단계로 넘어갑니다.

(iv) $s_{i}$ 를 지나는 노선을 $f\left(s_i\right)$ 를 통해 구합니다. $f\left(s_i\right)$ 의 원소 $s_{i,\\,1},\\:s_{i,\\,2},\\:\cdots,\\:s_{i,\\,j}$ 에 대하여, $s_{i,\\,j}$ 가 $V$ 의 원소가 아니라면 $Q$ 에 $s_{i,\\,j}$ 을 추가합니다.

> 이떄 $s_{i,\\,j}$ 를 탐색하지 않고 $Q$ 의 뒷부분으로 추가시키는 과정은 DFS (Depth-First Search)의 일환입니다. DFS는 주로 최단 경로를 찾을 때 사용하는 방법으로, 한 노드에서 다음 분기로 넘어가기 전 해당 분기의 모든 노드를 탐색하는 BFS (Breadth-First Search)에 비해 효율적입니다. 참고로 이 논제에서 환승역과 환승역 간 거리는 고려하지 않기 때문에 노드 간 가중치는 모두 같으므로 Dijkstra's algorithm 등을 도입할 필요는 없습니다.

(v) 지금까지 다룬 $\left(S_k,\\:L_m\right)$ 을 $Q$ 에서 삭제합니다. $Q$ 가 공집합이면 과정을 종료하고, 그렇지 않다면 (i)부터 다시 시작합니다.

> 이때 $Q$ 의 첫째 항을 제거하는 과정은 FIFO (First In First Out, 선입선출) 방식이므로, 속도를 위해 Python에서 deque를 사용합니다.