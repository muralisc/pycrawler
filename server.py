#!/bin/python

import crawler
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/crawl')
def hello_world():
    c = crawler.Crawler("https://www.rust-lang.org/", 1)
    site_map = c.crawl()
    return jsonify( dict(site_map) )

if __name__ == '__main__':
    app.run()
