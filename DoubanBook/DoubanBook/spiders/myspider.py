from scrapy import Request
from scrapy.spiders import Spider
from DoubanBook.items import DoubanBookItem
class DoubanBookSpider(Spider):
    name = 'DoubanBook'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.douban.com/doulist/118410371/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanBookItem()
        movies = response.xpath('//div[@class="article"]//div[@class="bd doulist-subject"]')
        for movie in movies:
            item['book_name'] = movie.xpath(
                './/div[@class="title"]/a[@target="_blank"]/text()').extract()[0]

            item['book_score'] = movie.xpath(
                './/div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]

            item['book_detail'] = movie.xpath(
                './/div[@class="abstract"]').extract()[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            yield Request(next_url[0], headers=self.headers)
