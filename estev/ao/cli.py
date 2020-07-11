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
"""
from docopt import docopt
import requests
import pyperclip

from estev.ao import VERSION
from estev.ao.config import APP_DOMAIN
from estev.ao.config import API_ENDPOINT


def create_link(url: str) -> str:
    """Create a shorted version of the url"""
    result = requests.post(API_ENDPOINT + '/links', json={
        'url': url
    }).json()

    return APP_DOMAIN + '/u/' + result['slug']


def main():
    """
    Main entry point for the tool.
    """
    arguments = docopt(__doc__, version=f"{VERSION}")

    link = create_link(url=arguments['<url>'])

    pyperclip.copy(link)

    print(link)
