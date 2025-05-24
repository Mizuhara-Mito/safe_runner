# safe_runner

`safe_runner` is a lightweight Python package that allows you to execute any function under constraints like:

- Maximum CPU usage (% per second)
- Maximum Memory usage (in MB)
- Maximum execution time (in seconds)
- Optional failure callback handler

## Installation
```bash
pip install .
```

## Usage Example
```python
from safe_runner import run_with_limits

def heavy_task():
    while True:
        pass

def on_fail(error):
    print(f"Task failed due to: {error}")

run_with_limits(
    target_function=heavy_task,
    cpu_limit_percent=50.0,
    memory_limit_mb=100,
    time_limit_sec=5,
    on_fail=on_fail
)
```

## How to Test
To run the test suite using `pytest`:
1. Install development dependencies:
```bash
pip install -r requirements.txt
pip install pytest
```
2. Run the tests
```bash
pytest
```



## License
MIT