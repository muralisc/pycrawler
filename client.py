#!/usr/bin/python3
import requests
import sys

server_url = sys.argv[1]
crawl_url = sys.argv[2]
depth = sys.argv[3]

r = requests.post( server_url, data={'url': crawl_url, 'depth': depth})
