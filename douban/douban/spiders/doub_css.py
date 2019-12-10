# -*- coding: utf-8 -*-
import scrapy


class DoubSpider(scrapy.Spider):
    name = 'doub_css'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self, response):
        for book in response.css("tr.item"):
            yield {"bookname":book.css("div.pl2 a::text").get().strip(),
                    "bookdetail":book.css("p.pl::text").get(),
                    "bookscore":book.css("span.rating_nums::text").get(),
                    "bookscorenums":book.css("span.pl::text").re(r"(\w+)人.*"),
                    "bookquote":book.css("span.inq::text").get(),
                    "bookimg":book.css("a.nbg img::attr(src)").get()}
        next_page = response.css("span.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

                        

