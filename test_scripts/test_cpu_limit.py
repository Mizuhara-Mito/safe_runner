from safe_runner import run_with_limits, ResourceLimitExceeded
from utils import on_fail

def cpu_intensive_task():
    while True:
        _ = sum(i * i for i in range(10_000))

if __name__ == "__main__":
    print(">>> Running CPU LIMIT test")
    run_with_limits(
        target_function=cpu_intensive_task,
        cpu_limit_percent=10.0,
        time_limit_sec=10,
        on_fail=on_fail
    )
