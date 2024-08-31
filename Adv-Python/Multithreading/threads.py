"""Running seperate threads parellel to the main script"""
import time
import threading


def func(timer: int, serial: int) -> None:
    print(f"func()-{serial} sleeping for {timer} second(s)")
    time.sleep(timer)
    print(f"func()-{serial} done sleeping")


def main() -> None:
    start: float = time.perf_counter()

    t1: threading.Thread = threading.Thread(
        target=func, args=[3, 1])
    t2: threading.Thread = threading.Thread(
        target=func, args=[4, 2])
    t3: threading.Thread = threading.Thread(
        target=func, args=[2, 3])

    t1.start()
    t2.start()
    t3.start()

    end: float = time.perf_counter()
    print(f"Time elapsed : {round(end - start, 2)} second(s)") # 0.0 seconds, since main() runs independently


if __name__ == "__main__":
    main()
