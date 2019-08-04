#!/bin/python

import crawler
from flask import Flask, jsonify, request
import logging
import json

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
    try:
        site_map = c.crawl()
    except:
        logger.error("Error while crawling", exc_info=True)
        return json.dumps('{ "message" : "Server error"}')
    return jsonify( dict(site_map) )

if __name__ == '__main__':
    app.run()
