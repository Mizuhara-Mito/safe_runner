# test_run.py
from safe_runner import run_with_limits, TimeoutExceeded, ResourceLimitExceeded
import time

def long_task():
    time.sleep(10)

def memory_hog():
    a = []
    while True:
        a.append(' ' * 10_000_000)
        time.sleep(0.1)

def on_fail(e):
    print(f"[TEST FAIL] Caught exception: {type(e).__name__} - {e}")

if __name__ == "__main__":
    print(">>> Running timeout test")
    run_with_limits(long_task, time_limit_sec=2, on_fail=on_fail)

    print(">>> Running memory limit test")
    run_with_limits(memory_hog, memory_limit_mb=50, time_limit_sec=5, on_fail=on_fail)
