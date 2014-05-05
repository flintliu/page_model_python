#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Action classes
author: Flint Liu
email: flintliu@hotmail.com
"""
from selenium import webdriver
from sample_page import GoogleSearchMainPage

def open_browser(browser_name, target_url):
    if browser_name == "firefox":
        br = webdriver.Firefox()
        br.get(target_url)
        return br

def do_search(browser, key_word):
	search_page = GoogleSearchMainPage(browser)
	search_bar = search_page.get_element("search_bar")
	search_bar.set_keys(key_word)