import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from shutil import which
import time

class CharactersSpider(scrapy.Spider):
    name = 'characters'
    allowed_domains = ['www.animecharactersdatabase.com', 'google.com']
    start_urls = ['https://google.com']

    def __init__(self):
        options = Options()
        options.add_argument('--headless')

        chrome_path = which("../selenium_basics/chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=chrome_path, options=options)


    def parse(self, response):
        self.driver.get('https://google.com')
        self.driver.implicitly_wait(2)
        input = self.driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
        input.send_keys("one piece characters list" + Keys.ENTER)
        self.driver.implicitly_wait(3)
        
        link = self.driver.find_element_by_xpath('(//div[@class="yuRUbf"]/a)[14]')
        link.click()
        time.sleep(6)
        self.driver.implicitly_wait(4)
        
        html = self.driver.page_source
        resp = Selector(text=html)
        characters = resp.xpath('//div[@id="tile"]/ul/li')
        for character in characters:
            yield {
                "name": character.xpath('.//p[2]/a/text()').get(),
                "imageURL": character.xpath('.//a/img/@src').get()
            }
