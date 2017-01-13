#! /usr/bin/env python

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if 'Hitler' in data: print data


def parseHtml(content):
    parser = MyHTMLParser()
    parser.feed(content)
