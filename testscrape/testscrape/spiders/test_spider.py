import scrapy

class PostsSpider(scrapy.Spider):
    name="posts"
    allowed_domains = ['https://auto.naver.com/bike/mainList.nhn']
    start_urls = [
        'https://auto.naver.com/bike/mainList.nhn'
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
       
       
       