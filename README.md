### Goals

The project aims to build a tiny web crawler.

### Steps to run Server


Create a virtual env
```
virtualenv crawler_env
source ./crawler_env/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Run the server
```
python3 server.py
```


### The client
```
python3 client.py <Server URL> <Site to crawl> <Depth> | jq '.'

python3 client.py http://127.0.0.1:5000/crawl https://github.com/muralisc/dotfiles 1 | jq '.'
```

### Test

```
python3 crawler_test.py
```

#### Curl cli

```
curl http://127.0.0.1:5000/crawl -X POST -d "url=https://github.com/muralisc/dotfiles&depth=2" | jq '.'
```
