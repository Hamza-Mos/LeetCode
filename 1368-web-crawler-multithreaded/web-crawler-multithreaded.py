# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque
from concurrent import futures

class Solution:

    def _get_hostname(self, url):
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self._get_hostname(startUrl)
        crawled_urls = set([startUrl])

        with futures.ThreadPoolExecutor() as executor:
            q = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while q:

                # Find any crawling that has completed
                while True:
                    urls = q.popleft()
                    if urls.done():
                        break
                    q.append(urls)

                for url in urls.result():
                    if self._get_hostname(url) == hostname and url not in crawled_urls:
                        crawled_urls.add(url)
                        q.append(
                            executor.submit(htmlParser.getUrls, url)
                        )

        return list(crawled_urls)