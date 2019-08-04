#!/bin/python

import crawler
from flask import Flask, jsonify, request
import logging

log_level = logging.DEBUG
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/crawl', methods = ['POST'])
def hello_world():
    url = request.form['url']
    depth =  request.form['depth']
    logger.info("Recieved request for url: "+url+ " depth: " + depth )
    c = crawler.Crawler(url, int(depth))
    site_map = c.crawl()
    return jsonify( dict(site_map) )

if __name__ == '__main__':
    app.run()
