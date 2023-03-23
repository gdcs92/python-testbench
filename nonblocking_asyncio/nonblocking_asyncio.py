import asyncio
from datetime import datetime
from time import sleep
import random


ITERATION_PERIOD = 2


def fill_iteration_period(start_time: datetime, iteration_period: int):
    now = datetime.now()
    delta_t = (now - start_time).total_seconds()

    remaining_time = iteration_period - delta_t

    if remaining_time < 0:
        print(f"(!) Período da iteração ultrapassado em {-remaining_time} segundos.")
        return

    print(f"Dormindo por {remaining_time} segundos para completar o período da iteração")
    sleep(remaining_time)


def run_sync_funcs_that_take_some_time():
    time_to_waste = random.uniform(0, ITERATION_PERIOD/2)
    sleep(time_to_waste)


async def func_that_may_take_time(task_id) -> None:
    if task_id == 3:
        func_running_time = round(random.uniform(0, 2*ITERATION_PERIOD), 4)
    else:
        func_running_time = round(random.uniform(0, 0.1), 4)

    # sleep(func_running_time)
    await asyncio.sleep(func_running_time)
    print(f"* Task {task_id} executada em {func_running_time:.4f} segundos.")
    return


async def run_async_funcs_that_may_take_time():
    num_tasks = 5
    tasks = [
        asyncio.create_task(func_that_may_take_time(i))
        for i in range(num_tasks)
    ]
    return await asyncio.gather(*tasks)


async def main():
    max_iter = 3

    for i in range(1, max_iter+1):
        iteration_start = datetime.now()
        print(f"Iteração {i} iniciada {iteration_start.strftime('%H:%M:%S.%f')}")

        run_sync_funcs_that_take_some_time()

        await run_async_funcs_that_may_take_time()

        fill_iteration_period(iteration_start, ITERATION_PERIOD)

        iteration_end = datetime.now()
        print(f"Iteração {i} terminada em {iteration_end.strftime('%H:%M:%S.%f')}")
        print(f"{(iteration_end - iteration_start).total_seconds() = }\n")


if __name__ == "__main__":
    asyncio.run(main())
    print("Loop principal finalizado.\n")
