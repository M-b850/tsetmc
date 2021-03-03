from django.test import TestCase

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class DataTest(TestCase):
    def test_crawl(self):
        URL = 'http://www.tsetmc.com/loader.aspx?ParTree=15131F'
        opts = Options()
        opts.set_headless()
        browser = Firefox(options=opts)
        browser.get(URL)

        