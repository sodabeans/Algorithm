import heapq

def solution(jobs):
    curr_time = 0 # 현재시점
    answer = 0 # 각각의 작업이 소요된 시간의 합
    idx = 0
    heap = []
    
    while idx < len(jobs): # 모든 job을 확인
        for job in jobs:
            if 0 <= job[0] <= curr_time: # 요청이 들어온 시간이 미래시점이 아니라면
                heapq.heappush(heap, [job[1], job[0]]) # [소요시간, 요청시점] 순으로 힙에 추가 
                job[0] = -1 # 중복으로 카운트 하지 않기 위해 요청시점 리셋
        if heap: # 작업이 있다면
            curr_job = heapq.heappop(heap) # 가장 우선 순위에 있는 작업 pop
            curr_time += curr_job[0] # 작업이 소요된 시간만큼 현재시점이 흐름
            answer += curr_time - curr_job[1] # 이 작업이 총 소요된 시간은 지금시점에서 요청시점만큼 뺀 값
            idx += 1
        else:
            curr_time += 1 # 작업이 없다면, 작업 요청을 기다림
    
    return answer // len(jobs)
  
