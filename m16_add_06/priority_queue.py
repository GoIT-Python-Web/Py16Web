import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return not bool(self.queue)
