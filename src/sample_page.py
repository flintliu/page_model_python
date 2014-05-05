#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Specific page object, inculding title, url and elements
author: Flint Liu
email: flintliu@hotmail.com
"""
from page import Page
from common_elements import *

#sample code of google search page

ELEMENTS = {"search_bar": ["window", "id", "gbqfq", "label_input"],\
            "search_button": ["window", "id", "gbqfba", "button"],\
            "lucky_button": ["window", "id", "gbqfbb", "button"]}
ELEMENTS.update(TOP_FUNC_BAR)

class GoogleSearchMainPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com.au"
        self.title = "Google"
        self.element_list = ELEMENTS