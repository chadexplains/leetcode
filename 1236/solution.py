class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        queue = deque([startUrl])
        hostname = startUrl.split('/')[2]
        while queue:
            url = queue.popleft()
            if url not in visited:
                visited.add(url)
                for next_url in htmlParser.getUrls(url):
                    if next_url.split('/')[2] == hostname:
                        queue.append(next_url)
        return list(visited)