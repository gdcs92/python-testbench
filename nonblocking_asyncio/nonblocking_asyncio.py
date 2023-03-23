import asyncio
from datetime import datetime
from time import sleep
import random


ITERATION_PERIOD = 2


def to_string(dt: datetime) -> str:
    return dt.strftime('%H:%M:%S.%f')


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
    task_start = datetime.now()
    print(f"* Task {task_id} iniciada em {to_string(task_start)}")

    if task_id == 3:
        func_running_time = round(random.uniform(0, 2*ITERATION_PERIOD), 4)
    else:
        func_running_time = round(random.uniform(0, 0.1), 4)

    # sleep(func_running_time)
    await asyncio.sleep(func_running_time)
    task_end = datetime.now()
    print(f"* Task {task_id} finalizada em {to_string(task_end)} ({func_running_time:.4f} segundos).")
    return


async def run_async_funcs_that_may_take_time():
    num_tasks = 5
    tasks = [
        asyncio.create_task(func_that_may_take_time(i))
        for i in range(num_tasks)
    ]
    done, pending = await asyncio.wait(tasks, timeout=0.1)
    print("\nTarefas pendentes:", len(pending))
    for task in pending:
        print(task, type(task))
    print()
    return


async def main():
    max_iter = 3

    for i in range(1, max_iter+1):
        iteration_start = datetime.now()
        print(f"Iteração {i} iniciada {to_string(iteration_start)}")

        run_sync_funcs_that_take_some_time()

        await run_async_funcs_that_may_take_time()

        fill_iteration_period(iteration_start, ITERATION_PERIOD)

        iteration_end = datetime.now()
        print(f"Iteração {i} terminada em {to_string(iteration_end)}")
        print(f"{(iteration_end - iteration_start).total_seconds() = }\n")


if __name__ == "__main__":
    asyncio.run(main())
    print("Loop principal finalizado.\n")
