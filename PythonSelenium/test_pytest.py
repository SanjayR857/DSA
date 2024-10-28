import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By

class TestWebApp:

    @pytest.fixture(scope='class')
    def setup(self):
        self.driver = webdriver.Chrome()
        yield self.driver
        self.driver.quit()

    def test_exam(self,setup):
        self.driver.get('https://testautomationpractice.blogspot.com/')
        assert  self.driver.text=='erre'
