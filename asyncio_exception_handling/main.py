import asyncio
import time

async def do_something(idx: int, raise_exceptions: bool) -> float:
    print(f"{idx = } foi dormir.")
    t1 = time.time()
    await asyncio.sleep(idx)
    t2 = time.time()
    deltat = t2 - t1

    if idx in [1, 3] and raise_exceptions:
        raise RuntimeError(f"Houve um problema na execução da tarefa {idx}")

    print(f"{idx = } acordou após {deltat:.3f} segundos.")
    return deltat

async def main():

    raise_exceptions = True

    tasks = [
        asyncio.create_task(do_something(idx, raise_exceptions))
        for idx in range(1, 5)
    ]
    deltas = await asyncio.gather(*tasks, return_exceptions=True)

    print(f"\n{deltas = }\n")

    if any(isinstance(x, Exception) for x in deltas):
        print("Ocorreram exceções nas tarefas.")
    else:
        print("Todas as tarefas foram executadas com sucesso.")

asyncio.run(main())
