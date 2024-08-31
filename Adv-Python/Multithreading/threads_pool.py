"""Running seperate threads asynchronously in a pool"""
import time
import concurrent.futures


def func(timer: int) -> str:
    print(f"Sleeping for {timer} second(s)")
    time.sleep(timer)
    return f"Done sleeping for {timer} seconds"


def main() -> None:
    start: float = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        timers: list[int] = [i for i in range(5, 0, -1)]

        # f1 = executor.submit(func, 1, 1)
        # f2 = executor.submit(func, 1, 2)
        # f3 = executor.submit(func, 1, 3)
        # print(f1.result())
        # print(f2.result())
        # print(f3.result())

        # Alternatively ...
        # results: list = [executor.submit(func, timer) for timer in timers]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        # Alternatively ...
        results: list = list(executor.map(func, timers))
        for result in results:
            print(result)  # prints out in the order of starting of execution

    end: float = time.perf_counter()
    print(f"\nTime elapsed : {round(end - start, 2)} second(s)\n")  # 5.02s


if __name__ == "__main__":
    main()
