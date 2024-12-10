from collections import deque

N, K = map(int, input().split())

def bfs(start, target):
    visited = [False] * 100001
    queue = deque([(start, 0)])  # (위치, 걸린 시간)

    # BFS 실행
    while queue:
        current, time = queue.popleft()

        # 동생을 찾으면 종료
        if current == target:
            return time

        # 이미 방문한 노드는 건너뛰기
        if visited[current]:
            continue
        visited[current] = True

        # 다음 이동 가능 위치 추가
        next_positions = [current - 1, current + 1, current * 2]
        for next_pos in next_positions:
            # 유효한 위치인지 확인
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                queue.append((next_pos, time + 1))

print(bfs(N, K))