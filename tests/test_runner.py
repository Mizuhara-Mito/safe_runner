import time
import pytest
from safe_runner import run_with_limits, TimeoutExceeded, ResourceLimitExceeded

def long_task():
    time.sleep(10)

def memory_hog():
    a = []
    while True:
        a.append(' ' * 10_000_000)
        time.sleep(0.1)

def cpu_burner():
    while True:
        sum(i*i for i in range(10_000))

def test_timeout():
    def handle_fail(e):
        assert isinstance(e, TimeoutExceeded)

    run_with_limits(long_task, time_limit_sec=2, on_fail=handle_fail)

def test_memory_exceed():
    def handle_fail(e):
        assert isinstance(e, ResourceLimitExceeded)

    run_with_limits(memory_hog, memory_limit_mb=50, time_limit_sec=5, on_fail=handle_fail)

def test_cpu_exceed():
    def handle_fail(e):
        assert isinstance(e, ResourceLimitExceeded)

    run_with_limits(cpu_burner, cpu_limit_percent=20.0, time_limit_sec=5, on_fail=handle_fail)
