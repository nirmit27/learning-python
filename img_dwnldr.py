""" For the automated downloading of images. """
from bing_image_downloader import downloader
from icrawler.builtin import GoogleImageCrawler


def bing_downloader(query, op_dir, limit) -> None:
    downloader.download(query=query, limit=limit, output_dir=op_dir,
                        adult_filter_off=True, force_replace=False, timeout=60)


def google_downloader(keyword, op_dir, limit) -> None:
    google_crawler = GoogleImageCrawler(storage={"root_dir": op_dir})
    google_crawler.crawl(keyword=keyword, max_num=limit)


def main() -> None:
    limit: int = int(input("Enter the limit (preferably don't exceed 100) : ")) or 10
    query: str = input(
        "\nEnter the keywords seperated by a space : ") or "white eggs"
    op_dir: str = input(
        "\nEnter the file download path : ") or r"data\white_eggs"
    google_downloader(query, op_dir, limit)
    # bing_downloader(query, op_dir, limit)


if __name__ == "__main__":
    main()
