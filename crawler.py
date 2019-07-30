from urllib import request, parse
from bs4 import BeautifulSoup
import logging
import re
from collections import defaultdict

# DEBUG , INFO, WARNING, ERROR, CRITICAL
log_level = logging.INFO
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

class Url:

    parent = None
    url = None
    parsed_url = None

    def __init__(self, url_str, parent=None):
        self.parsed_url = parse.urlparse(url_str)
        self.url = url_str
        self.parent = parent

    def get_full_url(self):
        if self.parent is not None and len(self.parsed_url.netloc) == 0:
            joined_url = parse.urljoin(self.parent, self.parsed_url.path)
            return joined_url
        return url


    def isSameDomain(self, that):
        if that.url is None and self.url is not None:
            logger.debug("url is:", that.url)
            return False
        if that.url[0] == '#':
            logger.debug("Internal Link:", that.url)
            return False
        if len(that.parsed_url.netloc) == 0 and len(that.parsed_url.path) > 0:
            logger.debug("Empty netloc", that.url)
            return True
        if self.parsed_url.netloc == that.parsed_url.netloc :
            logger.debug("Same netloc", that.url)
            return True
        logger.debug("Checking {} {}".format(self.parsed_url.netloc , that.url) )
        return False

class Crawler:

    root_url=""
    depth=0
    parsed_root_url= None
    site_map = defaultdict(list)

    def __init__(self,url, depth):
        logger.info("init Crawler")
        self.root_url = url
        self.depth = depth
        self.parsed_root_url = Url(self.root_url)

    def crawl(self):
        visited = defaultdict(lambda: False)
        queue = []
        queue.append( (self.root_url, self.depth) )
        while len(queue) > 0:
            root_tuple = queue.pop(0)
            cur_url = root_tuple[0]
            cur_depth = root_tuple[1]
            if visited[cur_url] == False:
                logger.info("Visiting: {} at depth {}".format(cur_url, cur_depth))
                fp = request.urlopen(cur_url)
                visited[cur_url] = True
                mybytes = fp.read()
                mystr = mybytes.decode("utf8")
                fp.close()
                soup = BeautifulSoup( mystr, "html.parser")
                links = soup.find_all("a")
                for link in links:
                    link_url = link.get('href')
                    parsed_link = Url(link_url, self.root_url)
                    if self.parsed_root_url.isSameDomain(parsed_link):
                        logger.debug("Adding to map {self.root_url} {parsed_link.url}")
                        self.site_map[cur_url].append(parsed_link.parsed_url.path)
                        if cur_depth > 1:
                            queue.append( ( parsed_link.get_full_url() , cur_depth-1) )
            else:
                logger.info("Skipping: {} ".format(cur_url))
        return self.site_map
