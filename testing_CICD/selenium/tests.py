import os
import pathlib
import unittest
from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("index.html"))
        self.assertEqual(driver.title, "My Webpage")

    def test_header_1(self):
        driver.get(file_uri("index.html"))
        header = driver.find_element_by_tag_name("h1")
        self.assertEqual(header.text, "This is a Webpage")

    def test_header_2(self):
        driver.get(file_uri("index.html"))
        header = driver.find_element_by_tag_name("h2")
        self.assertEqual(header.text, "This is a subtitle")

    def test_link(self):
        driver.get(file_uri("index.html"))
        link = driver.find_element_by_link_text("Click me")
        link.click()
        self.assertEqual(driver.title, "New Page")