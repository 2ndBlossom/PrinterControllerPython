import time

def delay(t):
    start_time = time.time()
    while (time.time() - start_time) < t:
        pass