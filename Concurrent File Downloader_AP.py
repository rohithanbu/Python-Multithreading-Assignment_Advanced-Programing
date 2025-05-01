import threading
import requests
import time

def download_file(url, index):
    response = requests.get(url)
    with open(f'file_{index}.html', 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: file_{index}.html")

def concurrent_downloader(urls):
    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_file, args=(url, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def sequential_downloader(urls):
    for i, url in enumerate(urls):
        download_file(url, i)

# Example
if __name__ == "__main__":
    urls = [
        'https://example.com',
        'https://www.google.com',
        'https://www.bing.com',
        'https://www.wikipedia.org'
    ]

    start = time.time()
    sequential_downloader(urls)
    print("Sequential download time:", time.time() - start)

    start = time.time()
    concurrent_downloader(urls)
    print("Concurrent download time:", time.time() - start)
