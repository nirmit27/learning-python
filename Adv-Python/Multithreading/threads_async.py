"""Running seperate threads asynchronously"""
import time
import threading


def func(timer: int, serial: int) -> None:
    print(f"func()-{serial} sleeping for {timer} second(s)")
    time.sleep(timer)
    print(f"func()-{serial} done sleeping")


def main() -> None:
    start: float = time.perf_counter()

    threads: list[threading.Thread] = []
    for _ in range(10):
        t: threading.Thread = threading.Thread(target=func, args=[3, _])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()  # joining all the threads for async. execution

    end: float = time.perf_counter()
    print(f"\nTime elapsed : {round(end - start, 2)} second(s)\n")  # 3.01s


if __name__ == "__main__":
    main()
