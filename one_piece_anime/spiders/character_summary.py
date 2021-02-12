import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from shutil import which
import time

class CharacterSummarySpider(scrapy.Spider):
    name = 'character_summary'
    allowed_domains = ['comicvine.gamespot.com']
    start_urls = ['https://comicvine.gamespot.com/one-piece/4050-21397/characters/?page=0/']
    
    def __init__(self):
        options = Options()
        options.add_argument("--headless")

        chrome_path = which('../selenium_basics/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=chrome_path, options=options)

    def parse(self, response):
        
        for i in range(1, 25):
            self.driver.get(f'https://comicvine.gamespot.com/one-piece/4050-21397/characters/?page={i}/')
            self.driver.implicitly_wait(2)
            time.sleep(2)
            html = self.driver.page_source
            resp = Selector(text=html)
            characters = resp.xpath('//ul[@class="editorial"]/li')

            for item in characters:
                yield {
                    "name": item.xpath('.//a/h3/text()').get(),
                    "summary": item.xpath('normalize-space(.//a/p/text())').get()
                }
