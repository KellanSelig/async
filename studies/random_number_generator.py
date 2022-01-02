import asyncio
import random
from enum import Enum
from utils import time_func_run

MAX_THRESHOLD = 25
MIN_THRESHOLD = 5


class Colors(Enum):
    NONE = "\033[0m"
    CYAN = "\033[36m"
    RED = "\033[91m"
    MAGENTA = "\033[35m"


async def rand_num(color: Colors, threshold: int) -> None:
    """Try random numbers until a number greater that threshold is found."""
    print(color.value + f"Starting random number generation with threshold: {threshold}")

    num = random.randint(1, threshold + 10)
    if num <= threshold:
        print(color.value + f"Random number {num} too low to be perfect. Gonna try again :(")
        await asyncio.sleep(max(num, 1))
        await rand_num(color, threshold)
    print(color.value + f"--->Found a perfect number {num} with threshold: {threshold}!" + Colors.NONE.value)


@time_func_run
async def run_async() -> None:
    tasks = (rand_num(color, random.randint(MIN_THRESHOLD, MAX_THRESHOLD)) for color in Colors)
    await asyncio.gather(*tasks)


@time_func_run
async def run_sequential() -> None:
    for color in Colors:
        await rand_num(color, random.randint(MIN_THRESHOLD, MAX_THRESHOLD))


if __name__ == '__main__':
    random.seed(444)
    async_time: float = asyncio.run(run_async())
    sequential_time: float = asyncio.run(run_sequential())
    print(f"Async took {async_time}, sequential took {sequential_time}")
