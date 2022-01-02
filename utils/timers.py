import time
from functools import wraps
from typing import Callable, Any


def time_func_run(func: Callable) -> Any:
    """Run a function and only return the execution time."""
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        print(f"===START {func.__name__.upper()}===")
        start = time.perf_counter()
        await func(*args, **kwargs)
        print(f"===END {func.__name__.upper()}===")
        return time.perf_counter() - start
    return wrapper
