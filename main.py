import timeit
import logging
import asyncio
import time

def asyc_count():
    async def count():
        print("One")
        await asyncio.sleep(1)
        print("Two")

    async def main():
        await asyncio.gather(count(), count(), count())

    asyncio.run(main())


def count():
    def count():
        print("One")
        time.sleep(1)
        print("Two")

    for _ in range(3):
        count()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(timeit.timeit(asyc_count, number=5))
    logging.info(timeit.timeit(count, number=5))
