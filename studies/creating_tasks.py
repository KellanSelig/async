"""Doing some basic low level event loop work"""
import asyncio
from utils import time_func_run


async def task(n: int) -> str:
    print(f"I'm task number {n}!")
    await asyncio.sleep(n)
    print(f"I waited for {n} seconds.")
    return f"This is the result of task {n}"


@time_func_run
async def run_in_seq():
    # Simply awaiting tasks like this means each task will run sequentially
    await task(1)
    await task(2)
    await task(3)
    await task(4)


@time_func_run
async def run_concurrent():
    # Creating tasks like this will mean they are run concurrently
    t1 = asyncio.create_task(task(1))
    t2 = asyncio.create_task(task(2))
    t3, t4 = (asyncio.create_task(task(i)) for i in (3, 4))
    await t1
    await t2
    await t3
    await t4


@time_func_run
async def also_run_concurrent():
    # Can run things concurrently and get the individual results using as_completed
    tasks = [asyncio.create_task(task(i)) for i in range(1, 5)]
    for result in asyncio.as_completed(tasks):
        await result


@time_func_run
async def run_concurrent_with_result():
    # Same as above, but showing reading the results of our tasks
    tasks = [asyncio.create_task(task(i)) for i in range(1, 5)]
    for result in asyncio.as_completed(tasks):
        r = await result
        print(r)


@time_func_run
async def run_concurrent_with_result_gather():
    # Same as above, but showing the difference between as_completed and using gather
    result = await asyncio.gather(*(task(i) for i in range(1, 5)))
    for r in result:
        print(r)


if __name__ == '__main__':
    run_in_seq_time = asyncio.run(run_in_seq())
    run_concurrent_time = asyncio.run(run_concurrent())
    also_run_concurrent_time = asyncio.run(also_run_concurrent())
    run_concurrent_with_result_time = asyncio.run(run_concurrent_with_result())
    run_concurrent_with_result_gather_time = asyncio.run(run_concurrent_with_result_gather())
    print(
        f"{run_in_seq_time=}\n",
        f"{run_concurrent_time=}\n",
        f"{also_run_concurrent_time=}\n",
        f"{run_concurrent_with_result_time=}\n",
        f"{run_concurrent_with_result_gather_time=}"
    )
