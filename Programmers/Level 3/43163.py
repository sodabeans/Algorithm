from collections import deque

def is_edge(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return True if cnt == 1 else False


def solution(begin, target, words):
    # 마지막 제한사항 처리
    if target not in words:
        return 0
    # Graph 만들기
    relations = {word: [] for word in words}
    relations[begin] = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_edge(words[i], words[j]):
                relations[words[i]].append(words[j])
                relations[words[j]].append(words[i])
        if is_edge(begin, words[i]):
            relations[begin].append(words[i])
    # BFS
    answer = float('inf')
    visited = {word: 0 for word in words}
    queue = deque([(begin, 0)])
    while queue:
        curr, step = queue.popleft()
        for word in relations[curr]:
            if word == target:
                answer = min(answer, step + 1)
                break
            if visited[word] == 0:
                visited[word] += 1
                queue.append((word, step + 1))
    return answer
