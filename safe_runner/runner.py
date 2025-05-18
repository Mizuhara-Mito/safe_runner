import multiprocessing
import time
import psutil
from .exceptions import ResourceLimitExceeded, TimeoutExceeded

def _start_and_monitor(target, cpu_limit_percent, memory_limit_mb, time_limit_sec, on_fail):
    process = multiprocessing.Process(target=target)
    process.start()

    try:
        proc = psutil.Process(process.pid)
        start_time = time.time()

        while time.time() - start_time < time_limit_sec:
            if not proc.is_running():
                break

            cpu = proc.cpu_percent(interval=0.5)
            mem = proc.memory_info().rss / 1024 / 1024

            if cpu > cpu_limit_percent:
                proc.terminate()
                raise ResourceLimitExceeded(f"CPU usage exceeded: {cpu:.1f}% > {cpu_limit_percent}%")

            if mem > memory_limit_mb:
                proc.terminate()
                raise ResourceLimitExceeded(f"Memory usage exceeded: {mem:.1f}MB > {memory_limit_mb}MB")

        else:
            proc.terminate()
            raise TimeoutExceeded(f"Execution time exceeded {time_limit_sec} seconds")

    except (ResourceLimitExceeded, TimeoutExceeded) as e:
        if on_fail:
            on_fail(e)

    process.join()

def run_with_limits(target_function, cpu_limit_percent=50.0, memory_limit_mb=100, time_limit_sec=10, on_fail=None):
    """
    Run a target function under resource constraints.

    :param target_function: Function to execute
    :param cpu_limit: CPU usage limit (%)
    :param memory_limit_mb: Memory limit (in MB)
    :param time_limit: Time limit (seconds)
    :param on_fail: Callback function called on failure (receives exception as argument)
    """
    _start_and_monitor(
        target=target_function,
        cpu_limit_percent=cpu_limit_percent,
        memory_limit_mb=memory_limit_mb,
        time_limit_sec=time_limit_sec,
        on_fail=on_fail
    )
