def DFS(answer, goal, relations, visited):
    if len(answer) == goal:
        return answer
    curr = answer[-1]
    if curr not in relations: # 현재 공항에서 갈 수 있는 경로가 없는 경우 처리
        return None
    for (arrive, idx) in relations[curr]:
        if not visited[idx]:
            visited[idx] = 1
            answer.append(arrive)
            sol = DFS(answer, goal, relations, visited)
            if sol:
                return sol
            answer.pop()
            visited[idx] = 0
    

def solution(tickets):
    goal = len(tickets) + 1
    answer = ["ICN"]

    relations = {}
    for i in range(len(tickets)): # 여행 경로 그래프 생성, 티켓의 번호를 확인 (edge)
        a, b = tickets[i]
        if a not in relations:
            relations[a] = []
        relations[a].append((b, i))
    for depart in relations:
        relations[depart].sort()
    visited = [0] * len(tickets)
        
    return DFS(answer, goal, relations, visited)
