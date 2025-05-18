from safe_runner import run_with_limits, TimeoutExceeded
from utils import on_fail
import time

def long_task():
    time.sleep(10)

if __name__ == "__main__":
    print(">>> Running TIME LIMIT test")
    run_with_limits(
        target_function=long_task,
        time_limit_sec=2,
        on_fail=on_fail
    )
