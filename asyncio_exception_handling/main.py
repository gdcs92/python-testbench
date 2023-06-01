import asyncio
import time

async def do_something(idx: int):
    print(f"{idx = } foi dormir.")
    t1 = time.time()
    await asyncio.sleep(idx)
    t2 = time.time()
    print(f"{idx = } acordou após {t2-t1:.3f} segundos.")

async def main():
    tasks = [
        asyncio.create_task(do_something(idx)) for idx in range(1, 5)
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
