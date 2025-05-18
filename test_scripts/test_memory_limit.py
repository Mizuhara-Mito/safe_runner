from safe_runner import run_with_limits, ResourceLimitExceeded
from utils import on_fail
import time

def memory_hog():
    a = []
    while True:
        a.append(' ' * 10_000_000)
        time.sleep(0.1)

if __name__ == "__main__":
    print(">>> Running MEMORY LIMIT test")
    run_with_limits(
        target_function=memory_hog,
        memory_limit_mb=50,
        time_limit_sec=10,
        on_fail=on_fail
    )
