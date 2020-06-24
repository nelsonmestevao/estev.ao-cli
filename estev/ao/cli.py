#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""estev.ao

Usage:
  estev <url>
  estev (-h | --help)
  estev (-v | --version)

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  -l --lang=<lang>  Choose programming language [default: C].
  -d --debug        Run in debug mode for developting purposes.
"""
from docopt import docopt
import requests
import pyperclip

from estev.ao import VERSION


def create_link(url: str) -> str:
    """Create a shorted version of the url"""
    result = requests.post('http://api.estev.ao/links', json={
        'url': url
    }).json()

    return result['link']


def main():
    """
    Main entry point for the tool.
    """
    arguments = docopt(__doc__, version=f"{VERSION}")

    link = create_link(url=arguments['<url>'])

    pyperclip.copy(link)

    print(link)
