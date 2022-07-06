import concurrent.futures
import blog_spider1


# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider1.craw, blog_spider1.urls)
    htmls = list(zip(blog_spider1.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider1.parse, html)
        futures[future] = url
    
    # for future, url in futures.items():
    #     print(url, future.result())

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())
