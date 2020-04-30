import scrapy


class DoubanBookItem(scrapy.Item):

    book_name = scrapy.Field()

    book_score = scrapy.Field()

    book_detail= scrapy.Field()
