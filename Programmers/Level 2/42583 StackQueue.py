from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    sum_bridge = 0
    while True:
        if len(truck_weights) == 0:
            answer += bridge_length
            break
        curr_truck = truck_weights.popleft()
        if sum_bridge - bridge[0] + curr_truck <= weight:
            bridge.append(curr_truck)
            sum_bridge += curr_truck
            off_bridge_truck = bridge.popleft()
            sum_bridge -= off_bridge_truck
            answer += 1
        else:
            truck_weights.appendleft(curr_truck)
            off_bridge_truck = bridge.popleft()
            sum_bridge -= off_bridge_truck
            bridge.append(0)
            answer += 1

    return answer
