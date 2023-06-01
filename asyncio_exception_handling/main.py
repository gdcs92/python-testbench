import asyncio
import time

async def do_something(idx: int) -> float:
    print(f"{idx = } foi dormir.")
    t1 = time.time()
    await asyncio.sleep(idx)
    t2 = time.time()
    deltat = t2 - t1
    print(f"{idx = } acordou após {deltat:.3f} segundos.")
    return deltat

async def main():
    tasks = [
        asyncio.create_task(do_something(idx)) for idx in range(1, 5)
    ]
    deltas = await asyncio.gather(*tasks)

    print(f"\n{deltas = }")

asyncio.run(main())
