#!/uer/bin/python
# -*- coding: utf-8 -*-
"""
element selector base class
author: Flint LIU
email: flintliu@hotmail.com
"""

__version__ = "0.1"
__all__ = ["ElementSelector"]

from .object_models import sample_objects

class ElementSelector(object):
    """
    element selector base class
    """
    def __init__(self, element_name, elements_info, window):
        self.element_name = element_name
        self.elements_info = elements_info
        self.window = window
        self.path_flow = []
        
    def get_element_info(self, element_name):
        _element_info = self.elements_info.get(element_name)
        _parent_element = _element_info[0]
        _selection_method = _element_info[1]
        _selection_arg = _element_info[2]
        _element_type = _element_info[3]
        return _parent_element, _selection_method, _selection_arg, _element_type
    
    def element_selector(self, driver):
        if len(self.path_flow) == 1:
            return driver
        else:
            self.path_flow.pop(-1)
            _selection_method = self.get_element_info(self.path_flow[-1])[1]
            _selection_arg = self.get_element_info(self.path_flow[-1])[2]
            if _selection_method == "id":
                driver = driver.find_element_by_id(_selection_arg)
            elif _selection_method == "ids":
                driver = driver.find_elements_by_id(_selection_arg)
            elif _selection_method == "xpath":
                driver = driver.find_element_by_xpath(_selection_arg)
            elif _selection_method == "name":
                driver = driver.find_element_by_name(_selection_arg)
            elif _selection_method == "className":
                driver = driver.find_element_by_class_name(_selection_arg)
            elif _selection_method == "tagName":
                driver = driver.find_element_by_tag_name(_selection_arg)
            elif _selection_method == "tagNames":
                driver = driver.find_elements_by_tag_name(_selection_arg)
            elif _selection_method == "linkText":
                driver = driver.find_element_by_link_text(_selection_arg)
            elif _selection_method == "linkPartialText":
                driver = driver.find_element_by_partial_link_text(_selection_arg)
            elif _selection_method == "css":
                driver = driver.find_element_by_css_selector(_selection_arg)
            return self.element_selector(driver)
    
    def path_builder(self, parent_element):
        self.path_flow.append(parent_element)
        if self.path_flow[-1] == "window":
            return None
        else:
            parent_element = self.get_element_info(parent_element)[0]
            return self.path_builder(parent_element)
    
    def get_element(self):
        self.path_builder(self.element_name)
        element = self.element_selector(self.window)
        element_type = self.get_element_info(self.element_name)[3]
        if element_type != "" and sample_objects.OBJECT_MAP.has_key(element_type):
            return sample_objects.OBJECT_MAP[element_type](element)
        else:
            return element
