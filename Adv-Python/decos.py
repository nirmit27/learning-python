"""Creating decorators."""

from time import sleep, perf_counter


def timer_decorator(func):
    """For performance logging."""
    def timer(sec: int):
        """Returns the time elapsed rounded off to 2 decimal places."""
        start: float = perf_counter()
        func(sec)
        end: float = perf_counter()
        print(f"\nTime elapsed : {round(end - start, 2)} seconds")
        return timer
    return timer


@timer_decorator
def funky(sec: int) -> None:
    """Sample function for testing the decorator."""
    print(f"Sleeping for {sec} seconds ...")
    sleep(sec)
    print("Waking up!")


def main() -> None:
    funky(4)


if __name__ == "__main__":
    main()
