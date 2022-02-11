import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,mixed)
        cnt += 1
        if len(scoville) ==1 and scoville[0] < K:
            return -1

    return cnt
