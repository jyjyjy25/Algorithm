import sys
from collections import deque


def BFS(screen, clipboard):
    queue = deque([(screen, clipboard, 0)])
    packages.add((screen, clipboard))

    while queue:
        screen, clipboard, time = queue.popleft()
        if screen == S:
            return time
        
        # 1. 화면에 있는 이모티콘 모두 복사 후 클립보드에 저장
        if screen <= 1000:
            if (screen, screen) not in packages:
                queue.append((screen, screen, time+1))
                packages.add((screen, screen))

        # 2. 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
        if clipboard > 0 and screen+clipboard <= 1000:
            if (screen+clipboard, clipboard) not in packages:
                queue.append((screen+clipboard, clipboard, time+1))
                packages.add((screen+clipboard, clipboard))

        # 3. 화면에 있는 이모티콘 중 하나 삭제
        if 0 < screen-1 <= 1000:
            if (screen-1, clipboard) not in packages:
                queue.append((screen-1, clipboard, time+1))
                packages.add((screen-1, clipboard))


S = int(sys.stdin.readline())
packages = set()
print(BFS(1, 0))