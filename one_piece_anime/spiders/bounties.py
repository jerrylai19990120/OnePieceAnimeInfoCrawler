import scrapy



class BountiesSpider(scrapy.Spider):
    name = 'bounties'
    allowed_domains = ['listfist.com']
    start_urls = ['http://listfist.com/list-of-one-piece-characters-by-bounty/']

    def parse(self, response):
        bounties = response.xpath('(//tr)[position()!=1]')

        for bounty in bounties:
            yield {
                "name": bounty.xpath('.//td[@class="col-3 odd"]/text()').get(),
                "bounty": bounty.xpath('.//td[@class="col-4 even"]/text()').get().strip("\u0e3f")
            }
