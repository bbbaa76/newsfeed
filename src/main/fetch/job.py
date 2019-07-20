from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .nzherald import NzHerald

class Job:

    def ___init___(self):
        self.browser = None

    def siteSwitcher(self, siteName):
        url = {
            'nzherald': 'https://www.nzherald.co.nz',
            'stuff': 'https://www.stuff.co.nz/',
            'newsHub': 'https://www.newshub.co.nz/home.html',
            'zb': 'https://www.newstalkzb.co.nz/',
            'oneNews': 'https://www.tvnz.co.nz/one-news'
        }.get(siteName, "https://www.nzherald.co.nz")
        return url
    
    def browserOpen (self):
        self.browser = webdriver.Firefox()

    def fetch (self, siteName):
        url = self.siteSwitcher(siteName)
        self.browser.get(url)
        if siteName == 'nzherald':
            nzherald = NzHerald(self.browser)
            nzherald.fetch()
        


    def browserClose (self):
        self.browser.close()