import random, time
from collections import deque
import threading

class LeakyBucket:
    def __init__(self, capacity, processing_rate):
        self.bucket = deque()
        self.capacity = capacity
        self.processing_rate = processing_rate

    def allow_request(self, request):
        if len(self.bucket) + 1 > self.capacity:
            print(f"Dropping: {request}")
            return False
        self.bucket.append(request)
        return True
    
    def process_request(self):
        requests = []
        for i in range(self.processing_rate):
            if not self.bucket:
                break
            request = self.bucket.popleft()
            requests.append(request)
        return requests

class Request:

    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return f"request id: {self.id}"


def add_request():
    while True:
        requests = rate_limiter.process_request()
        print(f"Processing requests: {requests}")
        time.sleep(1)



if __name__ == "__main__":
    rate_limiter = LeakyBucket(5, 2)

    t = threading.Thread(target=add_request)
    t.start()

    while True:
        request = Request(random.randint(1, 10000))
        rate_limiter.allow_request(request)
        time.sleep(0.2)
