"""Asynchronously downloading multiple images for saving time"""

import json
import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor as TPE


def download_imgs(img_url: str) -> None:
    img_bytes: bytes = requests.get(img_url).content
    img_name: str = img_url.split('/')[3]

    with open(f"../Resources/Images/{img_name}.jpg", "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} downloaded successfully!")


def main() -> None:
    img_urls: list[str] = json.load(open("../Resources/data.json"))

    start: float = perf_counter()

    with TPE() as executor:
        executor.map(download_imgs, img_urls)

    end: float = perf_counter()
    print(f"\nTime elapsed : {round(end - start, 2)} second(s)\n")  # 2.79s


if __name__ == "__main__":
    main()
