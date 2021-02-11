import scrapy


class CharacterHeightSpider(scrapy.Spider):
    name = 'character_height'
    allowed_domains = ['www.animeshirtclub.com']
    start_urls = ['https://www.animeshirtclub.com/blogs/news/height-of-one-piece-characters/']

    def parse(self, response):
        
        heights = response.xpath('(//tr[@role="row"])[position()!=1]')

        for item in heights:
            yield {
                "name": item.xpath('.//td[@class="col-1 odd sorting_1"]/text()').get(),
                "height": item.xpath('.//td[@class="col-2 even"]/text()').get()
            }
