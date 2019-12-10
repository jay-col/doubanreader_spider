# -*- coding: utf-8 -*-
import scrapy


class DoubSpider(scrapy.Spider):
    name = 'doub_xpath'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self, response):
        for book in response.xpath("//tr[@class='item']"):
            yield {"bookname":book.xpath(".//div[@class='pl2']/a/text()").get().strip().replace("\n",""),
                    "bookdetail":book.xpath(".//p[@class='pl']/text()").get(),
                    "bookscore":book.xpath(".//span[@class='rating_nums']/text()").get(),
                    "bookscorenums":book.xpath(".//span[@class='pl']/text()").re(r"(\w+)人.*")[0],
                    "bookquote":book.xpath(".//span[@class='inq']/text()").get(),
                    "bookimg":book.xpath(".//a[@class='nbg']/img/@src").get()}
        next_page = response.xpath("//span[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)

                        

