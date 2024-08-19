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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # dfs
        visited = set()
        res = []

        def getHostName(url):
            return url.split("/")[2]

        hostname = getHostName(startUrl)

        def dfs(url):
            if url in visited:
                return

            visited.add(url)
            res.append(url)

            for nextUrl in htmlParser.getUrls(url):
                if hostname == getHostName(nextUrl):
                    dfs(nextUrl)

        dfs(startUrl)
        return res

        