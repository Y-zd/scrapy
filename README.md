scrapy爬虫

- [入门教程](https://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html)

  - PS: 浏览器可以装xpath helper插件辅助查看 xpath

- [爬取豆瓣TOP250电影数据](/DoubanMovieTop250)
  ```
  # 项目根目录(DoubanMovieTop250\DoubanMovieTop250)下执行以下命令
  scrapy crawl douban_movie_top250 -o douban.csv
  ```  
