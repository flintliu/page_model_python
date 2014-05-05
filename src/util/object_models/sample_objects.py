#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Actions of common object
author: Flint Liu
email: flintliu@hotmail.com
"""

class Button(object):
	def __init__(self, button):
		self.button = button

	def click(self):
		self.button.click()

class LabelInput(object):
	def __init__(self, label):
		self.label = label

	def set_keys(self, value):
		self.label.send_keys(value)
		self.label.send_keys("\n")

OBJECT_MAP = {"label_input": LabelInput,\
              "button": Button}
