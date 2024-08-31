"""Intro to Multiprocessing"""

from time import perf_counter, sleep
# from multiprocessing  import Process
from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor as PPE


def funky(timer: int) -> str:
    print(f"Sleeping for {timer} seconds ...")
    sleep(timer)
    return f"Done sleeping for {timer} seconds."


def main() -> None:
    start: float = perf_counter()

    # p1: multiprocessing.Process = multiprocessing.Process(target=funky, args=[1])
    # p2: multiprocessing.Process = multiprocessing.Process(target=funky, args=[1])

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # Alternatively ...
    # processes: list[multiprocessing.Process] = []
    # for t in range(10):
    #     p: multiprocessing.Process = multiprocessing.Process(
    #         target=funky, args=[t])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    with PPE() as p_executor:
        timers: list[int] = [i for i in range(10, 0, -1)]

        # Alternatively ...
        # with PPE() as p_executor:
        #     results: list = list(p_executor.map(funky, timers))
        #     for result in results:
        #         print(result) # prints out in the order of starting of execution

        # Alternatively ...
        results: list = [p_executor.submit(funky, timer) for timer in timers]
        for p in as_completed(results):
            print(p.result())

    end: float = perf_counter()
    print(f"\nTime elapsed : {round(end - start, 2)} second(s)\n")  # 10.32s


if __name__ == "__main__":
    main()
