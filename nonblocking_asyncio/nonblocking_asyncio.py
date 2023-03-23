import asyncio
from datetime import datetime
from time import sleep
import random


ITERATION_PERIOD = 2


def run_tasks_that_take_some_time():
    time_to_waste = random.uniform(0, ITERATION_PERIOD/2)
    sleep(time_to_waste)


def fill_iteration_period(start_time: datetime, iteration_period: int):
    now = datetime.now()
    delta_t = (now - start_time).total_seconds()

    if delta_t >= iteration_period:
        return

    remaining_time = iteration_period - delta_t
    print(
        f"Dormindo por {remaining_time} segundos para completar o período da iteração"
    )
    sleep(remaining_time)


async def main():
    max_iter = 5

    for i in range(1, max_iter+1):
        iteration_start = datetime.now()
        print(f"Iteração {i} iniciada {iteration_start.strftime('%H:%M:%S.%f')}")

        run_tasks_that_take_some_time()

        fill_iteration_period(iteration_start, ITERATION_PERIOD)

        iteration_end = datetime.now()
        print(f"Iteração {i} terminada em {iteration_end.strftime('%H:%M:%S.%f')}")
        print(f"{(iteration_end - iteration_start).total_seconds() = }\n")


if __name__ == "__main__":
    asyncio.run(main())
    print("Loop principal finalizado.\n")
