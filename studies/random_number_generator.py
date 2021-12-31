import asyncio
import random
from enum import Enum
import time

MAX_THRESHOLD = 25
MIN_THRESHOLD = 5


class Colors(Enum):
    NONE = "\033[0m"
    CYAN = "\033[36m"
    RED = "\033[91m"
    MAGENTA = "\033[35m"

    @staticmethod
    def available() -> list:
        return [i.name for i in Colors]


async def rand_num(color: Colors, threshold: int) -> int:
    """Try random numbers until a number greater that threshold is found."""
    assert color in Colors, "Invalid colour chosen"
    print(color.value + f"Starting random number generation with threshold: {threshold}")
    num = random.randint(1, threshold + 10)
    if num > threshold:
        print(color.value + f"--->Found a perfect number {num} with threshold: {threshold}!" + Colors.NONE.value)
        return num
    print(color.value + f"Random number {num} too low to be perfect. Gonna try again :(")
    await asyncio.sleep(max(num, 1))
    await rand_num(color, threshold)


async def run_async() -> float:
    print("===START ASYNC===")
    start = time.perf_counter()
    tasks = (rand_num(color, random.randint(MIN_THRESHOLD, MAX_THRESHOLD)) for color in Colors)
    await asyncio.gather(*tasks)
    print("===END ASYNC===")
    return time.perf_counter() - start


async def run_sequential() -> float:
    print("===START SEQ===")
    start = time.perf_counter()
    for color in Colors:
        await rand_num(color, random.randint(MIN_THRESHOLD, MAX_THRESHOLD))
    print("===END SEQ===")
    return time.perf_counter() - start


if __name__ == '__main__':
    random.seed(444)
    sequential = asyncio.run(run_async())
    sequential_time = asyncio.run(run_sequential())
    print(f"Async took {sequential}, sequential took {sequential_time}")
