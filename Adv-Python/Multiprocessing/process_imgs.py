"""Multiprocessing used for concurrent processing of multiple images"""

import os
from time import perf_counter
from PIL import Image, ImageFilter
from concurrent.futures import ProcessPoolExecutor as PPE


img_dir: str = "../Resources/Images"
processed_dir: str = "../Resources/Processed_Images"


def img_resize_blur(img_path: str) -> None:
    size: tuple[int, int] = (800, 800)
    img: Image.open.image = Image.open(img_path)

    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)

    output_path: str = os.path.join(processed_dir, os.path.basename(img_path))
    img.save(output_path)
    print(f"{img_path} was processed and saved to {output_path}.")


def main() -> None:
    os.makedirs(processed_dir, exist_ok=True)

    img_paths: list[str] = []
    for root, _, files in os.walk(img_dir):
        for file in files:
            if file.endswith(".jpg"):
                img_paths.append(os.path.join(root, file))

    start: float = perf_counter()

    with PPE() as p_executor:
        p_executor.map(img_resize_blur, img_paths)

    end: float = perf_counter()
    print(f"\nTime elapsed: {round(end - start, 2)} second(s)\n")  # 4.67s


if __name__ == "__main__":
    main()
