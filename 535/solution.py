class Codec:
    def __init__(self):
        self.urls = {}
        self.alphabet = string.ascii_letters + '0123456789'
        self.base_url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.urls:
            code = ''.join(random.choice(self.alphabet) for _ in range(6))
            if code not in self.urls:
                self.urls[code] = longUrl
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.split('/')[-1]
        return self.urls[code]
