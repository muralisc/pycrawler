### Goals

The project aims to build a tiny web crawler.

### Steps to run Server

```
virtualenv crawler_env
source ./crawler_env/bin/activate
pip install -r requirements.txt
python3 server.py
```



### Executing the client
```
python3 client.py http://127.0.0.1:5000/crawl https://github.com/muralisc/dotfiles 1 | jq '.'
```

#### Curl cli

```
curl http://127.0.0.1:5000/crawl -X POST -d "url=https://github.com/muralisc/dotfiles&depth=2" | jq '.'
```
