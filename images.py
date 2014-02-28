# -*- coding: utf-8 -*-
import os

class Item:

    def __init__(self, offset, seconds):
        self.offset = offset
        self.time_seconds = seconds
        self.date = ''
        self.percent = 0

    def set_offset(self, offset):
        self.offset = offset

    def set_time_seconds(self, seconds):
        self.time_seconds = seconds

    def set_date(self, date):
        self.date = date

    def set_percent(self, percent):
        self.percent = percent


class Image:

    def __init__(self, name):
        self.name = name
        self.item_list = []

    def add_item(self, offset, seconds):
        self.item_list.append(Item(offset, seconds))