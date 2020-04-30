import scrapy


class DoubanMovieItem(scrapy.Item):

    ranking = scrapy.Field()

    movie_name = scrapy.Field()

    score = scrapy.Field()

    score_num = scrapy.Field()
